from fastapi import FastAPI,UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil


app=FastAPI()

#Step 1 -> Ensure Uploads folder exists
UPLOAD_DIR="Uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#Step 2 >Static File set-up
#HTTP : HTTP://127.0.1:8000/files/<filename>
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


#Step 3 -> Upload File Api
@app.post("/uploadfile")
def upload_file(file: UploadFile = File(...)):
    filename=file.filename
    file_path=os.path.join(UPLOAD_DIR,filename)
    if not filename:
        raise HTTPException(status_code=400, detail="No file selected")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": filename, "message": "File uploaded successfully", "fileurl": f"http://127.0.0.1:8000/files/{filename}"}

#Step 4 -> Get File URL API
@app.get("/files/{filename}")
def get_file_url(filename: str):
    file_path=os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")   
    return {"fileurl": f"http://127.0.0.1:8000/files/{filename}"}

@app.get("/")
def home():
    return {"message": "Welcome to the File Upload API."}