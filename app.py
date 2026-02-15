import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
from roboflow import Roboflow

# Page config
st.set_page_config(page_title="Laser Leak Detector", page_icon="🔦", layout="wide")

# Title and Description
st.title("🔦 Laser Leak Detection System")
st.markdown("""
Monitor air leakage in industrial pipes by detecting **laser loss**.
This system uses a trained YOLOv8 model to identify laser signatures on pipe surfaces.
""")

# Sidebar for configuration
st.sidebar.header("Model Configuration")
api_key = st.sidebar.text_input("Roboflow API Key", value="xcQkFJhGXtteV0tNvzod", type="password")
project_id = st.sidebar.text_input("Project ID", value="laser-detection-w531n")
version_id = st.sidebar.number_input("Version", value=1, min_value=1)

# Initialize Roboflow
@st.cache_resource
def get_model(api_key, project_id, version_id):
    try:
        rf = Roboflow(api_key=api_key)
        project = rf.workspace().project(project_id)
        model = project.version(version_id).model
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = get_model(api_key, project_id, version_id)

# Main Interface
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Input Data")
    uploaded_file = st.file_uploader("Upload an image of the pipe...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

with col2:
    st.header("Analysis")
    if uploaded_file is not None and model is not None:
        if st.button("Run Leak Detection"):
            with st.spinner("Analyzing..."):
                # Run prediction
                # Note: Model prediction might require a temporary file
                temp_filename = "temp_input.jpg"
                image.save(temp_filename)
                
                prediction = model.predict(temp_filename, confidence=40, overlap=30).json()
                
                # Cleanup
                os.remove(temp_filename)
                
                # Process predictions
                predictions = prediction.get('predictions', [])
                
                if not predictions:
                    st.warning("🚨 ALERT: NO LASER DETECTED! Potential air leakage detected in this section.")
                else:
                    st.success(f"✅ Laser signature found! {len(predictions)} detections confirmed.")
                    
                    # Display Raw JSON for debugging (expandable)
                    with st.expander("Show Raw Detection Data"):
                        st.json(prediction)
    else:
        st.info("Please upload an image and ensure the API key is correct to start analysis.")

# Project Info
st.divider()
st.info("Built for IAS Bootcamp — Laser Leak Detection Mission")
