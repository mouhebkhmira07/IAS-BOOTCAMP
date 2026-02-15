import os
from roboflow import Roboflow

def download_model():
    """
    Downloads the YOLOv8 model from Roboflow using the provided API key and project info.
    Returns the path to the downloaded model.
    """
    api_key = "xcQkFJhGXtteV0tNvzod"
    rf = Roboflow(api_key=api_key)
    project = rf.workspace("laser-detection-cco13").project("laser-detection-w531n")
    version = project.version(1)
    
    # Download the dataset/model
    # Note: version.download("yolov8") would download the model weight files directly 
    # if it's a deployment-ready model.
    dataset = version.download("yolo26")
    
    print(f"Model version {version.version} downloaded to {dataset.location}")
    return dataset.location

if __name__ == "__main__":
    download_model()
