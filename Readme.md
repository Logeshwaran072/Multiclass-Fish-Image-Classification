# Multiclass Fish Image Classification

## 📌 Project Overview
This project focuses on **multiclass fish species classification** using deep learning. Various **CNN architectures** were trained and evaluated to identify the most accurate model for deployment. The selected model is deployed using a **Streamlit web application** for real-time predictions.

## 🏗️ Models Trained
The following deep learning models were trained and compared:
- **CNN from Scratch**
- **VGG16**
- **ResNet50**
- **MobileNet** (Selected for Deployment)
- **InceptionV3**
- **EfficientNetB0**

## 📂 Project Structure
```
├── Dataset
│   ├── train/  # Training images (11 classes)
│   ├── val/    # Validation images (11 classes)
│   ├── test/   # Testing images (11 classes)
│
├── Model
│   ├── cnn_fish_classifier.h5
│   ├── vgg16_fish_classifier.h5
│   ├── resnet50_fish_classifier.h5
│   ├── mobilenet_fish_classifier.h5  # Final selected model
│   ├── inceptionv3_fish_classifier.h5
│   ├── efficientnetb0_fish_classifier.h5
│
├── Notebooks
│   ├── 1_Data_Preprocessing.ipynb
│   ├── 2_Model_Training.ipynb
│   ├── 3_Model_Evaluation.ipynb
│
├── Streamlit
│   ├── fish_classifier.py  # Streamlit app
│   ├── README.md
│
│
└── README.md  # This file
```

## 🔍 Data Preprocessing
- Images were resized to **224x224** for compatibility with pre-trained models.
- Applied **data augmentation** (rotation, flipping, zoom) to enhance model generalization.
- Used **train-validation-test split** with an imbalance check and oversampling for underrepresented classes.

## 🏆 Model Selection
- **Evaluated models based on accuracy, precision, recall, and F1-score.**
- MobileNet outperformed other models in **accuracy vs. efficiency trade-off**, making it the best choice for real-time deployment.

## 🚀 Streamlit Web App
The **Streamlit application** allows users to upload an image and classify fish species with:
- **Top-1 and Top-3 predictions**
- **Confidence score visualization**
- **Processing progress bar**

## 🔧 Installation & Usage
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App
```bash
streamlit run Streamlit/fish_classifier.py
```

## 📊 Future Enhancements
- Improve dataset balance with **more images for underrepresented classes**
- **Optimize the MobileNet model** with quantization for better inference speed
- **Deploy via cloud services** for broader accessibility

## 📜 License
This project is licensed under the MIT License.

---
**Contributions are welcome!** If you have ideas for improvements, feel free to submit a pull request. 🚀

