import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__))) # 追加
if parent_dir not in sys.path: # 追加
    sys.path.append(parent_dir) # 追加
apple = 100
apple_num = 2
tax = 1.1
from ch05.layer_naive import MulLayer
#layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)

#backward
dprice = 1 #dpriceは順伝播出力の微分の値を入れる
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax)