import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.utils import to_categorical

# Dummy data for classification
X = np.array([[7, 7], [8, 6], [5, 4], [3, 8], [2, 9]])  # Features: Sweetness, Crunchiness
y = np.array([0, 0, 1, 1, 1])  # Labels: 0 for Apple, 1 for Orange

# One-hot encode the labels
y_categorical = to_categorical(y)

# Build the model
model = Sequential([
    Input(shape=(2,)),              # Define the input shape
    Dense(8, activation='relu'),    # Hidden layer
    Dense(2, activation='softmax')  # Output layer (2 classes)
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y_categorical, epochs=50, verbose=0)

# Test the model
test_data = np.array([[6, 6]])  # Test sample: Sweetness, Crunchiness
pred = model.predict(test_data)
print("Prediction (Class Probabilities):", pred)
print("Predicted Class:", np.argmax(pred))
