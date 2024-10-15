# Создает матрицу Плейфера на основе заданного ключа.
def create_playfair_square(key: str) -> list:
    # Создание алфавита
    alphabet = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]
    matrix = []
    used_chars = set()

    # Удаление пробелов и приведение к верхнему регистру для ключа
    key = key.replace(" ", "").upper()

    # Добавление символов ключа в матрицу
    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Добавление оставшихся символов алфавита в матрицу
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Разделение списка символов на 4 строки по 8 символов
    return [matrix[i * 8:(i + 1) * 8] for i in range(4)]


# Подготавливает текст для шифрования
def preprocess_text(text: str) -> str:
    # Замена символов Й на И и Ё на Е
    text = text.replace("Й", "И").replace("Ё", "Е")
    text = text.upper().replace(" ", "")
    processed = ""
    i = 0
    while i < len(text):
        # Если встречаются две буквы "Я" подряд, вставляем между ними "А"
        if i + 1 < len(text) and text[i] == text[i + 1] == "Я":
            processed += text[i] + "А"
            i += 1
        # Если встречаются две одинаковые буквы подряд, вставляем между ними "Я"
        elif i + 1 < len(text) and text[i] == text[i + 1]:
            processed += text[i] + "Я"
            i += 1
        else:
            processed += text[i]
            i += 1

    # Если длина текста нечетная, добавляем "Я" или "А" в конец, чтобы не образовывались две одинаковые буквы подряд
    if len(processed) % 2 != 0:
        if processed[-1] == 'Я':
            processed += 'А'
        else:
            processed += 'Я'

    return processed


# Находит позицию символа в матрице.
def find_position(matrix: list, char: str) -> tuple:
    # Нахождение позиции символа в матрице
    for i, row in enumerate(matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j
    return None


# Шифрует текст по алгоритму Плейфера.
def playfair_encrypt(plaintext: str, key: str) -> str:
    # Создание матрицы Плейфера на основе ключа
    matrix = create_playfair_square(key)
    # Предобработка текста
    plaintext = preprocess_text(plaintext)
    ciphertext = ""

    # Шифрование текста
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Если символы в одной строке
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 8] + matrix[row2][(col2 + 1) % 8]
        # Если символы в одном столбце
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 4][col1] + matrix[(row2 + 1) % 4][col2]
        # Если символы образуют прямоугольник
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


# Расшифровывает текст по алгоритму Плейфера.
def playfair_decrypt(ciphertext, key):
    # Создание матрицы Плейфера на основе ключа
    ciphertext = ciphertext.upper().replace(" ", "")
    matrix = create_playfair_square(key)
    plaintext = ""

    # Расшифрование текста
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Если символы в одной строке
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 8] + matrix[row2][(col2 - 1) % 8]
        # Если символы в одном столбце
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 4][col1] + matrix[(row2 - 1) % 4][col2]
        # Если символы образуют прямоугольник
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext


if __name__ == "__main__":
    # Задание 1
    print("ЗАДАНИЕ 1")
    print("Преобразованный открытый текст: " + preprocess_text("Алгоритм шифрования известен всем"))
    print("Преобразованный ключ: ")
    # Вывод матрицы для проверки
    for row in create_playfair_square("принципы"):
        print(" ".join(row))
    print(playfair_encrypt("Алгоритм шифрования известен всем", "принципы") + '\n')

    # Задание 2
    print("ЗАДАНИЕ 2")
    print("Преобразованный ключ: ")
    # Вывод матрицы для проверки
    for row in create_playfair_square("криптостойкость"):
        print(" ".join(row))
    print(playfair_decrypt("рьрпа юомтш лвучгбыс тсмратблнуюг", "криптостойкость") + '\n')

    # Задание 3
    print("ЗАДАНИЕ 3")
    print("Преобразованный открытый текст: " + preprocess_text("Тимошенко Антон Дмитриевич"))
    print("Преобразованный ключ: ")
    # Вывод матрицы для проверки
    for row in create_playfair_square("хочет домой"):
        print(" ".join(row))
    print(playfair_encrypt("Тимошенко Антон Дмитриевич", "хочет домой") + '\n')

    # Задание 4
    print("ЗАДАНИЕ 4")
    print("Преобразованный открытый текст: " + preprocess_text("Нужно истлеть чтобы переродиться"))
    print("Преобразованный ключ: ")
    # Вывод матрицы для проверки
    for row in create_playfair_square("перерождение"):
        print(" ".join(row))
    print(playfair_encrypt("Нужно истлеть чтобы переродиться", "перерождение") + '\n')
