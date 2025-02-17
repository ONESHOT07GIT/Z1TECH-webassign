
# Image Resizer & X Poster

## Overview
This project allows users to upload an image, resize it to multiple sizes, and post the resized images on X (formerly known as Twitter). The frontend is built with **Streamlit**, while the backend is powered by **FastAPI**. It interacts with the **Twitter API** to upload images as media and post them as tweets.

## Features
- **Image Upload**: Users can upload PNG, JPG, or JPEG images.
- **Image Resizing**: The images are resized to predefined sizes (300x250, 728x90, 160x600, 300x600).
- **Post to X (Twitter)**: After resizing the images, users can choose to post them to X with a tweet.

## Prerequisites
- Python 3.7+
- Streamlit
- FastAPI
- Tweepy (for interacting with Twitter API)
- Python Imaging Library (PIL)
- Requests
- dotenv (to load API keys)

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-resizer-x-poster.git
cd image-resizer-x-poster
```

### 2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Setup Twitter API credentials
- Create a `.env` file in the project root and add your Twitter API credentials:
  ```bash
  API_KEY=your_api_key
  API_SECRET=your_api_secret
  ACCESS_TOKEN=your_access_token
  ACCESS_SECRET=your_access_secret
  ```

### 5. Run the Backend (FastAPI)
```bash
uvicorn main:app --reload
```

### 6. Run the Frontend (Streamlit)
```bash
streamlit run app.py
```

## How It Works
1. **Frontend** (Streamlit): Users upload an image via the Streamlit interface.
2. **Backend** (FastAPI): The uploaded image is resized to multiple sizes, and the resized images are saved in the `static/` directory.
3. **Twitter Integration**: The resized images are uploaded to X (Twitter) as media, and a tweet is posted with the uploaded images.

## API Endpoints
- **POST /resize/**: Accepts an image and resizes it to predefined sizes.
  - Request: Multipart form-data (image file).
  - Response: JSON with the paths to the resized images.
  
- **POST /post_to_x/**: Accepts a list of resized image paths and posts them as a tweet on X.
  - Request: JSON with a list of image paths.
  - Response: Success or error message.

## Example Usage
1. Upload an image using the frontend.
2. View the resized images.
3. Post the resized images to X with a click of a button.

## Development and Contribution
Feel free to fork this repository and contribute to the project. To contribute:
- Clone the repository.
- Create a new branch.
- Make your changes.
- Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
