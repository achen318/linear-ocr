import pickle

import numpy as np

from models.base_model import BaseModel


class MeanMatrix(BaseModel):
    def __init__(self):
        super().__init__("mean_matrix.model")

    def train(self, trainX, trainY) -> None:
        try:
            # If the model exists, load it
            with open(self.model_file, "rb") as f:
                self.model = pickle.load(f)

        except FileNotFoundError:
            # Train the model
            for mat, label in zip(trainX, trainY):
                if label not in self.model:
                    self.model[label] = np.zeros(mat.shape)

                # Accumulate the mean of matrices
                self.model[label] += mat / len(trainX)

            # Save the model
            with open(self.model_file, "wb") as f:
                pickle.dump(self.model, f)

    def predict(self, mat) -> int:
        closest_label = -1
        closest_dist = np.inf

        for label, label_mean in self.model.items():
            # Minimize the Frobenius norm of the difference in matrices
            dist = np.linalg.norm(mat - label_mean)

            if dist < closest_dist:
                closest_dist = dist
                closest_label = label

        return closest_label
