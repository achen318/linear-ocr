import pickle

import matplotlib.pyplot as plt
import numpy as np

from models.base_model import BaseModel


class LeastSquares(BaseModel):
    def __init__(self):
        super().__init__("least_squares.model")

    def train(self, trainX, trainY) -> None:
        try:
            # If the model exists, load it
            with open(self.model_file, "rb") as f:
                self.model = pickle.load(f)

        except FileNotFoundError:
            # Perform linear regression with pseudo-inverse
            X = trainX.reshape(trainX.shape[0], -1)
            Y = trainY

            B = np.linalg.pinv(X.T @ X) @ X.T @ Y
            self.model = B

            # Save the model
            with open(self.model_file, "wb") as f:
                pickle.dump(self.model, f)

    def display(self) -> None:
        # Show the coefficients/weights matrix
        plt.imshow(self.model.reshape(28, 28), cmap="RdYlGn")
        plt.axis("off")
        plt.show()

    def predict(self, mat) -> str:
        X = mat.reshape(1, -1)
        Y = X @ self.model  # returns a decimal

        return round(Y[0])
