# Шифрование квадратом Полибия
# args: шифруемое сообщение
def polybius_square(message: str) -> str:
    alphabet = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]
    alphabet.insert(alphabet.index('Е') + 1, 'Ё')

    alphabet_dict = {char: f"{(i // 6) + 1}{(i % 6) + 1}" for i, char in enumerate(alphabet)}

    encrypted_message = ""
    for char in message:
        if char in alphabet_dict:
            encrypted_message += alphabet_dict[char]
        else:
            encrypted_message += char

    return encrypted_message


if __name__ == "__main__":
    message = input("Введите ФИО: ")

    # Квадрат Полибия
    print("\nКвадрат Полибия")
    print("Зашифрованное сообщение " + polybius_square(message.upper()))
