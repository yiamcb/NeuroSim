# model_cnn_attention.py
import torch
import torch.nn as nn

class CNN_Attention(nn.Module):
    def __init__(self, n_channels=19, seq_len=2560):
        super().__init__()
        self.conv = nn.Conv1d(n_channels, 32, 5, padding=2)
        self.attn = nn.MultiheadAttention(32, 4)
        self.fc = nn.Linear(32, 3)

    def forward(self, x):
        x = self.conv(x)
        x = x.permute(2,0,1)
        x,_ = self.attn(x,x,x)
        x = x.mean(0)
        return self.fc(x)
