# def print_params(a = 1, b = 'строка', c = True):
#     print(a,b,c)
# print_params()
# print_params(10)
# print_params(10,'слово')
# print_params(b=25)
# print_params(c=[1, 2, 3])

#def print_params(a = 1, b = 'строка', c = True):
#     print(a,b,c)
# values_list = [29,'String', False]
# values_dict = {'a':2,'b':'выаыва','c': [45,56,67]}
# print_params(*values_list)
# print_params(**values_dict)

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = [29,'String', False]
values_dict = {'a':2,'b':'выаыва','c': [45,56,67]}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
