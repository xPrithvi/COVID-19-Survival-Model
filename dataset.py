import torch
from torch.utils.data import Dataset, DataLoader

class COVID_DATASET(Dataset):
    def __init__(self, X, Y):

        # Converting X and Y to tensors,
        self.Y = torch.from_numpy(Y)
        self.X = torch.from_numpy(X)
        del X, Y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.Y[index]