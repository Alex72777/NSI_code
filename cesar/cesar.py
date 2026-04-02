
def cesar(cle: int, contenu: str, min_ord: int = 32, max_ord: int = 1114111) -> str:
    message = ""
    for char in contenu:
        index = ord(char) + cle
        if index > max_ord:
            index -= 26
        elif index < min_ord:
            index += 26
        
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

def brute_force(msg: str) -> None:
    min_ord = 97
    max_ord = 122
    
    for i in range(min_ord + 1, max_ord + 1):
        attempt = cesar(i - min_ord, msg)
        print("Décalage %2d: %s" % (i - min_ord, attempt))
    

def analyse_frequentielle(msg: str) -> None:
    frequency = {}
    for i in range(97, 123):
        frequency[chr(i)] = 0
    
    for char in msg:
        frequency[char] = msg.count(char)
    print(frequency)
    print(sum(frequency.values()))

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
    #brute_force("erqmrxu")
    #analyse_frequentielle(open("loremipsum.txt", "r", encoding="utf-8").read())*
    #crypte = vigenere("clef", "bienvenue")
    #print(crypte)
    print(vigenere("clef", "21w285mz21mpur5mnzvm78mr6m75r6m6az3nmwnvzrmyr6myn6nt1r6mr7mwrmqr7r67rmyr6mr7n76m81v6mqnzr5v48rm1vxmv65nrymn16m81mp5a3726a67rzrmn6az75v48rm28mp5a3726a67rzrmnmpyr6m38oyv48r6myr6mpyr6mr v67r17m3n5m3nv5rmyrm7r5zrmqrmovpyr6mr67mtr1r5nyrzr17mrz3y2arm81rmpyrm38oyv48rm3285mpuvss5rzr17m81rmpyrm6rp5r7rm35v9rm3285mqrpuvss5rzr17", True))

if __name__ == "__main__":
    main()