from random import randint

player = {
  "health": 100,
  "maxhealth": 100,
  "shield": 100,
  "mainhand": None,
  "lefthand": None,
  "inventory": [],
  "wins": 0
}

ennemy = {
  "health": 95,
  "maxhealth": 100,
  "shield": 100,
  "mainhand": None,
  "lefthand": None,
  "inventory": [],
  "wins": 0
}

def battle():
  while player["health"] > 0 and ennemy["health"] > 0:
    player["health"] -= 10 - randint(0, 3)
    ennemy["health"] -= 10 - randint(0, 3)
    #print("PV du joueur: {}/100".format(player["health"]))
    #print("PV du bozo: {}/100".format(ennemy["health"]))

  #print("Battle ended, winner is {}".format("Player" if ennemy["health"] <= 0 else "Ennemy"))

  if player["health"] <= 0:
    ennemy["wins"] += 1
  else:
    player["wins"] += 1

rounds = 100
healthDif = 5

for health in range(-healthDif, healthDif+1, 1):
  
  for i in range(rounds):
    battle()
    player["health"] = player["maxhealth"]
    ennemy["health"] = ennemy["maxhealth"] + health

  plWins = player["wins"]
  enWins = ennemy["wins"]
  print("Pour {} tours avec une différence de {} PV(Adversaire)".format(rounds, health))
  print("Ratio (Player/Ennemy) {}:{}".format(plWins, enWins))

  plWins = player["wins"] = 0
  enWins = ennemy["wins"] = 0
