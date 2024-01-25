from piece import Piece

class Bishop(Piece):
  def __init__(self,color,x,y) :
      
    Piece.__init__(self,"b",color, x, y )

  def valid_moves( self, board):
      
    possible_moves=[]
    
    #cambios
    #up rigth move
    new_x,new_y = self.x+1,self.y+1
    while new_x<=7 and new_y<=7:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                 
        possible_moves.append((new_y, new_x))
        new_x+=1
        new_y+=1
        
    #up left move
    new_x,new_y = self.x-1,self.y+1
    while new_x >= 0 and new_y <= 7:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                    
        possible_moves.append((new_y, new_x))
        new_x-=1
        new_y+=1
    
    #down right move
    new_x,new_y = self.x+1,self.y-1
    while new_x <= 7 and new_y >= 0:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                    
        possible_moves.append((new_y, new_x))
        new_x+=1
        new_y-=1
    
    
    #down left move
    new_x,new_y = self.x-1,self.y-1
    while new_x >= 0 and new_y >= 0:
        if  board[new_y][new_x]:
            if board[new_y][new_x].color != self.color:
                possible_moves.append((new_y, new_x))
                
            break
                    
        possible_moves.append((new_y, new_x))
        new_x-=1
        new_y-=1
        
    return possible_moves