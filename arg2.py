# Написать Функцию которая принимает предложение как аргумент,
# считает количество букв и возвращает сколько символов он ввёл.
# НЕ ИСПОЛЬЗОВАТЬ функцию len()
text = input("Введите текст: ")


def main(text):
    count = 0
    for i in text:
        count += 1
    return count


print('Количество букв в предложении: ', main(text))
