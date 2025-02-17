import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("Image Resizer & X Poster")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Send the uploaded file to the backend for resizing
    files = {"file": uploaded_file.getvalue()}
    
    response = requests.post(f"{BACKEND_URL}/resize/", files=files)
    
    if response.status_code == 200:
        resized_images = response.json()
        
        st.write("Resized Images:")
        
        # Loop through the resized image paths and display them
        for file_path in resized_images["files"]:
            st.image(file_path, caption=f"Resized Image: {file_path}", use_container_width=True)
        
        # Post to X (Twitter)
        if st.button("Post to X"):
            post_response = requests.post(f"{BACKEND_URL}/post_to_x/", json={"images": resized_images["files"]})
            if post_response.status_code == 200:
                st.success("Images posted to X successfully!")
            else:
                st.error("Failed to post images to X.")
    else:
        st.error("Image processing failed.")
