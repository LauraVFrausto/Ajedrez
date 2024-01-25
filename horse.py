from piece import Piece

class Horse(Piece):
  def __init__(self,color,x,y) :
      
    Piece.__init__(self,"h",color, x, y )

  def valid_moves( self, board):
    possible_moves=[]
    
    twos=[2,-2]
    ones=[1,-1]
    
    
    #two up/down one side
    
    for i in twos:
      for j in ones:
        if self.y+i<=7 and self.y+i>=0 and self.x+j>=0 and self.x+j<=7:
          if board[self.y+i][self.x+j]:
            if board[self.y+i][self.x+j].color != self.color:
              possible_moves.append((self.y+i, self.x+j))
          else:
            possible_moves.append((self.y+i, self.x+j))    

                
    for i in twos:
      for j in ones:
        if self.y+j<=7 and self.y+j>=0 and self.x+i>=0 and self.x+i<=7:
          if board[self.y+j][self.x+i]:
            if board[self.y+j][self.x+i].color != self.color:
              possible_moves.append((self.y+j, self.x+i))
          else:
            possible_moves.append((self.y+j, self.x+i))    
    return possible_moves