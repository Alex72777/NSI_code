#coding : UTF8
alpha="abcdefghijklmnopqrstuvwxyz1234567890 "
def code_cesar(texte,cle,alpha):
	msg_code=""
	for c  in texte:
		for j in range(len(alpha)):
			if c==alpha[j]:
				#print(c,j,alpha[j],cle)
				msg_code+=alpha[int(j+int(cle))%len(alpha)]
				#modulo 36 car a→z puis 0→9 pour reveinr au debut
		#print(msg_code[-1])
	return(msg_code)
	
def code_vigenere(texte,code,alpha):
	ind=0
	txt_conv=""
	for c in texte:
		cle=code[ind%len(alpha)]
		#print(c,cle)
		txt_conv += code_cesar(c,cle,alpha)
	return txt_conv

msg="21w285mz21mpur5mnzvm78mr6m75r6m6az3nmwnvzrmyr6myn6nt1r6mr7mwrmqr7r67rmyr6mr7n76m81v6mqnzr5v48rm1vxmv65nrymn16m81mp5a3726a67rzrmn6az75v48rm28mp5a3726a67rzrmnmpyr6m38oyv48r6myr6mpyr6mr v67r17m3n5m3nv5rmyrm7r5zrmqrmovpyr6mr67mtr1r5nyrzr17mrz3y2arm81rmpyrm38oyv48rm3285mpuvss5rzr17m81rmpyrm6rp5r7rm35v9rm3285mqrpuvss5rzr17"
cle=[-13, -1, -20, -8, -5, -13, -1, -20, -9, -17, -21, -5, -19]
print(code_vigenere(msg,cle,alpha))