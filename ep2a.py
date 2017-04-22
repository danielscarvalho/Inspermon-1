import time
import random
Insperdex=dict()
Insperdex={"Pikachu":{"poder":20,"vida":100,"defesa":7,"xpatual":0,"xpevolucao":1,"xp2":25},	
		   "Bulbasaur":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Squirtle":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Charmander":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Ivysaur":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Wartortle":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Charmeleon":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevolucao":1,"xp2":20},
		   "Venusaur":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevolucao":1,"xp2":30},
		   "Blastoise":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevolucao":1,"xp2":30},
		   "Charizard":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevolucao":1,"xp2":30},
		   "Abra":{"poder":20,"vida":80,"defesa":5,"xpatual":0,"xpevolucao":1,"xp2":15},
		   "Tentacool":{"poder":15,"vida":60,"defesa":5,"xpatual":0,"xpevolucao":1,"xp2":10},
		   "Geodude":{"poder":20,"vida":70,"defesa":6,"xpatual":0,"xpevolucao":1,"xp2":15},
		   "Onix":{"poder":15,"vida":80,"defesa":9,"xpatual":0,"xpevolucao":1,"xp2":25},
		   "Horsea":{"poder":15,"vida":60,"defesa":5,"xpatual":0,"xpevolucao":1,"xp2":15},
		   "Zubat":{"poder":15,"vida":50,"defesa":5,"xpatual":0,"xpevolucao":1,"xp2":10}}
		   
Computador=[]

probbilidadefuga1 = [0,1,2,3,4,5,6,7,8,9,10]

#FUNÇÃO RETORNA UM NÚMERO ALEATÓRIO NUMA DISTRIBUIÇÃO NORMAL CENTRADA EM NUM
def distnormal(num):
		lisnum=[1.5,
				1.4,1.4,
				1.3,1.3,1.3,
				1.2,1.2,1.2,1.2,
				1.1,1.1,1.1,1.1,1.1,
				1.0,1.0,1.0,1.0,1.0,1.0,
				0.9,0.9,0.9,0.9,0.9,
				0.8,0.8,0.8,0.8,
				0.7,0.7,0.7,
				0.6,0.6,
				0.5]
		return(int(num*random.choice(list(lisnum))))

#FUNÇÃO DE ATAQUE
def ataca(atacante,defensor):
	ataque = distnormal(Insperdex[atacante]["poder"])
	defesa = distnormal(Insperdex[defensor]["defesa"])
	if ataque > defesa:
			Insperdex[defensor]["vida"]=Insperdex[defensor]["vida"]-((ataque-defesa))
			if Insperdex[defensor]["vida"] < 0:
				Insperdex[defensor]["vida"] = 0	

def evolve(inspermon):
	if 



#MAIN CODE		   
print("Bem vindo ao Inspermon")
time.sleep(0.5)

print("Carregando o jogo...") 
time.sleep(1.5)

#ESCOLHA DE INSPERMON
while True:
	usuario=str(input("Escolha seu Inspermon: Bulbasaur(1), Charmander(2), Squirtle(3):"))
	if usuario == "1":
		usuario = "Bulbasaur"
	if usuario == "2":
		usuario = "Charmander"
	if usuario == "3":
		usuario = "Squirtle"
	if usuario == "Charmander" or usuario == "Bulbasaur" or usuario == "Squirtle":
		Computador.append(usuario)
		print("Você escolheu o {}".format(usuario))
		break
	else:
		print("Escolha um Inspermon válido")
		
		
#COMANDO INICIAL PASSEAR/DORMIR/COMPUTADOR
while True:
	x=random.choice(list(Insperdex.keys()))
	y=random.choice(list(probbilidadefuga1))
	a = input("Você deseja passear, dormir ou ver seu computador?")
	if a == "dormir":
		print("Você encerrou o jogo, salvando...")
		time.sleep(1)
		print("Jogo salvo. Até a proxima!")
		exit()
	elif a == "computador":
		print(Computador)
	elif a == "passear":
		print("Passeando...")
		time.sleep(1)
		print("Aaah...Você encontrou um {} selvagem.".format(x))
		Computador.append(x)

				
	#INICIO BATALHA	
		b= input("Deseja batalhar ou fugir?")
		if b =="fugir":
			if y < 5:
				print("Você fugiu da batalha com sucesso")
					
			if y >= 5:
				print("Fuga mal sucedida!")
				b="batalhar"
				
		if b == "batalhar":
			print("Iniciando batalha...")
			time.sleep(1)
			print("Inspermon : {}".format(x))
			print("poder = {}".format(Insperdex[x]["poder"]))
			print("vida = {}".format(Insperdex[x]["vida"]))
			print("defesa = {}".format(Insperdex[x]["defesa"]))
			c= input("Voce deseja atacar ou fugir?")
			if c == "fugir":
				if y < 5:
					print("Você fugiu da batalha com sucesso")
			
				if y >= 5:
					print("Fuga mal sucedida, VOCÊ TERÁ que batalhar!")
				
			elif c == "atacar":
				while Insperdex[x]["vida"]>0 and Insperdex[usuario]["vida"]>0:
						
					ataca(usuario,x)
					ataca(x,usuario)			

					print("Vida do seu Inspermon:{}".format(Insperdex[usuario]["vida"]))
					print("vida do oponente:{}".format(Insperdex[x]["vida"]))
					time.sleep(1)
					if Insperdex[x]["vida"]<=0:
						print("Parabens!Voce ganhou a batalha")
						print("Vida do seu Inspermon = {}".format(Insperdex[usuario]["vida"]))
						print("XP ganho = {}".format(Insperdex[usuario]["xp1"]+Insperdex[x]["xp2"]))
						
					Insperdex[usuario]["vida"]=Insperdex[usuario]["vida"]-(Insperdex[x]["poder"]-Insperdex[usuario]["defesa"])
					if Insperdex[usuario]["vida"]<=0:
						print("Voce perdeu a batalha")
						time.sleep(1)
						print("Retornando ao InsperCenter para recuperar seu Inspermon...")
						time.sleep(1)
						print("A vida do seu Inspermon foi restaurada!")


"""COISAS QUE FALTAM:
→ FUNCIONALIDADE 1: FEITA
→ FUNCIONALIDADE 2: FEITA
→ FUNCIONALIDADE 3: FEITA
→ FUNCIONALIDADE 4:	Evolução
→ FUNCIONALIDADE 5: Salvar jogo"""