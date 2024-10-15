# Вычисляет НОД двух чисел
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Проверяет числа на взаимную простоту
def are_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


# Вычисляет обратное к a по модулю m
def mod_inverse(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


# Афинное шифрование
def athenian_encryption(alphabet: list, m: int, a: int, b: int, message: str) -> str:
    alphabet_dict = {char: i for i, char in enumerate(alphabet)}
    reverse_alphabet_dict = {i: char for char, i in alphabet_dict.items()}
    encrypted_message = ""

    for char in message:
        if char in alphabet_dict:
            encrypted_index = (a * alphabet_dict[char] + b) % m
            encrypted_message += reverse_alphabet_dict[encrypted_index]
        else:
            encrypted_message += char

    return encrypted_message


# Функция дешифровки афинного шифра
def athenian_decryption(alphabet: list, m: int, a: int, b: int, encrypted_message: str) -> str:
    alphabet_dict = {char: i for i, char in enumerate(alphabet)}
    reverse_alphabet_dict = {i: char for char, i in alphabet_dict.items()}
    decrypted_message = ""

    a_inv = mod_inverse(a, m)  # Находим обратное к a по модулю m

    for char in encrypted_message:
        if char in alphabet_dict:
            decrypted_index = (a_inv * (alphabet_dict[char] - b)) % m
            decrypted_message += reverse_alphabet_dict[decrypted_index]
        else:
            decrypted_message += char

    return decrypted_message


def get_valid_input(prompt: str, validation_func=None) -> str:
    while True:
        try:
            value = input(prompt)
            if validation_func and not validation_func(value):
                raise ValueError
            return value
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    rus_alphabet = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]
    rus_alphabet.insert(rus_alphabet.index('Е') + 1, 'Ё')
    eng_alphabet = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]

    def is_coprime_with_alphabet(a):
        return are_coprime(a, len(rus_alphabet))

    for alphabet, language in [(rus_alphabet, "русском"), (eng_alphabet, "английском")]:
        message = get_valid_input(f"Введите предложение на {language}: ").upper()
        encrypted_message = "юнйьуд нсуд"
        a = int(get_valid_input("Введите а: ", lambda x: are_coprime(int(x), len(alphabet))))
        b = int(get_valid_input("Введите b: ", lambda x: x.isdigit()))
        print(f"\nЗашифрованное сообщение: {athenian_encryption(alphabet, len(alphabet), a, b, message)}")
        print(f"\nДешифрованное сообщение: {athenian_decryption(alphabet, len(alphabet), a, b, encrypted_message.upper())}")
