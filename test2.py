# 张量运算

import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([2, 2, 2, 2, 2])
# 两个相同形状的张量对应元素的计算
print(x+y)
print(x-y)
print(x/y)
print(x**y)
print(x == y)

print(torch.exp(x))  # 连接两个tensor
print(torch.cat((x, y), dim=0))
# 连接两个tensor
print(torch.cat((x, y), dim=-1))
# 连接两个tensor
print(torch.cat((x, y), dim=0))
# 连接两个tensor 按行连接（没有效果，可能要2维的向量）
print(torch.cat((x, y), dim=0))
# 连接两个tensor 按列连接
print(torch.cat((x, y), dim=-1))
# 广播机制
print(x+y.reshape(5, 1))

# 索引和切片
print(x[0])
print(x[:-1])
X = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(X)
X[1, 1] = 9
print(X)
print(X[0])
print(X[0:2, 0:2])
# 不重新分配内存 id()查看内存是否一样
before = id(X)
print(before)
X = X + X
print(X)
print(id(X))
X[:] = X+X
print(id(X))
