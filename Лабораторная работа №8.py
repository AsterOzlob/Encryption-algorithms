# Алгоритм 1
def simple_transposition_cipher(text, key, pad_char='*'):
    # Определяем количество букв в группе
    b = len(key)

    # Добавляем специальные символы в конец текста, чтобы длина текста делилась нацело на b
    while len(text) % b != 0:
        text += pad_char

    print("Преобразованный текст с добавлением специальных символов:", text)

    # Разбиваем текст на группы по b букв
    groups = [text[i:i + b] for i in range(0, len(text), b)]

    # Выводим матрицу исходного текста
    print("Матрица исходного текста:")
    for group in groups:
        print(' '.join(group))

    # Переставляем символы в каждой группе
    transposed_groups = []
    for group in groups:
        transposed_group = ''.join(group[key[i] - 1] for i in range(b))
        transposed_groups.append(transposed_group)

    # Выводим матрицу с перестановкой
    print("Матрица с перестановкой символов:")
    for transposed_group in transposed_groups:
        print(' '.join(transposed_group))

    # Объединяем группы обратно в строку
    encrypted_text = ''.join(transposed_groups)
    return encrypted_text


def reverse_order(key):
    reversed_order = [0] * len(key)
    for i, pos in enumerate(key):
        reversed_order[pos - 1] = i + 1
    return reversed_order


def simple_transposition_decipher(text, key, pad_char='*'):
    # Определяем количество букв в группе
    b = len(key)

    # Разбиваем текст на группы по b букв
    groups = [text[i:i + b] for i in range(0, len(text), b)]

    # Выводим матрицу зашифрованного текста
    print("Матрица зашифрованного текста:")
    for group in groups:
        print(' '.join(group))

    # Получаем обратный порядок
    reversed_order = reverse_order(key)

    # Переставляем символы в каждой группе в обратном порядке
    original_groups = []
    for group in groups:
        original_group = ''.join(group[reversed_order[i] - 1] for i in range(b))
        original_groups.append(original_group)

    # Выводим матрицу с восстановленными символами
    print("Матрица с восстановленными символами:")
    for original_group in original_groups:
        print(' '.join(original_group))

    # Объединяем группы обратно в строку
    decrypted_text = ''.join(original_groups)

    # Убираем специальные символы
    decrypted_text = decrypted_text.rstrip(pad_char)
    return decrypted_text


if __name__ == "__main__":
    encrypted_text = simple_transposition_cipher("Тимошенко_Антон_Дмитриевич", [3, 1, 6, 4, 2, 5])
    print(encrypted_text, '\n')
    decrypted_text = simple_transposition_decipher("епаьчлан_сяиоти_ря", [2, 1, 4, 6, 3, 5])
    print(decrypted_text)
