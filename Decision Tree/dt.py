from sklearn.tree import DecisionTreeClassifier

# Example dataset for gender classification
# Features: [Height, Weight, Shoe Size]
X = [
    [180, 75, 42],  # Male
    [160, 60, 38],  # Female
    [170, 65, 40],  # Male
    [155, 55, 36],  # Female
    [165, 62, 39],  # Female
    [175, 70, 41]   # Male
]

# Labels: 0 for Female, 1 for Male
Y = [1, 0, 1, 0, 0, 1]

# Initialize DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X, Y)

# Predict gender using random values for [Height, Weight, Shoe Size]
# Example prediction for a new individual
prediction = clf.predict([[170, 65, 40]])

# Display the output
if prediction[0] == 1:
    print("Predicted Gender: Male")
else:
    print("Predicted Gender: Female")
