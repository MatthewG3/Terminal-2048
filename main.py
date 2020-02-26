# created by Matthew Gorena 2/26/20

from random import random, randint


class Game():

    def __init__(self):
        # created game 'board'
        self.gameList = [['0', '0', '0', '0'],
                        ['0', '0', '0', '0'],
                        ['0', '0', '0', '0'],
                        ['0', '0', '0', '0']]

        # values that can be added
        self.startingValues = ['2', '4']

        self.randomizerWeight = 0.8

        self.gameOver = False


    # uses a random number to add a value from startingValues to the game board
    def createNum(self):
        randNum = random()

        if randNum < self.randomizerWeight:
            self.addNum(self.startingValues[0])
        else:
            self.addNum(self.startingValues[1])


    # checks if a certain value is open on the board
    def checkNum(self):
        while True:
            x, y = randint(0, 3), randint(0, 3)
            if self.gameList[x][y] == '0':
                return [x, y]
            elif self.noMoreSpots():
                return [-1, -1]


    # add number to the game board
    def addNum(self, num):
        position = self.checkNum()

        if not -1 in position:
            self.gameList[position[0]][position[1]] = num


    def noMoreSpots(self):
        for i in self.gameList:
            if '0' in i:
                return False
        return True


    # checks if no more moves are possible
    def isGameOver(self):
        # initially checks to see if there are any 0 values, or no values meaning there is not even a value in the game assigned to any index
        for i in self.gameList:
            if '0' in i:
                self.gameOver = False
                return False

        # checks to see if there are any values next to each other that equal each other, if that is true the game is not yet over and isGameOver returns false
        for i in range(len(self.gameList) - 1):
            for j in range(len(self.gameList[0]) - 1):
                if self.gameList[i][j] == self.gameList[i][j+1]:
                    self.gameOver = False
                    return False
                if self.gameList[i][j] == self.gameList[i+1][j]:
                    self.gameOver = False
                    return False

        self.gameOver = True
        return True


    # show game over statement and then return true/false based on if the user wants to play again
    def gamesOver(self):
        if self.gameOver:
            print('Game Over!')
            return True


    def move(self):
        inp = input('Used WASD to move the Board or type stop to stop: ')
        inp = inp.lower()

        if inp == 'w':
            li = []
            for i in range(len(self.gameList[0])):
                for j in range(len(self.gameList)):
                    li.append(self.gameList[j][i])
                li = self.algo(li)
                for j in range(len(self.gameList)):
                    self.gameList[j][i] = li[j]
                li = []


        elif inp == 'a':
            for i in range(len(self.gameList)):
                self.gameList[i] = self.algo(self.gameList[i])

        elif inp == 's':
            li = []
            for i in range(len(self.gameList[0])):
                for j in range(len(self.gameList)):
                    li.append(self.gameList[j][i])
                li.reverse()
                li = self.algo(li)
                li.reverse()
                for j in range(len(self.gameList)):
                    self.gameList[j][i] = li[j]
                li = []

        elif inp == 'd':
            for i in range(len(self.gameList)):
                a = self.gameList[i]
                a.reverse()
                li = self.algo(a)
                li.reverse()
                self.gameList[i] = li

        elif inp == 'stop':
            self.gameOver = True

        else:
            print('That is not a valid input.')
            self.move()


    def algo(self, li):
        li = [i for i in li if i != '0']

        for i in range(len(li) - 1):
            if li[i] == li[i+1]:
                li[i] = str(int(li[i]) * 2)
                li[i+1] = '0'

        li = [i for i in li if i != '0']

        while len(li) < 4:
            li.append('0')

        return li


    def printBoard(self):
        def format(string):
            while len(string) <= 4:
                string = ' ' + string
            return string

        string = ''
        for i in range(len(self.gameList)):
            for j in range(len(self.gameList[i])):
                string += ' ' + format(self.gameList[i][j]) + ' '
            string += '\n'

        print(string)


    # changes weight based on the highest block on the grid
    def randomizerWeightUpdate(self):
        if '256' in self.gameList:
            self.randomizerWeight = 0.5
        elif '2048' in self.gameList:
            self.randomizerWeight = 0.2


    def updateList(self):
        self.isGameOver()
        self.printBoard()
        tempList = [[], [], [], []]
        for i in range(len(self.gameList)):
            for j in range(len(self.gameList[i])):
                tempList[i].append(self.gameList[i][j])
        self.move()
        self.randomizerWeightUpdate()
        if tempList != self.gameList:
            self.createNum()
        elif self.noMoreSpots() and self.gameOver:
            self.gamesOver()


    def startGame(self):
        self.createNum()
        self.createNum()


def main():
    game = Game()
    game.startGame()

    while True:
        game.updateList()

        if game.gamesOver():
            break


if __name__ == "__main__":
    main()
