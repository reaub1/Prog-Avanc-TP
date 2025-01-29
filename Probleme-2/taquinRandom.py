import random

TROU  =  '0'
nbcomb=0
dim = 0

def afficheJeu(jeu) :
	for l in jeu :
		for c in l :
			print(c, end=' ')
		print()
	print()

def initTaquin(nf) :
	f = open(nf,"r")
	lignes = f.readlines()
	jeu, ref = [], []
	global dim 
	dim = len(lignes)//2
	print(dim)
	for l in lignes[:dim] :
		c = l.split()
		jeu.append(c[:])
	for l in lignes[dim:] :
		c = l.split()
		ref.append(c[:])
	return jeu, ref

def chercher(val, ref) :
	for i in range(len(ref)) :
		if val in ref[i] : return i, ref[i].index(val)		

def valJeu( jeu,  ref) :
	sommedist=0
	for i in range(len(jeu)) :
		for j in range(len(jeu[i])) :
			if (jeu[i][j] != ref[i][j]) :
				y, x  = chercher(jeu[i][j], ref)
				sommedist += abs(y-i) + abs(x-j)
	return sommedist

def meilleureConfig(lstJeu, ref) : 
	return lstJeu[0]

def pasDansListe(jeu, lstJeu) :
	for j in lstJeu :
		if valJeu(j[0], jeu) == 0 : return 0
	return 1

def copie_jeu(j) :
	jeu=[]
	for i in range(len(j)) :
		jeu.append(j[i][:])
	return jeu

def jouer(ref, jeu) :
	nbEssais = 0
	global dim
	fin = False
	while not fin :
		if nbEssais%10000 == 0 : print(nbEssais, end=" ")
		dist = valJeu(jeu, ref)
		#print(dist, end=' ')
		if (dist == 0) :
			print()
			print("nombre de mouvements :", nbEssais)
			afficheJeu(jeu)
			exit (0)
		
		# chercher la position du trou 
		mt, nt = chercher(TROU, jeu)
		# on joue au hasard parmi toutes les possibilités d'action, sans tester si on revient en arrière ...

		coup = random.randint(0,3)
		if (mt > 0) and (coup==0)   :
			nbEssais+=1
			# on echange le trou et l'élément au dessus 
			(jeu[mt][nt], jeu[mt-1][nt]) = (jeu[mt-1][nt], jeu[mt][nt])
		if (mt < dim-1) and (coup==1) :
			nbEssais+=1
			# on echange le trou et l'élément au dessus 
			(jeu[mt][nt], jeu[mt+1][nt]) = (jeu[mt+1][nt], jeu[mt][nt])
		if (nt > 0) and (coup==2) :
			nbEssais+=1
			# on echange le trou et l'élément au dessus 
			(jeu[mt][nt], jeu[mt][nt-1]) = (jeu[mt][nt-1], jeu[mt][nt])		
		if (nt < dim-1) and (coup==3) :
			nbEssais+=1
			# on echange le trou et l'élément au dessus 
			(jeu[mt][nt], jeu[mt][nt+1]) = (jeu[mt][nt+1], jeu[mt][nt])		

jeu, ref = initTaquin("taquin4.txt")
afficheJeu(jeu)
afficheJeu(ref)

jouer(ref, jeu)