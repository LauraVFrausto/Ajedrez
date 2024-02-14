from piece import Piece

class Rook(Piece):
  def __init__(self,color,x,y) :
      
    Piece.__init__(self,"r",color, x, y )
    self.cont = 0
    
  def valid_moves( self, board):
    possible_moves=[]
    
    #right move
    new_x,new_y=self.x+1,self.y

    while new_x<=7:
        if  board[new_y][new_x] != None:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_x, new_y))

            break
                 
        possible_moves.append((new_y, new_x))
        new_x+=1
        
    #left move
    new_x,new_y=self.x-1,self.y
    
    while new_x >= 0:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                 
        possible_moves.append((new_y, new_x))
        new_x-=1
    
    #up move
    new_x,new_y=self.x,self.y+1
    
    while new_y <= 7:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                 
        possible_moves.append((new_y, new_x))
        new_y+=1
    
    #down move
    new_x,new_y=self.x,self.y-1
    
    while new_y >= 0:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                 
        possible_moves.append((new_y, new_x))
        new_y-=1
        
    return possible_moves