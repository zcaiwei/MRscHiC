import torch
import torch.nn as nn
import torch.nn.functional as F



class AutoEncoder(nn.Module):
    def __init__(self,ndim,outdim,hid1,hid2):
        super(AutoEncoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(ndim, hid1),
            nn.Tanh(),
            nn.Linear(hid1, hid2),
            nn.Tanh(),
            nn.Linear(hid2, outdim),
            #nn.ReLU(),
            #nn.Linear(16, 2),
        )

        self.decoder = nn.Sequential(
            #nn.Linear(2, 16),
            #nn.ReLU(),
            nn.Linear(outdim,hid2),
            nn.Tanh(),
            nn.Linear(hid2, hid1),
            nn.Tanh(),
            nn.Linear(hid1, ndim),
#            nn.Tanh()
#            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded