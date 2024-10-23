import random

import time

import threading

validMoves = {0: [1,4,5] , 1: [0, 2, 4, 5, 6] , 2: [1,3,5,6,7], 3: [2,6,7], 4: [0, 1, 5, 8, 9], 5: [0,1,2,4,6,8,9,10],
              6: [1,2,3,5,7,9,10,11], 7: [2,3,6,10,11], 8: [4,5,9,12,13], 9:[4,5,6,8,10,12,13,14], 10:[5,6,7,9,13,14,11,15],
              11: [6,7,10,14,15], 12: [8,9,13], 13: [8,9,10,12,14], 14: [9,10,11,13,15], 15: [10,11,14]}

playerStart = 1

mutex = threading.Lock()

Robot = 1

Bomb = 2

Gold = 3

Gold2 = 4

Bomb2 = 5

playerPiece = {1 : "R", 2 : "B", 3 : "G", 4 : "G", 5 : "B", 0 : " "}


class BoardState:
    board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    #empty board
    counter = 0
    lastBomb = Bomb2

    gameOver = False
    currPlayer = playerStart
    posRobot = random.randint(0,15)
    posBomb = random.randint(0,15)
    while posBomb == posRobot:
        posBomb = random.randint(0,15)
    
    posGold = random.randint(0,15)
    while posGold == posRobot or posGold == posBomb:
        posGold = random.randint(0,15)

    
    posGold2 = random.randint(0,15)
    while posGold2 == posRobot or posGold2 == posBomb or posGold2 == posGold:
        posGold2 = random.randint(0,15)

    posBomb2 = random.randint(0,15)
    while posBomb2 == posRobot or posBomb2 == posBomb or posBomb2 == posGold or posBomb2 == posGold2:
        posBomb2 = random.randint(0,15)

    board[posRobot] = Robot
    board[posBomb] = Bomb
    board[posGold] = Gold
    board[posGold2] = Gold2
    board[posBomb2] = Bomb2
state = BoardState()

def robotTurn():
    moves = validMoves[state.posRobot][:]     #specify valid moves
    if state.posBomb in moves:
        moves.remove(state.posBomb)             #ensure it does not hit the bomb
    newPosValue = random.randint(0, len(moves)-1)     #generate new robot position randomly moving towards the gold
    newPos = moves[newPosValue]
    state.board[state.posRobot] = 0
    state.posRobot = newPos
    state.board[newPos] = Robot

def bombTurn():
    moves = validMoves[state.posBomb][:]
    if state.posGold in moves: 
        moves.remove(state.posGold)
    if state.posGold2 in moves:
        moves.remove(state.posGold2)
    if state.posBomb2 in moves:
        moves.remove(state.posBomb2)
    newPosValue = random.randint(0,len(moves)-1)
    newPos = moves[newPosValue]
    state.board[state.posBomb] = 0
    state.posBomb = newPos
    state.board[newPos] = Bomb

def bombTurn2():
    moves = validMoves[state.posBomb2][:]
    if state.posGold in moves: 
        moves.remove(state.posGold)
    if state.posGold2 in moves:
        moves.remove(state.posGold2)
    if state.posBomb in moves:
        moves.remove(state.posBomb)
    newPosValue = random.randint(0,len(moves)-1)
    newPos = moves[newPosValue]
    state.board[state.posBomb2] = 0
    state.posBomb2 = newPos
    state.board[newPos] = Bomb2

def TakeTurn(playerName):
    global state
    global mutex
    global Robot
    global Bomb
    global Bomb2
    global moves

    try:
        state.counter +=1
        if state.gameOver == True:
            return
        
        printBoard()
        if playerName == Robot:
            robotTurn()             #call function to make move
            
            if state.posRobot == state.posGold:
                state.posGold = -1
            if state.posRobot == state.posGold2:
                state.posGold2 = -1
        
            if state.lastBomb == Bomb:
                state.currPlayer = Bomb2
            elif state.lastBomb == Bomb2:
                state.currPlayer = Bomb

        elif playerName == Bomb:
            bombTurn()
            if state.posBomb == state.posRobot:
                state.gameOver = True
            state.lastBomb = Bomb
            state.currPlayer = Robot

        elif playerName == Bomb2:
            bombTurn2()
            if state.posBomb2 == state.posRobot:
                state.gameOver = True
            state.lastBomb = Bomb2
            state.currPlayer = Robot
        
        
        if state.posGold == -1 and state.posGold2 == -1 :
            print ("Robot wins")
            state.gameOver = True

        if state.posBomb == state.posRobot or state.posBomb2 == state.posRobot:
            print ("Bomb wins")
            state.gameOver = True
        print(state.counter)

    except Exception as e:
        print (e)
        mutex.release()
        
def printBoard():
    global state
    print(f' {playerPiece[state.board[0]]} | {playerPiece[state.board[1]]} | {playerPiece[state.board[2]]} | {playerPiece[state.board[3]]} ')

    print('---|---|---|---')

    print(f' {playerPiece[state.board[4]]} | {playerPiece[state.board[5]]} | {playerPiece[state.board[6]]} | {playerPiece[state.board[7]]} ')

    print('---|---|---|---')

    print(f' {playerPiece[state.board[8]]} | {playerPiece[state.board[9]]} | {playerPiece[state.board[10]]} | {playerPiece[state.board[11]]} ')

    print('---|---|---|---')

    print(f' {playerPiece[state.board[12]]} | {playerPiece[state.board[13]]} | {playerPiece[state.board[14]]} | {playerPiece[state.board[15]]} \n\n')

def game(playerName):
    global state
    global mutex
    while state.gameOver == False:
        mutex.acquire()
        if playerName == state.currPlayer:
            TakeTurn(playerName)
        mutex.release()
        time.sleep(.5)
    


def main():
    global Robot
    global Bomb
    global Bomb2
    
    thread1 = threading.Thread(target = game, args = (Robot,))
    thread2 = threading.Thread(target = game, args = (Bomb,))
    thread3 = threading.Thread(target = game, args = (Bomb2,))


    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    printBoard()
    

if __name__ == "__main__":
    main()
    