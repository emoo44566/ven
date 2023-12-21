import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# تولید داده‌های مصنوعی برای آموزش مدل
# در اینجا مثالی از ویژگی‌های ژنراتور و غیر ژنراتور ایجاد شده است.
# شما باید داده‌های واقعی خود را جایگزین کنید.
generator_data = np.random.rand(1000, 10) # 1000 نمونه از ویژگی‌های ژنراتور
non_generator_data = np.random.rand(1000, 10) # 1000 نمونه از ویژگی‌های غیر ژنراتور

# برچسب‌ها: 1 برای ژنراتور و 0 برای غیر ژنراتور
generator_labels = np.ones((1000, 1))
non_generator_labels = np.zeros((1000, 1))

# ترکیب داده‌ها
all_data = np.concatenate([generator_data, non_generator_data], axis=0)
all_labels = np.concatenate([generator_labels, non_generator_labels], axis=0)

# مخلوط کردن داده‌ها
indices = np.arange(all_data.shape[0])
np.random.shuffle(indices)
all_data = all_data[indices]
all_labels = all_labels[indices]

# تقسیم داده‌ها به دو بخش آموزش و آزمون
split = int(0.8 * all_data.shape[0])
train_data, test_data = all_data[:split], all_data[split:]
train_labels, test_labels = all_labels[:split], all_labels[split:]

# ساخت مدل
model = keras.Sequential([
   layers.Dense(64, activation='relu', input_shape=(10,)),
   layers.Dense(1, activation='sigmoid')
])

# تعریف توابع هزینه و بهینه‌ساز
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# آموزش مدل
model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

# ارزیابی مدل
test_loss, test_accuracy = model.evaluate(test_data, test_labels)
print(f"Test Accuracy: {test_accuracy}")

# پیش‌بینی برچسب برای چند نمونه تست
predictions = model.predict(test_data[:5])
print(f"Predictions: {predictions}")