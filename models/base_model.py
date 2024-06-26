class BaseModel:
    def __init__(self, model_file):
        self.model = {}
        self.model_file = model_file

    def train(self, trainX, trainY) -> None: ...

    def predict(self, mat) -> int: ...

    def test(self, testX, testY) -> float:
        correct = 0
        total = 0

        for mat, label in zip(testX, testY):
            if self.predict(mat) == label:
                correct += 1

            total += 1

        return correct / total
