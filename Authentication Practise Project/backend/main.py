import os
import shutil
import uuid

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from auth import create_access_token, decode_token, hash_password, verify_password
from database import Base, engine, get_db
from models import User

# ============================================================
# APP INITIALIZATION & CONFIG
# ============================================================

app = FastAPI(title="React FastAPI Authentication API")

# Create database tables
Base.metadata.create_all(bind=engine)

# CORS setup
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup uploads directory
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/")
def home():
    return {"message": "FastAPI Authentication API is running"}


@app.post("/register")
def register(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Check if username already exists
    existing_username = db.query(User).filter(User.username == username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Check if email already exists
    existing_email = db.query(User).filter(User.email == email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Validate image extension
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    original_name = image.filename or ""
    extension = os.path.splitext(original_name)[1].lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG, PNG, and WEBP images are allowed"
        )

    # Save uploaded image
    image_name = f"{uuid.uuid4()}{extension}"
    image_path = os.path.join(UPLOAD_DIR, image_name)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Hash password and create user
    hashed_pwd = hash_password(password)
    new_user = User(
        username=username,
        email=email,
        hashed_password=hashed_pwd,
        image=image_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "image": new_user.image
        }
    }

#LOGIN
@app.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Authenticate user
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT
    access_token = create_access_token({"sub": str(user.id)})

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }



#PROFILE
@app.get("/profile")
def get_current_user(
    authorization: (str | None) = Header(default=None),
    db: Session = Depends(get_db)
):
    # Validate authorization header
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing authorization header"
        )

    token = authorization.split(" ", 1)[1]
    payload = decode_token(token)

    if not payload or not (user_id := payload.get("sub")):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    # Fetch user from database
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "image": user.image
    }