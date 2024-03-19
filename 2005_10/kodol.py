# https://www.oktatas.hu/bin/content/dload/erettsegi/feladatok2005osz/emelt/e_info_05okt_fl.pdf


print("\n1. feladat\n")

# text = "Ez a próba szöveg, amit kódolunk!"
text = input("Adjon meg egy legfeljebb 255 karakterből álló szöveget: ")


print("\n2. feladat\n")

text = text.upper()

hu_char = ['Á', 'É', 'Í', 'Ó', 'Ö', 'Ő', 'Ú', 'Ü', 'Ű', '.', ',', '!', ' ']
en_char = ['A', 'E', 'I', 'O', 'O', 'O', 'U', 'U', 'U', '', '', '', '']

for old, new in zip(hu_char, en_char):
    text = text.replace(old, new)


print("\n3. feladat\n")

print(text)


print("\n4. feladat\n")

# enc_key = auto
enc_key = input('Kérem, adja meg a kulcsszót, ami legfeljebb 5 karakterből állhat: ')
enc_key = enc_key.upper()


print("\n5. feladat\n")

cnt = len(text) // len(enc_key) + 1
enc_key = cnt * enc_key
enc_key = enc_key[:len(text)]
print(enc_key)
print(text)


print("\n6. feladat\n")

vigenere = {}
with open('Vtabla.dat', 'r') as f:
    for row in f:
        start_char = row[0]
        row = row.strip()
        if start_char == 'A':
            vigenere['abc'] = row
        if start_char in enc_key:
            vigenere[start_char] = row

enc_text = ''
for c, k in zip(text, enc_key):
    col = vigenere['abc'].index(c)
    enc_text += vigenere[k][col]


print("\n7. feladat\n")

# print(text)
# print(enc_key)
print(enc_text)

with open('kodolt.dat', 'w') as f:
    f.writelines(enc_text)
