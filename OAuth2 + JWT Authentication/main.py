# ============================================================
# STEP 1: প্রয়োজনীয় Library Import
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
# FastAPI → API তৈরি করার জন্য
# HTTPException → Error response দেওয়ার জন্য
# Depends → Dependency Injection ব্যবহার করার জন্য

from jose import jwt, JWTError
# jwt → JWT token তৈরি ও decode করার জন্য
# JWTError → Token ভুল হলে error ধরার জন্য

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# OAuth2PasswordBearer → Bearer token নেওয়ার জন্য
# OAuth2PasswordRequestForm → Login form থেকে username/password নেওয়ার জন্য

from datetime import datetime, timedelta, timezone
# Token-এর expiration time সেট করার জন্য

from passlib.context import CryptContext
# Password hash এবং verify করার জন্য


# ============================================================
# STEP 2: FastAPI Application তৈরি
# ============================================================

app = FastAPI()
# FastAPI-এর application object তৈরি করছি


# ============================================================
# STEP 3: JWT Configuration
# ============================================================

SECRET_KEY = "mysecret"
# JWT token sign/encrypt করার জন্য secret key

ALGORITHM = "HS256"
# JWT token তৈরি করার জন্য কোন algorithm ব্যবহার হবে

ACCESS_TOKEN_EXPIRE_MINUTES = 30
# Login করার পর token 30 মিনিট পর্যন্ত valid থাকবে


# ============================================================
# STEP 4: Password Hashing Setup
# ============================================================

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)
# Password সরাসরি database-এ রাখা হবে না
# Password-কে hash করে রাখা হবে


# ============================================================
# STEP 5: OAuth2 Setup
# ============================================================

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")
# Protected API ব্যবহার করার সময়
# User-এর কাছ থেকে Bearer Token নেওয়ার ব্যবস্থা করছে
#
# tokenUrl="login" মানে login করার endpoint হলো /login


# ============================================================
# STEP 6: Dummy User Database
# ============================================================

fake_user_db = {
    "admin": {
        "username": "admin",

        # আসল password "1234"
        # কিন্তু database-এ password hash করে রাখা হচ্ছে
        "hashed_password": pwd_context.hash("1234")
    }
}

# Practice করার জন্য আমরা এখানে fake database ব্যবহার করছি
# Real project-এ এখানে PostgreSQL/MySQL/MongoDB ব্যবহার করা হবে


# ============================================================
# STEP 7: Password Hash করার Function
# ============================================================

def hash_password(password: str):
    # User-এর normal password নিয়ে hash তৈরি করবে
    return pwd_context.hash(password)


# ============================================================
# STEP 8: Password Verify করার Function
# ============================================================

def verify_password(plain_password, hashed_password):
    # User-এর দেওয়া password
    # database-এর hashed password-এর সাথে মিলিয়ে দেখবে

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ============================================================
# STEP 9: JWT Token তৈরি করার Function
# ============================================================

def create_token(data: dict):

    # Original data-এর একটি copy তৈরি করছি
    to_encode = data.copy()

    # Token কখন expire হবে সেটা নির্ধারণ করছি
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Token-এর মধ্যে expiration time যোগ করছি
    to_encode.update({
        "exp": expire
    })

    # JWT token তৈরি করছি
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# ============================================================
# STEP 10: Login API
# ============================================================

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    # User যে username দিয়েছে
    # সেই username দিয়ে fake database থেকে user খুঁজছি
    user = fake_user_db.get(form_data.username)

    # User না থাকলে অথবা password ভুল হলে
    # Login করতে দেওয়া হবে না
    if not user or not verify_password(
        form_data.password,
        user["hashed_password"]
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid Username or Password"
        )

    # Login successful হলে JWT token তৈরি করছি
    access_token = create_token({
        "sub": form_data.username
    })

    # Client-এর কাছে token পাঠিয়ে দিচ্ছি
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ============================================================
# STEP 11: JWT Token Verify করার Function
# ============================================================

def verify_token(
    token: str = Depends(oauth2_schema)
):

    try:

        # Token decode করে তার ভিতরের data বের করছি
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Token-এর "sub" থেকে username বের করছি
        username: str = payload.get("sub")

        # Username না থাকলে token invalid
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        # Token valid হলে username return করছি
        return username

    except JWTError:

        # Token expired / wrong / invalid হলে এখানে আসবে
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


# ============================================================
# STEP 12: Protected Route
# ============================================================

@app.get("/protected")
def protected_route(
    username: str = Depends(verify_token)
):

    # এই API ব্যবহার করতে হলে আগে valid JWT token লাগবে
    return {
        "message": f"Hello {username}, you have access to this protected route!"
    }