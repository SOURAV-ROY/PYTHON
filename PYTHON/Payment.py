# import math
price = 10
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
# print(f'Down Payment: {down_payment}')
# print('Down Payment: ', down_payment)
# result = price ** 2
result = pow(price, 4)
print('Multiply ', result)
