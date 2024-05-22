from tensorflow.keras.datasets import mnist

from models.mean_matrix import MeanMatrix
from models.mean_value import MeanValue

model = MeanMatrix()

# Load the dataset
(trainX, trainY), (testX, testY) = mnist.load_data()

# Normalize pixel data to be float32 in [0, 1]
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# Convert expected outputs to strings
trainY = trainY.astype(str)
testY = testY.astype(str)

# Train the model
model.train(trainX, trainY)

# Test the model
correct, total = model.test(testX, testY)

# Display results
print(f"{correct}/{total} correctly classified")
print(f"{correct/total*100}% accurate")
