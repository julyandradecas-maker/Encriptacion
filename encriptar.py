import random
def cipher(texto, key):
    return ''.join(chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(texto))

mensaje = input("Texto: ")
llave = [random.randint(0, 1) for _ in range(len(mensaje))]

cifrado = cipher(mensaje, llave)
descifrado = cipher(cifrado, llave)

print(f"Llave:      {llave}")
print(f"Cifrado:    {''.join(f'{ord(c):08b}' for c in cifrado)}")
print(f"Descifrado: {descifrado}")

