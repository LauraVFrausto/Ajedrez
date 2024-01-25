from piece import Piece

class Pawn(Piece):
  def __init__(self,color,x,y) :
    
    Piece.__init__(self,"p",color, x, y )
    self.cont=0
    self.enPassant= False
    
  def valid_moves( self, board):
    possible_moves=[]
    dir = 1 # Direction

    if self.color == "White":
       dir = -1

    #Two steps in the first move
    #Revisar direccion de avance de peon
    if self.cont==0 and not board[self.y+dir][self.x] and not board[self.y+(2*dir)][self.x] :
        possible_moves.append((self.y+(2*dir), self.x))
    
    if not board[self.y+dir][self.x]:
        possible_moves.append((self.y+dir, self.x))
    
    #cuidado en comer en direccion adecuada
    if board[self.y+dir][self.x+1]:
        if board[self.y+dir][self.x+1].color != self.color:
            possible_moves.append((self.y+dir, self.x+1))
        
    if board[self.y+dir][self.x-1]: 
        if board[self.y+dir][self.x-1].color != self.color:
            possible_moves.append((self.y+dir, self.x-1)) 
    
    #Comida de paso
    if board[self.y][self.x+1] and board[self.y][self.x+1].color != self.color and board[self.y][self.x+1].tag == "p" and board[self.y][self.x+1].enPassant:
        possible_moves.append((self.y+1, self.x+1))
    
    if board[self.y][self.x-1] and board[self.y][self.x-1].color != self.color and board[self.y][self.x-1].tag == "p" and board[self.y][self.x-1].enPassant:
        possible_moves.append((self.y+1, self.x-1))
    
    
                
    return possible_moves