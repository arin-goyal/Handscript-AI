import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

def predict_digit_from_path(image_path, model_path='model/handwritten.h5'):
    # Load the trained model
    model = tf.keras.models.load_model(model_path)
    
    # Open and process the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = ImageOps.invert(image)               # Invert background if white
    image = image.resize((28, 28))               # Resize to MNIST format
    image_array = np.array(image).astype('float32') / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(image_array)
    predicted_digit = np.argmax(prediction)

    return predicted_digit

# Example usage
if __name__ == '__main__':
    img_path = "C:\\Users\\Asus\\Downloads\\sample.png"  # Or any other image path
    result = predict_digit_from_path(img_path)
    print(f"Predicted Digit: {result}")
