word = input("Ingrese una palabra: ")
word = word.lower()
word = ''.join(filter(str.isalnum, word))

if word == word[::-1]:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
