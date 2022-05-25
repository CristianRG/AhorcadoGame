import images # importamos 3l archivo que contiene las escenas/imagenes del ahorcadp
import words
import random
import os
from colorama import Fore, Back

class Game(): # clase padre

    def __init__(self):

        self.sprite = images.images
        self.difficulty = None
        self.wordsCorrets = []
        self.wordsIncorrects = []
        self.words = words.wordsGenerate()
        self.namePlayers = {
        }
        self.score = 0


    def statusAhorcado(self, NOfErrors): # en base al numero de errores obtenidos, imprime una imagen del ahorcado
        print(self.sprite[NOfErrors -1])
        return 0 

    def registerNamePlayer(self): # registra el nombre del jugador, incluso podria registrar diferentes jugadores

        namePlayer = input('Nombre del Jugador: ')

        if(namePlayer in self.namePlayers.values()):
            namePlayer = None
        else:
            self.namePlayers.update({len(self.namePlayers.keys()) : namePlayer})
            playerId = list(self.namePlayers.keys())[list(self.namePlayers.values()).index(namePlayer)]
            return playerId

    def gameDifficulty(self): # indicamos una dificultad para tener palabras mas cortas o  largas

        print('[1] Easy [2] Normal [3] Hard')
        try:
            self.difficulty = int(input('Indica el  nivel de dificultad: '))
        except ValueError:
            return 0

    def GenerateRandomWord(self): # genera la palabra random en base a la dificultad indicada

        if(self.difficulty == 1):
            wordsDifficulty = [i for i in self.words if(len(i) >= 3 and len(i) <= 5)]
        elif(self.difficulty == 2):
            wordsDifficulty = [i for i in self.words if(len(i) >= 5 and len(i) <= 8)]
        elif(self.difficulty == 3):
            wordsDifficulty = [i for i in self.words if(len(i) >= 8 and len(i) <= 12)]
        else:
            return 0

        wordRandom = wordsDifficulty[random.randrange(len(wordsDifficulty) -1)]
        return wordRandom

    def generateSpaces(self, wordRandom): # genera los espacios en blanco una vez la palabra random fue generada
        spacesWhithe = '_' * len(wordRandom)
        return spacesWhithe

    def replaceSpacesWhite(self, spacesWhithe, wordRandom, wordUsed): # remplaza esos espacios sí la palabra de entrada coincide con la random
        for i in range(0, len(wordRandom)):
            try:
                if(wordUsed in wordRandom[i]):
                    spacesWhithe = spacesWhithe[:i] + wordRandom[i] + spacesWhithe[i+1:]
            except TypeError:
                return spacesWhithe
        return spacesWhithe

    def registerWordsCorrects(self, wordUsed, wordRandom): # registra las palabras correctas o incorrectas usadas
        if(wordUsed in wordRandom):
            self.wordsCorrets.append(wordUsed)
        else:
            self.wordsIncorrects.append(wordUsed)

    def statusGame(self, spacesWhithe, wordRandom): # indica si has ganado o perdido, ganado si descubres todas las palabras, y perdido si ya estas ahorcado
        if(len(self.wordsIncorrects) == (len(self.sprite)-1)):
            print(Fore.RED + '\n\t\t\tGame Over' + Fore.RESET)
            return 0
        elif(spacesWhithe == wordRandom):
            print(Fore.GREEN + '\n\t\t\tYou won!' + Fore.RESET)
            return 0

    def scorePlayer(self):
        self.score = 20 * len(self.wordsCorrets)
        return self.score

    def clearScreen(self):
        os.system('cls')


class StarGame(Game): # clase hija, se encarga de iniciar todo el juego

    def __init__(self):

        super().__init__()
        self.restarGameControl = False
        self.playerId = None
        self.namePlayer = None
        self.wordRandom = None
        self.spacesWhithe = None
        
    def starGame(self): # metodo que inicia todos los metodos de la clase padre para iniciar el juego
        super().clearScreen()
        self.playerId = super().registerNamePlayer()
        self.namePlayer = self.namePlayers.get(self.playerId)
        super().gameDifficulty()
        self.wordRandom = super().GenerateRandomWord()
        self.spacesWhithe = super().generateSpaces(self.wordRandom)
        self.wordUsed = None
        
        while True:
            self.score = super().scorePlayer()
            super().clearScreen()
            self.spacesWhithe = super().replaceSpacesWhite(self.spacesWhithe, self.wordRandom, self.wordUsed)

            if(super().statusGame(self.spacesWhithe, self.wordRandom) == 0):
                print('\tPlayer: {0}'.format(self.namePlayer), end=Fore.GREEN + '\tScore: {0}'.format(self.score) + Fore.RESET)
                super().statusAhorcado(len(self.wordsIncorrects) +1)
                print(self.spacesWhithe)
                print(self.wordRandom)
                break

            print('\nPlayer: {0}'.format(self.namePlayer), end=Fore.GREEN + '\tScore: {0}'.format(self.score) + Fore.RESET)
            super().statusAhorcado(len(self.wordsIncorrects) +1)
            self.spacesWhithe = super().replaceSpacesWhite(self.spacesWhithe, self.wordRandom, self.wordUsed)
            print(self.spacesWhithe)
            print('Palabras incorrectas: {0}'.format(self.wordsIncorrects))
            print('Palabras correctas: {0}'.format(self.wordsCorrets))
            self.wordUsed = input('Escriba una letra: ')
            super().registerWordsCorrects(self.wordUsed, self.wordRandom)

    def restartGame(self):

        print('[1] Si [2] No')
        res = int(input('¿Desea volver a jugar? ')) 

        if(res == 1):
            super().__init__()
            StarGame().__init__()
            self.restarGameControl = True
            return self.restarGameControl
        else:
            print('Gracias por jugar!')
            self.restarGameControl = False
            return self.restarGameControl

            
game = StarGame()
game.starGame()
game.restartGame()

while game.restarGameControl == True:
    game.starGame()
    game.restartGame()
