#from sys import set_int_max_str_digits
#from time import perf_counter
#set_int_max_str_digits(9999999)

def fibr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n - 1) + fibr(n - 2)

def fib(n, liste):
    if n < 0: raise ValueError("n < 0 !!!")
    liste += [liste[-1] + liste[-2]]
    return liste

"""'b = perf_counter()
temps = []
liste = [0, 1]
for i in range(0, 200):
    liste = fib(i, liste)
    #print(f"{i} : {temps[-1]}")
#print(liste[-1])
print(perf_counter() - b)"""
        
        
#n = input("n?")
#print(fibr(45)[-1])
#print(time())

def tour_complete(tour, nbre_disques):
    if not len(tour) == nbre_disques: return False
    for i in range(len(tour) - 2):
        if tour[i] < tour[i + 1]: return False
    return True

def peut_deplacer(tour_depart, tour_arrive) -> bool:
    if tour_depart and not tour_arrive:
        return True
    if tour_depart and tour_arrive and tour_depart[-1] < tour_arrive[-1]:
        return True
    return False

def deplacer(tours, deplacer_vers) -> list:
    if not peut_deplacer(tours[int(deplacer_vers[0]) - 1], tours[int(deplacer_vers[1]) - 1]):
        return tours
    tours[int(deplacer_vers[1]) - 1].append(tours[int(deplacer_vers[0]) - 1].pop())
    return tours

def valid_input(chars: str) -> bool:
    if not len(chars) == 2 or not chars.isdigit():
        return False
    if int(chars[0]) in range(1, 4) and int(chars[1]) in range(1, 4):
        return True
    return False

def get_input() -> str:
    deplacer_vers = input(">> ")
    while not valid_input(deplacer_vers):
        deplacer_vers = input(">> ")
    return deplacer_vers

def hanoi_deplacement(nbre_disques):
    tours = [[], [], []]
    for i in range(nbre_disques , 0, -1):
        tours[0].append(i)
    
    deplacements = 0
    while not tour_complete(tours[2], nbre_disques):
        print(tours)
        deplacer_vers = get_input()
        
        tours = deplacer(tours, deplacer_vers)
        deplacements += 1

# ~ hanoi_deplacement(4)

def hanoi_auto(nbre_disques):
	tours = [[], [], []]
	for i in range(nbre_disques , 0, -1):
		tours[0].append(i)

	while not tour_complete(tours[2], nbre_disques):
		index = 0
		for i in range(-3, 0, 1):
			if (tours[i] and not tours[i + 1]) or (tours[i] and tours[i + 1] and tours[i][-1] < tours[i + 1][-1]):
				index = i
				break
		
		element = tours[index].pop()
		if index <= 1:
			tours[index + 1].append(element)
		else:
			tours[0].append(element)
		print("plus petit déplacé", index)
		
		for i in range(-3, 0, 1):
			if not tours[i]: continue
			
			if tours[i + 1] and tours[i][-1] < tours[i + 1][-1]:
				tours[i + 1].append(tours[i].pop())
				break
			elif i != -3 and tours[i - 1] and tours[i][-1] < tours[i - 1][-1]:
				tours[i - 1].append(tours[i].pop())
				break
			elif not tours[i + 1]:
				tours[i + 1].append(tours[i].pop())
				break
			
			# ~ if i != -3 and tours[i - 1] and tours[i][-1] < tours[i - 1][-1]:
				# ~ tours[i - 1].append(tours[i].pop())
				# ~ break
			# ~ else:
				# ~ tours[-1].append(tours[i].pop())
				# ~ break
		print(tours)

hanoi_auto(4)

#print(hanoi(3))
