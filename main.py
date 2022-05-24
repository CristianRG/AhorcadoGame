from ahorcado import Ahorcado
import random

class Game(Ahorcado):

    def __init__(self):

        super().__init__()

        with open('words.txt') as f:
            self.words = f.read().split()
            

#         self.words = self.words

        
        self.difficulty = None
        self.wordsCorrets = []
        self.wordsIncorrects = []
        self.namePlayers = {
        }

    def registerNamePlayer(self):

        namePlayer = input('Nombre del Jugador: ')

        if(namePlayer in self.namePlayers.values()):
            namePlayer = None
        else:
            self.namePlayers.update({len(self.namePlayers.keys()) : namePlayer})
            playerId = list(self.namePlayers.keys())[list(self.namePlayers.values()).index(namePlayer)]
            return playerId

    def gameDifficulty(self):

        print('[1] Easy [2] Normal [3] Hard')
        try:
            self.difficulty = int(input('Indica el  nivel de dificultad: '))
        except ValueError:
            return 0

    def GenerateRandomWord(self):

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
        # wordRandom = self.words[random.randrange(len(self.words) -1)]
        # return wordRandom

    def generateSpaces(self, wordRandom):
        spacesWithe = '_' * len(wordRandom)
        return spacesWithe

    def replaceSpacesWhite(self, spacesWithe, wordRandom, wordUsed):
        for i in range(0, len(wordRandom)):
            try:
                if(wordUsed in wordRandom[i]):
                    spacesWithe = spacesWithe[:i] + wordRandom[i] + spacesWithe[i+1:]
            except TypeError:
                return spacesWithe
        return spacesWithe

        #     if(wordUsed in wordRandom[i]):
        #         spacesWithe = spacesWithe[:i] + wordRandom[i] + spacesWithe[i:]
        #     else:
        #         return spacesWithe
        # return spacesWithe

    def registerWordsCorrects(self, wordUsed, wordRandom):
        if(wordUsed in wordRandom):
            self.wordsCorrets.append(wordUsed)
        else:
            self.wordsIncorrects.append(wordUsed)

    def statusGame(self, spacesWithe, wordRandom):
        if(len(self.wordsIncorrects) == (len(self.sprite)-1)):
            print('\nGame Over')
            return 0
        elif(spacesWithe == wordRandom):
            print('\nYou won!')
            return 0


class StarGame(Game):

    def __init__(self):

        super().__init__()
        self.playerId = None
        self.namePlayer = None
        self.wordRandom = None
        self.spacesWithe = None
        

    def starGame(self):

        self.playerId = super().registerNamePlayer()
        self.namePlayer = self.namePlayers.get(self.playerId)
        super().gameDifficulty()
        self.wordRandom = super().GenerateRandomWord()
        self.spacesWithe = super().generateSpaces(self.wordRandom)
        self.wordUsed = None
        
        while True:

            self.spacesWithe = super().replaceSpacesWhite(self.spacesWithe, self.wordRandom, self.wordUsed)

            if(super().statusGame(self.spacesWithe, self.wordRandom) == 0):
                print('\tPlayer: {0}'.format(self.namePlayer))
                super().status(len(self.wordsIncorrects) +1)
                print(self.spacesWithe)
                break

            print('\tPlayer: {0}'.format(self.namePlayer))
            super().status(len(self.wordsIncorrects) +1)
            self.spacesWithe = super().replaceSpacesWhite(self.spacesWithe, self.wordRandom, self.wordUsed)
            print(self.spacesWithe)
            print('Palabras incorrectas: {0}'.format(self.wordsIncorrects))
            print('Palabras correctas: {0}'.format(self.wordsCorrets))
            self.wordUsed = input('Escriba una letra: ')
            super().registerWordsCorrects(self.wordUsed, self.wordRandom)

            
            
            


game = StarGame()
game.starGame()
# for i in range(1, 6):
#     verification = game.registerNamePlayer()
#     print(verification)
#     if(verification == 0):
#         print('El nombre de jugDador ya existe. Elija otro.')
#     else:
#         print('El nombre del jugador es: {0}'.format(game.namePlayer))