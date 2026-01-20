class Peage():
  """
  Représentation sous forme de classe d'un péage.
  """
  def __init__(self) -> None:
    self.file_attente = []

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