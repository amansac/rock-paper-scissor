# !/usr/bin/python3

from tkinter import *
import simpleaudio as sa
import random


Won = 0
Lost = 0
Drawn = 0

root = Tk()

root.title("Rock-Paper-Scissor")
root.configure(bg="#52c4bb")
root.resizable(width = False, height = False)


RockBtn = ""  #Button for Rock
PaperBtn = ""  #Button for Paper
ScissorBtn = ""  #Button for Scissor
ScoreBtn = ""  #Button for Score


PlayAud = sa.WaveObject.from_wave_file("sounds/Play.wav")  #Play sound
WonAud = sa.WaveObject.from_wave_file("sounds/Won.wav")  #Won sound
LostAud = sa.WaveObject.from_wave_file("sounds/Lost.wav")  #Lost sound
DrawAud = sa.WaveObject.from_wave_file("sounds/Draw.wav")  #Drawn sound


PlayAud.play()  #Start


PRockImg = PhotoImage(file = "images/P_Rock.png")  #Player's Rock image
PPaperImg = PhotoImage(file = "images/P_Paper.png")  #Player's Paper image
PScissorImg = PhotoImage(file = "images/P_Scissor.png")  #Player's Scissor image

CRockImg = PhotoImage(file = "images/C_Rock.png")  #Computer's Rock image
CPaperImg = PhotoImage(file = "images/C_Paper.png")  #Computer's Paper image
CScissorImg = PhotoImage(file = "images/C_Scissor.png")  #Computer's Scissor image

PlayImg = PhotoImage(file = "images/Play.png")  #Play image

WonImg = PhotoImage(file = "images/Won.png")  #Won image
LostImg = PhotoImage(file = "images/Lost.png")  #Lost image
DrawImg = PhotoImage(file = "images/Draw.png")  #Draw image


ResultBtn = Button(root, image = PlayImg)  #Result Button

clk = True  #Setting Click as True


#Computer's Choice
def opponentChoice():
	selects = random.choice(["Rock","Paper","Scissor"])
	return selects
	

#Your's Choice
def playerChoice(plMove):
	global clk, Won, Lost, Drawn
	
	opMove = opponentChoice()  #Getting Computer's Choice
	
	if clk == True:
		if plMove == "Rock":
			RockBtn.configure(image = PRockImg)
			if opMove == "Rock":
				ResultBtn.configure(image = DrawImg)
				PaperBtn.configure(image = CRockImg)
				DrawAud.play()
				Drawn += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Paper":
				ResultBtn.configure(image = LostImg)
				PaperBtn.configure(image = CPaperImg)
				LostAud.play()
				Lost += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Scissor":
				ResultBtn.configure(image = WonImg)
				PaperBtn.configure(image = CScissorImg)
				WonAud.play()
				Won += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))

		elif plMove == "Paper":
			RockBtn.configure(image = PPaperImg)
			if opMove == "Rock":
				ResultBtn.configure(image = WonImg)
				PaperBtn.configure(image = CRockImg)
				WonAud.play()
				Won += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Paper":
				ResultBtn.configure(image = DrawImg)
				PaperBtn.configure(image = CPaperImg)
				DrawAud.play()
				Drawn += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Scissor":
				ResultBtn.configure(image = LostImg)
				PaperBtn.configure(image = CScissorImg)
				LostAud.play()
				Lost += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))

		elif plMove == "Scissor" :
			RockBtn.configure(image = PScissorImg)
			if opMove == "Rock":
				ResultBtn.configure(image = LostImg)
				PaperBtn.configure(image = CRockImg)
				LostAud.play()
				Lost += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Paper":
				ResultBtn.configure(image = WonImg)
				PaperBtn.configure(image = CPaperImg)
				WonAud.play()
				Won += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
			elif opMove == "Scissor":
				ResultBtn.configure(image = DrawImg)
				PaperBtn.configure(image = CScissorImg)
				DrawAud.play()
				Drawn += 1
				ScoreBtn.configure(text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
		
		ScissorBtn.grid_forget()
		clk = False
		
	else:
		ResultBtn.configure(image = PlayImg)
		RockBtn.configure(image = PRockImg)
		PaperBtn.configure(image = PPaperImg)
		ScissorBtn.configure(image = PScissorImg)
		
		ScissorBtn.grid(row = 0, column = 2)
		
		clk = True
		PlayAud.play()


#Main Game Logic
def game():
	global RockBtn, PaperBtn, ScissorBtn, ScoreBtn
	
	RockBtn = Button(root, image = PRockImg, command = lambda:playerChoice("Rock"))
	RockBtn.grid(row = 0, column = 0)
	
	PaperBtn = Button(root, image = PPaperImg, command = lambda:playerChoice("Paper"))
	PaperBtn.grid(row = 0, column = 1)
		
	ScissorBtn = Button(root, image = PScissorImg, command = lambda:playerChoice("Scissor"))
	ScissorBtn.grid(row = 0, column = 2)
	
	ScoreBtn = Button(root, text = "Won : "+ str(Won) + "  Lost : "+ str(Lost) + "  Drawn : "+ str(Drawn))
	ScoreBtn.grid(row = 1, column = 0, columnspan = 5)
	
	ResultBtn.grid(row = 2, column = 0, columnspan = 5)
                

game()

root.mainloop()

