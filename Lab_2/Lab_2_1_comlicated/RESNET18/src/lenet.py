import mindspore.nn as nn
from mindspore.common.initializer import Normal
from mindspore.ops import operations as P

class ResidualBlock(nn.Cell):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, pad_mode='pad')
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, pad_mode='pad')
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = None
        if stride != 1 or in_channels != out_channels:
            self.downsample = nn.SequentialCell([
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, padding=0),
                nn.BatchNorm2d(out_channels)
            ])
        self.add = P.TensorAdd()

    def construct(self, x):
        identity = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        if self.downsample is not None:
            identity = self.downsample(identity)
        out = self.add(out, identity)
        out = self.relu(out)
        return out

class ResNet18(nn.Cell):
    def __init__(self, num_class=10, num_channel=1):
        super(ResNet18, self).__init__()
        self.conv1 = nn.Conv2d(num_channel, 64, kernel_size=7, stride=2, padding=3, pad_mode='pad')
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1, pad_mode='pad')
        self.layer1 = self.make_layer(64, 64, stride=1, blocks=2)
        self.layer2 = self.make_layer(64, 128, stride=2, blocks=2)
        self.layer3 = self.make_layer(128, 256, stride=2, blocks=2)
        self.layer4 = self.make_layer(256, 512, stride=2, blocks=2)
        self.mean = P.ReduceMean(keep_dims=True)
        self.flatten = nn.Flatten()
        self.fc = nn.Dense(512, num_class, weight_init=Normal(0.02))

    def make_layer(self, in_channels, out_channels, stride, blocks):
        layers = []
        layers.append(ResidualBlock(in_channels, out_channels, stride))
        for _ in range(1, blocks):
            layers.append(ResidualBlock(out_channels, out_channels, stride=1))
        return nn.SequentialCell(layers)

    def construct(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.mean(x, (2, 3))
        x = self.flatten(x)
        x = self.fc(x)
        return x
