from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# داده‌های آموزش و آزمایش
# در اینجا فرض کنید X ماتریس ویژگی‌ها و y برچسب‌ها باشند
# برای مثال:
# X = [[feature1_1, feature2_1], [feature1_2, feature2_2], ...]
# y = [label1, label2, ...]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد یک مدل k-NN
knn_model = KNeighborsClassifier(n_neighbors=3)

# آموزش مدل
knn_model.fit(X_train, y_train)

# پیش‌بینی برچسب‌ها برای داده‌های آزمایش
y_pred = knn_model.predict(X_test)

# ارزیابی دقت
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")