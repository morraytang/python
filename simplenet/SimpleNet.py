
from torch import nn


class SimpleNet(nn.Module):
    def __init__(self,in_dim, h1_dim , h2_dim, out_dim):
        super(SimpleNet, self).__init__()
        # self.layer1 = nn.Linear(in_dim,h1_dim)
        # self.layer2 = nn.Linear(h1_dim,h2_dim)
        # self.layer3 = nn.Linear(h2_dim,out_dim)
        self.layer1 = nn.Sequential(
            nn.Linear(in_dim, h1_dim),
            nn.BatchNorm1d(h1_dim),
            nn.ReLU(True)
        )
        self.layer2 = nn.Sequential(
            nn.Linear(h1_dim, h2_dim),
            nn.BatchNorm1d(h2_dim),
            nn.ReLU(True)
        )
        self.layer3 = nn.Sequential(
            nn.Linear(h2_dim, out_dim),
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return  x

