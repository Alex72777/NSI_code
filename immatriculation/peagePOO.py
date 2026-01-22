from vehicule import Vehicule
from random import choice

class Peage():
  """
  Représentation sous forme de classe d'un péage.
  """
  def __init__(self) -> None:
    self.file_attente: list[Vehicule] = []

  def enfiler(self, obj: object) -> None:
    """
    Ajoute un véhicule (object) à la file.
    """
    self.file_attente.append(obj)

  def defiler(self) -> object:
    """
    Défile la file d'attente
    """
    if len(self.file_attente) == 0:
      raise RuntimeError("File d'attente vide.")
    return self.file_attente.pop(0)

  def vider(self) -> None:
    self.file_attente.clear()

  @property
  def est_vide(self) -> bool:
    if len(self.file_attente) > 0:
      return False
    else:
      return True

  @property
  def longueur(self) -> int:
    return len(self.file_attente)

  def __repr__(self) -> str:
    return "\n".join([f"{i + 1}: {self.file_attente[i]}" for i in range(self.longueur)])

peage = Peage()
[peage.enfiler(Vehicule(choice(list(Vehicule.type_vehicules.keys())))) for i in range(10)]
[peage.defiler() for i in range(3)]

print(peage)

peage.vider()

print(peage)
print("File d'attente vide:", peage.est_vide)