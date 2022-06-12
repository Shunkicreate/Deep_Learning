import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__))) # 追加
if parent_dir not in sys.path: # 追加
    sys.path.append(parent_dir) # 追加
# sys.path.append('ch3')
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
    
(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)