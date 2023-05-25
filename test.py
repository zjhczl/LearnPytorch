# tensor
import torch

x = torch.arange(12)
print(x)
print(x.shape)
x2 = x.reshape(3, 4)
print(x2)
# -1可以自动计算维度
print(x.reshape(3, -1))

print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))

print(torch.tensor([[1, 2, 3], [5, 1, 1]]))
