# step 7(Функции)
# def get_summ(one, two, delimiter='&'):
#     one =str(one).capitalize()
#     two =str(two).capitalize()
#     return one + delimiter + two
# result_string = get_summ('learn', 'python')
# print(result_string)

def format_price(price):
    price = int(price)
    return f"Цена: {price} руб."

test_price=format_price(56.24)
print(test_price)