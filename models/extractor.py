import torch
from torch import nn
from utils.image import get_model


class FeatureExtractor(nn.Module):
    def __init__(self, arch="vgg19_bn"):
        super().__init__()
        self.model, _ = get_model(arch)

        self.model = self.model.eval()

    def forward(self, x):
        return self.model(x)
