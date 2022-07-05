from tkinter import *

First = True

lastTouched = ""

wholeButtonField = []

fieldOfColors = []

blackTower = chr(9820)
blackHorse = chr(9822)
blackBishof = chr(9821)
blackQueen = chr(9818)
blackKing = chr(9819)
blackPawn = chr(9823)

whiteTower = chr(9814)
whiteHorse = chr(9816)
whiteBishof = chr(9815)
whiteQueen = chr(9813)
whiteKing = chr(9812)
whitePawn = chr(9817)

#############################################################
#makes a chess board
def generateChessBoard():

    playboard = []

    firstTeamFirstRow = [blackTower, blackHorse, blackBishof, blackKing, blackQueen, blackBishof, blackHorse, blackTower]
    firstTeamPawnLine = [blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn, blackPawn]
    
    SecondTeamFirstRow = [whiteTower, whiteHorse, whiteBishof, whiteKing, whiteQueen, whiteBishof, whiteHorse, whiteTower]
    SecondTeamPawnLine = [whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn, whitePawn]

    playboard.append(firstTeamFirstRow)
    playboard.append(firstTeamPawnLine)
    for eachEmpty in range(4):
        playboard.append(["", "", "", "", "", "", "", ""])
    playboard.append(SecondTeamPawnLine)
    playboard.append(SecondTeamFirstRow)

    """
    for each in playboard:
        print(each)
        """
    createGameInterface(playboard)
        
######################################################

#Generates the whole button bed
def createGameInterface(board):
    global wholeButtonField
    global fieldOfColors
    FieldColor = True
    window = Tk(
    #Y coord of the field
    for plateHeight in range(len(board)):
        wholeLine = []
        colorLine = []
        FieldColor = not FieldColor
        #X coord of the field
        for plateSide in range(len(board[0])):
            FieldColor = not FieldColor
            Field = Button(window, text=board[plateHeight][plateSide], height=3, width = 5)
            Field.configure(command=lambda Field = Field, plateHeight = plateHeight, plateSide = plateSide:
                            selectAndMove([plateHeight, plateSide], Field),
                            font = ("calibri", 20))
            if FieldColor:
                colorLine.append("Grey")
                Field.configure(bg = "Grey")
            else:
                colorLine.append("White")
                Field.configure(bg = "White")
            Field.grid(row = plateHeight, column = plateSide)
            wholeLine.append(Field)
        fieldOfColors.append(colorLine)
        wholeButtonField.append(wholeLine)
    
    window.geometry("650x1000")
    window.mainloop()

# selects a place and check if valid or not
def selectAndMove(Place, Object):
    global wholeButtonField
    global fieldOfColors
    global lastTouched
    global First

    #######################################
    #resets color everytime
    for YCoord in range(len(wholeButtonField)):
        for XCoord in range(len(wholeButtonField[0])):
            wholeButtonField[YCoord][XCoord].configure(bg = fieldOfColors[YCoord][XCoord])

##################################################################
    #possible moves
    markedPlaces = []
    
    First = Place[0]
    Second = Place[1]

    def linearMoveSet():
        for line in range(len(wholeButtonField[First])):
            wholeButtonField[First][line].configure(bg = "Green")
        for lineTwo in range(len(wholeButtonField)):
            wholeButtonField[lineTwo][Second].configure(bg = "Green")

    def sideMoveSet():
        #############################################################
        #############################################################
        #############################################################
        ##################Last place touched#########################
        #############################################################
        #############################################################
        #############################################################
        wholeButtonField[lineTwo][line].configure(bg = "Green")
        
        wholeButtonField[line][lineTwo].configure(bg = "Green")

    objText = Object["text"]

    if objText == whitePawn:
        if Object == wholeButtonField[6][Second]:
            wholeButtonField[First - 2][Second].configure(bg = "Green")
        wholeButtonField[First - 1][Second].configure(bg = "Green")
        
    elif objText == whiteTower:
        linearMoveSet()

    elif objText == whiteQueen:
        linearMoveSet()
        sideMoveSet()

    elif objText == whiteBishof:
        sideMoveSet()

    wholeButtonField[Place[0]][Place[1]].configure(bg="Blue")
    
        
generateChessBoard()
