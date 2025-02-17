from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import os
import tweepy
from dotenv import load_dotenv
import base64
import requests

app = FastAPI()

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Load Twitter API credentials from .env
API_KEY = "HLxLnhJTbJL1THn3SQ1clBfUO"
API_SECRET = "88IZmGGMl6CeU9mmoF07obwxfwGpzXNpneOVbtyLyiWLkdvTqf"
ACCESS_TOKEN = "1563973474963828736-IjsvYryRSQdhKjGgHdwF7f669MIrRq"
ACCESS_SECRET = "4CkiHCcut2vLRJADNrCDe6FsHFOgB4nsxsLJ64BhePiCq"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Twitter media upload URL
UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"

# Predefined image sizes
IMAGE_SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]

@app.post("/resize/")
async def resize_image(file: UploadFile = File(...)):
    # Get image data from the uploaded file
    image_data = await file.read()
    
    # Open the image
    image = Image.open(io.BytesIO(image_data))
    
    # Define the required sizes
    sizes = [(300, 250), (728, 90), (160, 600), (300, 600)]
    
    # Resize and save images
    saved_files = []
    for size in sizes:
        resized_image = image.resize(size)
        # Save the resized image to the 'static' folder with appropriate names
        file_path = f"static/{size[0]}x{size[1]}.png"
        resized_image.save(file_path)
        saved_files.append(file_path)
    
    return {"message": "Images resized and saved", "files": saved_files}


def upload_image_to_x(image_path):
    """Uploads an image to X (Twitter) and returns the media_id."""
    with open(image_path, "rb") as image_file:
        files = {"media": image_file}
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        response = requests.post(UPLOAD_URL, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("media_id_string")
        else:
            return None

@app.post("/post_to_x/")
async def post_to_x(images: list):
    """Uploads images to X and posts them as a tweet."""
    media_ids = []
    
    for image_path in images:
        media_id = upload_image_to_x(image_path)
        if media_id:
            media_ids.append(media_id)
    
    if media_ids:
        api.update_status(status="Here are my resized images!", media_ids=media_ids)
        return {"message": "Posted successfully!"}
    else:
        return {"error": "Failed to upload images"}
