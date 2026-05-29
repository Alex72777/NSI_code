
def cesar(cle: int, contenu: str, alpha: str) -> str:
    message = ""
    for char in message:
        index = (alpha.index(char) + cle ) % len(alpha)
        message += alpha[index]
    return message

def crypter() -> None:
    message = '123~- Je suis vivant !!!! -~456'
    cle = input('Clé?')
    if not cle.isdigit():
        cle = '3'
    cle = int(cle) % 255
    print('Clé choisie: %d' % cle)
    
    recu = cesar(cle, message ,"")
    print('message: %s' % message)
    print('message crypté: %s' % recu)
    message_decrypte = cesar(-cle, recu, "")
    print('message décrypté: %s' % message_decrypte)
    
    assert cesar(3, 'bonjour', "") == "erqmrxu"
    assert cesar(3, 'b', "") == 'e'

def lire_et_decrypter() -> None:
    with open('secret_crypte.txt', 'r', encoding="utf-8") as file:
        for line in file.readlines():
            print(cesar(-3, line, ""))
        file.close()

def brute_force(msg: str, alpha: str) -> None:
    for i in range(1, len(alpha) + 1):
        attempt = cesar(i, msg, alpha)
        print("Décalage %2d: %s" % (i, attempt))
    

def analyse_frequentielle(msg: str, alpha: str) -> None:
    frequency = {}
    for char in alpha:
        frequency[char] = 0
    
    for char in msg:
        frequency[char] = msg.count(char)
    print(frequency)

def vigenere(cle: str, msg: str, negate: bool = False) -> str:
    min_ord = 97
    
    crypte = ""
    for i in range(len(msg)):
        decalage = ord(cle[i % len(cle)]) - min_ord + 1
        if negate:
            decalage *= -1
        # print(decalage)
        crypte += chr(ord(msg[i]) + decalage)
    #print(crypte)
    return crypte

def main() -> None:
    # crypter()
    #lire_et_decrypter()
    brute_force("erqmrxu")
    #analyse_frequentielle(open("loremipsum.txt", "r", encoding="utf-8").read())*
    crypte = vigenere("clef", "bienvenue")
    print(crypte)
    print(vigenere("clef", crypte, True))

if __name__ == "__main__":
    main()