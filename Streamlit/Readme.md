# Fish Classification Streamlit App

## 🐟 Overview
This Streamlit application is designed to classify fish species using a trained **MobileNet model**. Users can upload an image of a fish, and the model will predict the species with confidence scores.

## 🚀 Features
- **Upload an image** of a fish for classification
- **Top-1 or Top-3 predictions** with confidence scores
- **Visualization of confidence scores** using bar charts
- **Progress bar** to indicate processing status
- **Dark mode support** for better readability
- **Responsive layout** for an improved user experience

## 🛠️ Installation
Ensure you have **Python 3.8+** installed. Then, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-repo/fish-classification-streamlit.git
cd fish-classification-streamlit

# Install dependencies
pip install -r requirements.txt
```

## 📂 Folder Structure
```
├── Model
│   ├── mobilenet_fish_classifier.h5
├── Streamlit
│   ├── fish_classifier.py
│   ├── README.md
├── Dataset
│   ├── train/
│   ├── val/
│   ├── test/
```

## 🎯 Usage
Run the Streamlit app with the following command:
```bash
streamlit run Streamlit/fish_classifier.py
```

## 🖼️ How It Works
1. **Upload an image** of a fish.
2. The app preprocesses the image and feeds it to the trained MobileNet model.
3. The model predicts the species and **displays the top-1 result**.
4. Users can **toggle to see the top-3 predictions**.
5. A **confidence score bar chart** provides a visual representation of predictions.

## 📊 Visual Enhancements
- **Bar chart** for model confidence levels.
- **Model comparison chart** (optional, if using multiple models).
- **Image augmentation preview** (if added in the future).

## 🤝 Contributions
Feel free to improve this app! Open a pull request with feature enhancements or bug fixes.

## 📜 License
This project is licensed under the MIT License.

