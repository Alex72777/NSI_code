
def cesar(cle: int, contenu: str) -> str:
    message = ""
    for char in contenu:
        index = ord(char) + cle
#         if index > 90:
#             index -= 26
#         elif index < 65:
#             index += 26
        
        message += chr(index)
    return message

def crypter() -> None:
    message = '123~- Je suis vivant !!!! -~456'
    cle = input('Clé?')
    if not cle.isdigit():
        cle = '3'
    cle = int(cle) % 255
    print('Clé choisie: %d' % cle)
    
    recu = cesar(cle, message)
    print('message: %s' % message)
    print('message crypté: %s' % recu)
    message_decrypte = cesar(-cle, recu)
    print('message décrypté: %s' % message_decrypte)
    
    assert cesar(3, 'bonjour') == "erqmrxu"
    assert cesar(3, 'b') == 'e'

def lire_et_decrypter() -> None:
    with open('secret_crypte.txt', 'r', encoding="utf-8") as file:
        for line in file.readlines():
            print(cesar(-3, line))
        file.close()

def main() -> None:
    # crypter()
    lire_et_decrypter()

if __name__ == "__main__":
    main()