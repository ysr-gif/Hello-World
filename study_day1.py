"""
张量学习
张量 -> 存储同一类元素的存器，且元素值必须是数值
根据形状创建张量：
torch.tensor
torch.Tensor
torch.IntTensor、torch.FloatTensor、torch.DoubleTensor
"""

import torch
import numpy as np

#torch.tensor

def dm01():
    # 标量张量
    t1 = torch.tensor(1)

    #二维列表 -> 张量
    data = [[1,2,3],[4,5,6]]
    t2 = torch.tensor(data)

    #numpy nd数组 -> 张量
    data = np.random.randint(0,10,(2,3))
    t3 = torch.tensor(data,dtype=torch.float)


#torch.Tensor
def dm02():
    # 标量张量
    t1 = torch.Tensor(1)

    # 二维列表 -> 张量
    data = [[1, 2, 3], [4, 5, 6]]
    t2 = torch.Tensor(data)

    # numpy nd数组 -> 张量
    data = np.random.randint(0, 10, (2, 3))
    t3 = torch.Tensor(data)

    #直接创建指定维度张量
    t4 = torch.Tensor(2,3)


#torch.IntTensor、torch.FloatTensor、torch.DoubleTensor
def dm03():
    # 标量张量
    t1 = torch.IntTensor(1)

    # 二维列表 -> 张量
    data = [[1, 2, 3], [4, 5, 6]]
    t2 = torch.IntTensor(data)

    # numpy nd数组 -> 张量
    data = np.random.randint(0, 10, (2, 3))
    t3 = torch.IntTensor(data)

    # 如果类型不匹配，会尝试自动转换
    data = np.random.randint(0, 10, (2, 3))
    t4 = torch.FloatTensor(data)
