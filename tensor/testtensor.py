
from torch.tensor import *

floattensor = torch.Tensor([[2,3],[3,1],[8,3]])

print("tensor is : {}".format(floattensor))
print(floattensor.shape)

array1 = floattensor.numpy()
print(array1)