import pandas as pd


class Data:

    def __init__(self, path):
        df = pd.read_csv(path)
        self.data = df.to_dict(orient="list")

    def select_features(self, features):
        self.data = {k: self.data[k] for k in features}  # construct dict only with the features we have
