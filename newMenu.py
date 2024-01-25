from bishop import Bishop
from horse import Horse
from pawn import Pawn
from queen import Queen
#from king import King
from rook import Rook
from piece import Piece


############################Functions################################

#Function that will switch turns once the user has made their move.
def change_turn(turn):
  if turn == "White":
    turn = "Black"
  else:
    turn = "White"
  return turn

#This function will change the letter entered by the user from its position to its corresponding number. For example, from 'd' to 3.
def change_letter(letra):
  return ord(letra) - 97

#This function will convert our string-type number to an integer and assign it a value between 0 and 7. We subtract 1 because the user enters numbers between 1 and 8.
def change_number(numero):
  return 7 - (int(numero)-1)

# Convert a pawn into a piece of higher value.
def promote_pawn(XNew, YNew, board):
  pawnOption = int(input("Choose a piece:\n\t1. Queen\n\t2. Rook\n\t3. Bishop\n\t4. Knight\n"))

  while pawnOption not in [1,2,3,4]:
    pawnOption= int(input("Invalid option. Choose a piece: "))

  if board[YNew][XNew].color == "White" and YNew==0:
    options={1: Queen("White", XNew, YNew),
             2: Rook("White", XNew, YNew),
             3: Bishop("White", XNew, YNew),
             4: Horse("White", XNew, YNew)}
    board[YNew][XNew] = options[pawnOption]
    
  elif board[YNew][XNew].color == "Black" and YNew==0:
    options={1: Queen("Black", XNew, YNew),
             2: Rook("Black", XNew, YNew),
             3: Bishop("Black", XNew, YNew),
             4: Horse("Black", XNew, YNew)}
    board[YNew][XNew] = options[pawnOption]

# A function that allows capturing a pawn that has moved two squares in chess.
def en_passant(XCurrent, YCurrent, XNew, YNew, board):
  board[YNew][XNew] = board[YCurrent][XCurrent]
  board[YCurrent][XCurrent] = None
  if board[YNew][XNew].color == "White":
    board[YNew + 1][XNew] = None
  else:
    board[YNew - 1][XNew] = None

def move(XCurrent, YCurrent, XNew, YNew, board, turn, whiteKing, blackKing):
  if board[YNew][XNew] != None:
    board[YNew][XNew] = None
    board[YNew][XNew] = board[YCurrent][XCurrent]
    board[YCurrent][XCurrent] = None
  
  else:
    board[YNew][XNew] = board[YCurrent][XCurrent]
    board[YCurrent][XCurrent] = None

  board[YNew][XNew].x = XNew
  board[YNew][XNew].y = YNew

  if board[YNew][XNew].tag == "k":
    if turn == "White":
      whiteKing = (YNew, XNew)
    elif turn == "Black":
      blackKing = (YNew, XNew)


def king_jaque(turn, board, WhiteKing, BlackKing):
  if turn == "White":
    return board[change_number(WhiteKing[1])][change_letter(WhiteKing[0])].is_jaque() #Checar
  else:
    return board[change_number(BlackKing[1])][change_letter(BlackKing[0])].is_jaque() #Checar
  
def check_mate(whiteKing, blackKing, whitePieces, blackPieces, turn, board):
  if turn == "White":
    xKing = whiteKing[0]
    yKing = whiteKing[1]

    for piece in whitePieces:
      xCurrent = piece.x
      yCurrent = piece.y
      validMoves = piece.valid_moves(board)

      for moves in validMoves: 
        xNew = moves[1]
        yNew = moves[0]

        capturedPiece = board[yNew][xNew]

        move(xCurrent, yCurrent, xNew, yNew, board, turn, whiteKing, blackKing)

        if !(board[yKing][xKing].check(board)):
          move(xNew, yNew, xCurrent, yCurrent, board, turn, whiteKing, blackKing)
          board[yNew][xNew] = capturedPiece
          return False
        
        move(xNew, yNew, xCurrent, yCurrent, board, turn, whiteKing, blackKing)
        board[yNew][xNew] = capturedPiece
    return True

  elif turn == "Black":
    xKing=blackPieces[0]
    yKing=blackPieces[1]

    for piece in blackPieces:
      xCurrent = piece.x
      yCurrent = piece.y
      validMoves = piece.valid_moves(board)

      for moves in validMoves: 
        xNew = moves[1]
        yNew = moves[0]

        capturedPiece = board[yNew][xNew]

        move(xCurrent, yCurrent, xNew, yNew, board, turn, whiteKing, blackKing)

        if !(board[yKing][xKing].check(board)):
          move(xNew, yNew, xCurrent, yCurrent, board, turn, whiteKing, blackKing)
          board[yNew][xNew] = capturedPiece
          return False
        
        move(xNew, yNew, xCurrent, yCurrent, board, turn, whiteKing, blackKing)
        board[yNew][xNew] = capturedPiece
    return True
  


def drowned(whitePieces, blackPieces, turn, board):
  if turn == "White":
    for piece in whitePieces:
      if piece.valid_moves(board) > 0:
        return False
    return True
  
  elif turn == "Black":
    for piece in blackPieces:
      if piece.valid_moves(board) > 0:
        return False
    return True

def castle(XCurrent, YCurrent, XNew, YNew, board, turn, whiteKing, blackKing): #Checar
  #Mover al rey
  board[YNew][XNew] = None
  board[YNew][XNew] = board[YCurrent][XCurrent]
  board[YCurrent][XCurrent] = None
  
  #Mover a la torre 
  if turn == "White":
    if XCurrent - XNew < 0: #enroque corto
      board[7][5] = None
      board[7][5] = board[7][7]
      board[7][7] = None 
      board[7][5].x = 5
      board[7][5].y = 7

    else: #enroque largo 
      board[7][3] = None
      board[7][3] = board[7][0]
      board[7][0] = None 
      board[7][3].x = 3
      board[7][3].y = 7
  
  elif turn == "Black":
    if XCurrent - XNew < 0: #enroque largo
      board[0][3] = None
      board[0][3] = board[0][0]
      board[0][0] = None 
      board[0][3].x = 3
      board[0][3].y = 0

    else: #enroque corto 
      board[0][5] = None
      board[0][5] = board[0][7]
      board[0][7] = None 
      board[0][5].x = 5
      board[0][5].y = 0

  board[YNew][XNew].x = XNew
  board[YNew][XNew].y = YNew

  if board[YNew][XNew].tag == "k":
    if turn == "White":
      whiteKing = (YNew, XNew)
    elif turn == "Black":
      blackKing = (YNew, XNew)
      
#_________________________________________________________________________________________________________________________________________
# We create an 8x8 matrix which will be our board.
board = [[None for _ in range(8)] for _ in range(8)]

#-------------------------WHITE------------------------
#board[7][4] = King("White", 4, 7)
board[7][3] = Queen("White", 3, 7)
board[7][1] = Horse("White", 1, 7)
board[7][6] = Horse("White", 6, 7)
board[7][2] = Bishop("White", 2, 7)
board[7][5] = Bishop("White", 5, 7)
board[7][0] = Rook("White", 0, 7)
board[7][7] = Rook("White", 7, 7)
board[6][0] = Pawn("White", 0, 6)
board[6][1] = Pawn("White", 1, 6)
board[6][2] = Pawn("White", 2, 6)
board[6][3] = Pawn("White", 3, 6)
board[6][4] = Pawn("White", 4, 6)
board[6][5] = Pawn("White", 5, 6)
board[6][6] = Pawn("White", 6, 6)
board[6][7] = Pawn("White", 7, 6)

#-------------------------BLACK------------------------
#board[0][4] = King("Black", 4, 0)
board[0][3] = Queen("Black", 3, 0)
board[0][1] = Horse("Black", 1, 0)
board[0][6] = Horse("Black", 6, 0)
board[0][2] = Bishop("Black", 2, 0)
board[0][5] = Bishop("Black", 5, 0)
board[0][0] = Rook("Black", 0, 0)
board[0][7] = Rook("Black", 7, 0)
board[1][0] = Pawn("Black", 0, 1)
board[1][1] = Pawn("Black", 1, 1)
board[1][2] = Pawn("Black", 2, 1)
board[1][3] = Pawn("Black", 3, 1)
board[1][4] = Pawn("Black", 4, 1)
board[1][5] = Pawn("Black", 5, 1)
board[1][6] = Pawn("Black", 6, 1)
board[1][7] = Pawn("Black", 7, 1)

#-------------------------WHITE------------------------
# We create an list of 16 elements which will be our white pieces.
whitePieces= [
  #board[7][4],
  board[7][3],
  board[7][1],
  board[7][6],
  board[7][2],
  board[7][5],
  board[7][0],
  board[7][7],
  board[6][0],
  board[6][1],
  board[6][2],
  board[6][3],
  board[6][4],
  board[6][5],
  board[6][6],
  board[6][7]
]

whitePieces= set(whitePieces)
"""
#whitePices.append(King("White", 4, 7))
whitePices.append(Queen("White", 3, 7))
whitePices.append(Horse("White", 1, 7))
whitePices.append(Horse("White", 6, 7))
whitePices.append(Bishop("White", 2, 7))
whitePices.append(Bishop("White", 5, 7))
whitePices.append(Rook("White", 0, 7))
whitePices.append(Rook("White", 7, 7))
whitePices.append(Pawn("White", 0, 6))
whitePices.append(Pawn("White", 1, 6))
whitePices.append(Pawn("White", 2, 6))
whitePices.append(Pawn("White", 3, 6))
whitePices.append(Pawn("White", 4, 6))
whitePices.append(Pawn("White", 5, 6))
whitePices.append(Pawn("White", 6, 6))
whitePices.append(Pawn("White", 6, 1))
"""


#-------------------------BLACK------------------------
blackPieces = [
  #board[0][4],
  board[0][3],
  board[0][1],
  board[0][6],
  board[0][2],
  board[0][5],
  board[0][0],
  board[0][7],
  board[1][0],
  board[1][1],
  board[1][2],
  board[1][3],
  board[1][4],
  board[1][5],
  board[1][6],
  board[1][7],
]

blackPieces = set(blackPieces)

"""blackPieces.append(King("Black", 4, 0))
blackPieces.append(Queen("Black", 3, 0))
blackPieces.append(Horse("Black", 1, 0))
blackPieces.append(Horse("Black", 6, 0))
blackPieces.append(Bishop("Black", 2, 0))
blackPieces.append(Bishop("Black", 5, 0))
blackPieces.append(Rook("Black", 0, 0))
blackPieces.append(Rook("Black", 7, 0))
blackPieces.append(Pawn("Black", 0, 1))
blackPieces.append(Pawn("Black", 1, 1))
blackPieces.append(Pawn("Black", 2, 1))
blackPieces.append(Pawn("Black", 3, 1))
blackPieces.append(Pawn("Black", 4, 1))
blackPieces.append(Pawn("Black", 5, 1))
blackPieces.append(Pawn("Black", 6, 1))
blackPieces.append(Pawn("Black", 7, 1))"""

print("-----------------------------")
print("|          Welcome          |")
print("-----------------------------")

menuOption=0 # Option to resign, offer a draw, or move a piece
turn = "White" # It will tell us whose turn it is to play
whiteKing = (7, 4) # White king's position
blackKing = (0, 4) # Black king's position
pawn_enPassant = []
isCheck = False

while menuOption!=1:
  if pawn_enPassant:
    if pawn_enPassant[-1] == turn:
      board[pawn_enPassant[1]][pawn_enPassant[0]].enPassant =False
      pawn_enPassant = []



  # Print board
  for i in range(8):
    for j in range(8):
      if board[i][j] == None:
        print("[   ]", end="")
      else:
        print("[", board[i][j].tag, "]", end="")

      if j == 7:
        print(" ", 8 - i)
  print("  a    b    c    d    e    f    g    h")
  print("Your turn ", turn)
  menuOption=int(input("\n\t1. Surrender \n\t2. Offer a draw \n\t3. Move a piece\n "))
  # Surrender
  if menuOption == 1:
    print("Congratulations, ", change_turn(turn), ", you have won.")
  
  #Offer a draw
  elif menuOption == 2:
    acceptDraw=str(input("The other player accepts the draw? (yes/no): "))

    if acceptDraw=='yes' or acceptDraw=='Yes':
        print("It's a draw.")
        break
    elif acceptDraw == 'no' or acceptDraw == 'No':
        change_turn(turn)
    else: 
      while acceptDraw != 'yes' or acceptDraw=='Yes' or acceptDraw != 'no' or acceptDraw == 'No':
        acceptDraw = str(input("Invalid option. Please enter another option: "))
    
  
  #Move piece
  elif menuOption == 3:
    if isCheck and check_mate(whiteKing, blackKing, whitePieces, blackPieces, turn, board): #Checar
      print("Checkmate, you have lost ", turn)
      break

    if drowned(whitePieces, blackPieces, turn, board): #Checar
      print("Drowned")

    while True:
      movePiece = str(input("Piece to move (enter the position, for example \"d3\"):  ")) # Position of the piece we want to move.
      XCurrent = change_letter(movePiece[0]) 
      YCurrent = change_number(movePiece[1])

      if YCurrent < 0 or YCurrent > 7 or len(movePiece) != 2:
        print("Invalid position")
        continue
      elif XCurrent < 0 or XCurrent > 7 or len(movePiece) != 2:
        print("Invalid position")
        continue
      elif (board[YCurrent][XCurrent] == None):
        print("There is no piece at this position")
        continue
      elif (board[YCurrent][XCurrent].color != turn):
        print("Does not match its color")
        continue
      
      currentPiece = board[YCurrent][XCurrent] # Current position already validated

      newPosition= str(input("Where do I want to move the piece? ")) # Where do I want to move the piece?
      XNew = change_letter(newPosition[0]) # New X position
      YNew = change_number(newPosition[1]) # New Y position 


      print(currentPiece.valid_moves(board))
      if (YNew, XNew) not in currentPiece.valid_moves(board):
        print("No valid position")
        continue

      #Check if the opposing king is in check to set the variable 'isCheck' as True and verify in the next loop if it is not a checkmate
      elif king_jaque(change_turn(turn), board, whiteKing, blackKing): #Checar
        isCheck = True
        change_turn(turn) 

      else: 
        isCheck = False
        change_turn(turn) 

      if currentPiece.tag == "p":
        if abs(YCurrent - YNew) == 2 and currentPiece.cont == 0:
          currentPiece.enPassant = True
          pawn_enPassant = [XNew, YNew, turn]
        
        currentPiece.cont = 1
       
      if currentPiece.tag == "k" and abs(XCurrent -XNew) > 1: #Checar 
        castle(XCurrent, YCurrent, XNew, YNew, board, turn, whiteKing, blackKing)
        break

      move(XCurrent, YCurrent, XNew, YNew, board, turn, whiteKing, blackKing)

      break

  else:
    print("Try again...")
    continue
  
  turn = change_turn(turn)

print("Game over")