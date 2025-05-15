# ✍️ HANDWRITE-AI: Handwritten Digit Recognition using MNIST

**HANDWRITE-AI** is a deep learning project that uses Convolutional Neural Networks (CNNs) to recognize handwritten digits using the **MNIST** dataset. It includes both training and prediction workflows and comes with a **Streamlit** web app for real-time digit recognition.

---


---

## 🔍 Overview

The MNIST dataset contains **70,000 grayscale images** of handwritten digits (0–9). This project builds and trains CNN models on this dataset, allowing accurate digit classification.

---

## 🧠 Features

- CNN-based architecture using Keras & TensorFlow  
- Trained models saved in `.h5` format  
- Jupyter notebooks for training, evaluation, and prediction  
- **Streamlit app** for easy-to-use web-based prediction  
- CLI-based prediction using `predict.py`  
- Modular and scalable code structure

---

## 📊 Model Performance

- **Training Accuracy**: ~99%  
- **Test Accuracy**: ~99%  
- Evaluation metrics available in `evaluation.ipynb`

---

## 🚀 How to Run

### 🖥️ 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 🌐 2. Run the Streamlit App
Launch the web interface for digit prediction:
```bash
streamlit run App.py
```
## 📌 Future Enhancements
- Extend model to support handwritten letters using EMNIST dataset
- Improve preprocessing for real-world handwriting
- Integration with live camera feed for real-time digit recognition
- Deploy the app using Streamlit Cloud or HuggingFace Spaces