def shift_alphabet(alphabet: list, shift: int, reverse: bool = False) -> list:
    alphabet_length = len(alphabet)

    # Проверяем длину алфавита, чтобы избежать деления на ноль
    if alphabet_length == 0:
        raise ValueError("Алфавит не может быть пустым.")

    shift = shift % alphabet_length
    if reverse:
        shift = -shift

    return alphabet[shift:] + alphabet[:shift]


# Шифрование методом Цезаря
# args: алфавит, строка, сдвиг, прямой или обратный сдвиг
def caesar_cipher(alphabet: list, message: str, shift: int, reverse: bool = False) -> str:
    # Проверяем, что сообщение не пустое
    if not message:
        raise ValueError("Сообщение не может быть пустым.")

    shifted_alphabet = shift_alphabet(alphabet, shift, reverse)
    print(shifted_alphabet)

    encrypted_message = ""
    for char in message:
        if char.upper() in alphabet:
            index = alphabet.index(char.upper())
            encrypted_char = shifted_alphabet[index]
            encrypted_message += encrypted_char.lower() if char.islower() else encrypted_char
        else:
            encrypted_message += char

    return encrypted_message


# Функция проверки корректного ввода
def get_valid_input(prompt: str, type_func: type, error_message: str) -> str:
    while True:
        user_input = input(prompt).strip()
        try:
            return type_func(user_input)
        except ValueError:
            print(error_message)


if __name__ == "__main__":
    alphabet = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]
    print(alphabet)

    while True:
        message = get_valid_input("Введите ФИО: ", str, "ФИО не может быть пустым.")
        if message:
            break
        else:
            print("ФИО не может быть пустым или состоять только из пробелов.")

    shift = int(get_valid_input("Введите сдвиг: ", int, "Сдвиг должен быть целым числом."))

    print("\nШифр Цезаря")
    print("Сдвиг по часовой стрелке: " + caesar_cipher(alphabet, message, shift))
    print("Сдвиг против часовой стрелки: " + caesar_cipher(alphabet, message, shift, True))