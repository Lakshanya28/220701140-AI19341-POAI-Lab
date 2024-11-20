import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Dummy data for regression
X = np.array([[7, 100], [6, 120], [4, 90], [8, 150], [5, 130]])  # Features: Crunchiness, Weight
y = np.array([7, 8, 4, 9, 6])  # Target: Sweetness

# Build the model
model = Sequential([
    Input(shape=(2,)),              # Define the input shape
    Dense(8, activation='relu'),    # Hidden layer
    Dense(1, activation='linear')   # Output layer (1 continuous output)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# Train the model
model.fit(X, y, epochs=50, verbose=0)

# Test the model
test_data = np.array([[6, 110]])  # Test sample: Crunchiness, Weight
pred = model.predict(test_data)
print("Predicted Sweetness:", pred[0][0])
