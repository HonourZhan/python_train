import numpy as np
import matplotlib.pyplot as plt
import h5py
from lr_utils import load_dataset

train_set_x_orig , train_set_y , test_set_x_orig , test_set_y , classes = load_dataset()

index = 25
plt.imshow(train_set_x_orig[12])
# print("train_set_y=" + str(train_set_y)) #你也可以看一下训练集里面的标签是什么样的。
