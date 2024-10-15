# Вывод таблицы Трисемуса
def print_trisemus_table(trisemus_table: list[list[str]]) -> None:
    for line in trisemus_table:
        print(" ".join(line))


# Создание таблицы Трисемуса
def create_trisemus_table(alphabet: list) -> list[list[str]]:
    trisemus_table = [alphabet]
    for i in range(1, len(alphabet)):
        last_line = trisemus_table[-1]
        shifted_line = last_line[1:] + last_line[:1]
        trisemus_table.append(shifted_line)

    return trisemus_table


# Шифрование по таблице Трисемуса
def trisemus_encryption(trisemus_table: list[list[str]], message: str) -> str:
    encrypted_message = ''
    non_alphabet_count = 0
    for i, char in enumerate(message.upper()):
        row = trisemus_table[(i - non_alphabet_count) % len(trisemus_table)]
        if char in row:
            char_index = row.index(char)
            encrypted_message += row[(char_index + i) % len(row)]
        else:
            encrypted_message += char
            non_alphabet_count += 1

    return encrypted_message


# Дешифрование по таблице Трисемуса
def trisemus_decryption(trisemus_table: list[list[str]], message: str) -> str:
    decrypted_message = ''
    for i, char in enumerate(message.upper()):
        row = trisemus_table[i % len(trisemus_table)]
        if char in row:
            char_index = row.index(char)
            decrypted_message += row[(char_index - i) % len(row)]
        else:
            decrypted_message += char

    return decrypted_message


if __name__ == "__main__":
    # Русский алфавит
    rus_alphabet = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]

    # Создание таблицы Трисемуса
    trisemus_table = create_trisemus_table(rus_alphabet)

    print_trisemus_table(trisemus_table)

    # Примеры работоспособности программы
    message1 = "Защищённость системы зависит от применяемых средств"
    encrypted_message1 = trisemus_encryption(trisemus_table, message1)
    print(f"Исходное сообщение: {message1}\nЗашифрованное сообщение: {encrypted_message1}\n")

    encrypted_message2 = "Вбйг"
    decrypted_message2 = trisemus_decryption(trisemus_table, encrypted_message2)
    print(f"Зашифрованное сообщение: {encrypted_message2}\nРасшифрованное сообщение: {decrypted_message2}\n")

    message3 = "Тимошенко Антон Дмитриевич"
    encrypted_message3 = trisemus_encryption(trisemus_table, message3)
    print(f"Исходное сообщение: {message3}\nЗашифрованное сообщение: {encrypted_message3}\n")

    message4 = "Ты перепутал небо со звёздами, отражёнными ночью в поверхности пруда"
    encrypted_message4 = trisemus_encryption(trisemus_table, message4)
    print(f"Исходное сообщение: {message4}\nЗашифрованное сообщение: {encrypted_message4}\n")
