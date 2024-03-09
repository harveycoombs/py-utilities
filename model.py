# Written by Harvey Coombs, 2024
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

class Model(nn.Module):
    def __init__(self, vocab_size, d_model=256, nhead=8, num_encoder_layers=6):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer = nn.Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers)
        self.fc = nn.Linear(d_model, vocab_size)

    def forward(self, src, tgt):
        src, tgt = self.embedding(src), self.embedding(tgt)
        output = self.transformer(src.permute(1, 0, 2), tgt.permute(1, 0, 2))
        return self.fc(output.permute(1, 0, 2))

class MaskedDataset(Dataset):
  # to-do

torch.save(model.state_dict(), "model.pth")
