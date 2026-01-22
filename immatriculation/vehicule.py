from random import randint

class Vehicule():
  type_vehicules = {
    "voiture": {
      "roue": 4,
      "moteur": 1,
      "passager": 5,
      "immat": "01-",
    },
    "camion": {
      "roue": 12,
      "moteur": 1,
      "passager": 2,
      "immat": "02-",
    },
    "velo": {
      "roue": 2,
      "moteur": 0,
      "passager": 1,
      "immat": "03-",
    },
    "avion": {
      "roue": 12,
      "moteur": 2,
      "passager": 260,
      "immat": "04-",
    },
    "moto": {
      "roue": 2,
      "moteur": 1,
      "passager": 2,
      "immat": "05-",
    }
  }

  def __init__(self, type: str) -> None:
    if type in self.type_vehicules:
      self.type = type
    else:
      self.type = "voiture"

    for key, val in self.type_vehicules[self.type].items():
      setattr(self, key, val)

    self.immat = self.type_vehicules[self.type]['immat'] + f"{randint(0,999):03d}"

  def __repr__(self) -> str:
    return f"{self.immat} - {self.type.capitalize()}"

if __name__ == "__main__":
  liste_vehc = []
  liste_vehc.append(Vehicule('voiture'))
  liste_vehc.append(Vehicule('camion'))
  liste_vehc.append(Vehicule('moto'))
  liste_vehc.append(Vehicule('velo'))
  liste_vehc.append(Vehicule('avion'))
  [print(vehc) for vehc in liste_vehc]