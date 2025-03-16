import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import time  

st.set_page_config(page_title="Fish Classification", page_icon="🐟", layout="wide")

# Load the trained MobileNet model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("D:/Project/Multiclass_project/Model/mobilenet_update_fish_classifier.h5")
    return model

model = load_model()

# Define class labels (Update these to match your dataset)
class_labels = ['animal fish',
 'animal fish bass',
 'fish sea_food black_sea_sprat',
 'fish sea_food gilt_head_bream',
 'fish sea_food hourse_mackerel',
 'fish sea_food red_mullet',
 'fish sea_food red_sea_bream',
 'fish sea_food sea_bass',
 'fish sea_food shrimp',
 'fish sea_food striped_red_mullet',
 'fish sea_food trout']

# Streamlit UI


# Sidebar - Upload Image
st.sidebar.title("🔍 Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Sidebar - Model Info
st.sidebar.write("✅ **Model:** MobileNet")
st.sidebar.write("🧠 **Trained on:** Multiclass Fish Dataset")
st.sidebar.write("📌 **Image Size:** 224x224")

st.title("🐟 Fish Species Classification")
st.write("Upload an image to classify the fish species.")

# Dark Mode Toggle
#dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

if uploaded_file is not None:
    # Open image using PIL and Resize for Display
    img = Image.open(uploaded_file)
    st.image(img, caption="🖼 Uploaded Image", width=300) 

    # Progress Bar
    with st.spinner("🔄 Processing... Please wait."):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)

    # Preprocess image
    img = img.resize((224, 224))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  

    # Make prediction
    predictions = model.predict(img_array)
    sorted_indices = np.argsort(predictions[0])[::-1]  # Sort in descending order

    # Display top 1 prediction
    st.success("✅ Classification Complete!")
    st.subheader(f"🏆 Prediction: **{class_labels[sorted_indices[0]]}**")
    st.progress(float(predictions[0][sorted_indices[0]]))  # Show confidence level
    st.write(f"🎯 Confidence: **{predictions[0][sorted_indices[0]] * 100:.2f}%**")

    # User option to show top 3 predictions
    show_top_3 = st.checkbox("📊 Show Top 3 Predictions")

    if show_top_3:
        st.write(f"🥈 **2nd:** {class_labels[sorted_indices[1]]} ({predictions[0][sorted_indices[1]] * 100:.2f}%)")
        st.write(f"🥉 **3rd:** {class_labels[sorted_indices[2]]} ({predictions[0][sorted_indices[2]] * 100:.2f}%)")

    # Downloadable Classification Report
    report_text = f"""
    🏆 Prediction: {class_labels[sorted_indices[0]]}
    🎯 Confidence: {predictions[0][sorted_indices[0]] * 100:.2f}%
    🥈 2nd Best: {class_labels[sorted_indices[1]]} ({predictions[0][sorted_indices[1]] * 100:.2f}%)
    🥉 3rd Best: {class_labels[sorted_indices[2]]} ({predictions[0][sorted_indices[2]] * 100:.2f}%)
    """
    st.download_button("📄 Download Report", report_text, file_name="classification_report.txt")
