# tensor和numpy的相互转换
import torch
import numpy

A = torch.tensor([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
print("A:", end="")
print(A)

B = A.numpy()
print("B:", end="")
print(B)

C = torch.tensor(B)
print("C:", end="")
print(C)
# 将大小为1的张量转换为标量
a = torch.tensor([4.1])
print(a)
print(a.item())
print(float(a))
print(int(a))
