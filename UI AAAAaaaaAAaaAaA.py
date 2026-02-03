from tkinter import Canvas, Button, Tk
from random import randint

app = Tk()
tab = []

for i in range(5):
	tab.append([])
	for j in range(5):
		button = Button(app, text=f"{i + 1}{j + 1}")
		button.grid(row=i, column=j)
		tab[i].append(button)

# tab[randint(0, 4)][randint(0, 4)]["background"] = "red"
tab[0][2]["background"] = "black"
tab[1][2]["background"] = "blue"
tab[2][2]["background"] = "blue"
tab[3][2]["background"] = "blue"
tab[4][1]["background"] = "blue"
tab[4][3]["background"] = "blue"
tab[1][1]["background"] = "red"
tab[1][3]["background"] = "red"
tab[2][0]["background"] = "red"
tab[2][4]["background"] = "red"

tab[0][0]["command"] = lambda: print("Augh")

canva = Canvas(app, width=150, height=150, background="beige")
canva.create_line(20, 120, 130, 120)
canva.create_line(40, 100, 110, 100)
canva.create_line(20, 120, 20, 80)
canva.create_line(130, 120, 130, 80)
canva.create_line(40, 80, 40, 100)
canva.create_line(110, 80, 110, 100)
canva.create_line(20, 80, 40, 80)
canva.create_line(110, 80, 130, 80)

canva.create_line(35, 25, 70, 25)
canva.create_line(35, 45, 70, 45)
canva.create_line(35, 45, 35, 25)
canva.create_line(70, 25, 70, 45)
canva.create_line(55, 45, 55, 25)

canva.create_line(115, 25, 80, 25)
canva.create_line(115, 45, 80, 45)
canva.create_line(115, 45, 115, 25)
canva.create_line(80, 25, 80, 45)
canva.create_line(95, 45, 95, 25)

canva.create_rectangle(10, 10, 140, 135)
canva.create_arc(10, 15, 140, 1)
canva.create_arc(140, 1, 15, 15)

canva.grid(row=1, column = 6)

app.mainloop()
