import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__))) # 追加
if parent_dir not in sys.path: # 追加
    sys.path.append(parent_dir) # 追加
from ch05.layer_naive import MulLayer, AddLayer

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
all_price = add_apple_orange_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(all_price, tax)

print(price)

#backward
dprice = 1 #dpriceは順伝播出力の微分の値を入れる
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num,dorange, dorange_num, dtax)