from random import randint
from time import time

def LancerDes(faces, tirages):
  print("{} tirages avec un dé equilibré de {} faces".format(tirages, faces))

  result = []
  for i in range(tirages):
    result.append(randint(1, faces))
    print("Tirage n°{}: {}".format(i+1, result[i]))

  return result

init = time()
faces = 8
TirageDes = LancerDes(faces, 100)
occurences = {}

print("Somme: {} Moyenne: {}".format(sum(TirageDes), sum(TirageDes)/len(TirageDes)))
print("Temps d'éxécution: {} secondes".format(time()-init))
print("Occurences par faces:")
for i in range(1, faces+1):
  print(" - {}: {} occurences".format(i, TirageDes.count(i)))

print(occurences)
