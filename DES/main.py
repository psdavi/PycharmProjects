

from Crypto.Cipher import DES

chave = '12345671'

def pad(texto):
    while len(texto) % 8 != 0:
        texto += ' '
    return texto

des = DES.new(chave, DES.MODE_ECB)
texto_exemplo = "Sistemas Distribuidos Melhor Disciplina"
padded_text = pad(texto_exemplo)
texto_criptografado = des.encrypt(padded_text)

print()
print("------------------------------------ TEXTO CRIPTOGRAFADO ----------------------------------------------")
print()
print(texto_criptografado)


print()
print("------------------------------------ TEXTO DESCRIPTOGRAFADO -------------------------------------------")
print()
print(des.decrypt(texto_criptografado))

print()
print("-------------------------------------------------------------------------------------------------------")





