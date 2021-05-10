# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.

def dictionary(**kwargs):
    my_dict = [ ]
    my_dict.append([kwargs["key"]])
    my_dict.append([kwargs["key2"]])
    return my_dict


a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}

print(dictionary(key=a, key2=b))
