def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('а')
            encrypted_char = chr(((ord(char.lower()) - ord('а') + shift) % 32) + ord('а'))
            encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_decrypt(cipher_text, key):
    decrypted_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('а')
            decrypted_char = chr(((ord(char.lower()) - ord('а') - shift + 32) % 32) + ord('а'))
            decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text


# Задание 1
plain_text_1 = "Уязвимость симметричного шифрования в передаче ключа"
key_1 = "угроза"
cipher_text_1 = vigenere_encrypt(plain_text_1, key_1)
print("Задание 1:")
print("Зашифрованный текст:", cipher_text_1)

# Задание 2
cipher_text_2 = "щныюэвсъцц аайт пх апяюьтаю пжмяюеитыщс жптыцуеюгцсэшоушач"
key_2 = "безопасность"
decrypted_text_2 = vigenere_decrypt(cipher_text_2, key_2)
print("\nЗадание 2:")
print("Расшифрованный текст:", decrypted_text_2)

# Задание 3
print("\nЗадание 3:")
plain_text_3 = input("Введите своё ФИО: ")
key_3 = "студент"
cipher_text_3 = vigenere_encrypt(plain_text_3, key_3)
print("Зашифрованный текст:", cipher_text_3)

# Задание 4
plain_text_4 = "Ты перепутал небо со звёздами, отражёнными ночью в поверхности пруда"
key_4 = "ведьмак"
cipher_text_4 = vigenere_encrypt(plain_text_4, key_4)
print("\nЗадание 4:")
print("Зашифрованный текст:", cipher_text_4)
