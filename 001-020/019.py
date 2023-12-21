import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained GAN model
gan_model = load_model('path_to_your_gan_model.h5')

def detect_generator(image_path):
   # Load and preprocess the input image
   img = image.load_img(image_path, target_size=(64, 64)) # adjust target size based on your GAN model
   img_array = image.img_to_array(img)
   img_array = np.expand_dims(img_array, axis=0)
   img_array /= 255.0 # normalize pixel values to [0, 1]

   # Make predictions using the GAN model
   predictions = gan_model.predict(img_array)

   # Assuming binary classification (fake vs. real), you may need to adjust this based on your GAN model
   is_fake = predictions[0][0] > 0.5

   if is_fake:
     print("Generator Detected!")
   else:
     print("Not a Generator.")

# Example usage
image_path = 'path_to_test_image.jpg'
detect_generator(image_path)