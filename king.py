#include "Rey.h"
from piece import Piece

class King(Piece):
  def __init__(self,color,x,y) :
      
    Piece.__init__(self,"k",color, x, y )
    self.cont=0

  def valid_moves( self, board):
      possible_moves=[]
      
      #right moves
      if self.x+1<=7:
            
          if self.y-1>=0 and (board[self.y-1][self.x+1] == None  or board[self.y-1][self.x+1].color != self.color) and not self.check(board,self.x+1, self.y-1):
              possible_moves.append((self.x+1, self.y-1))
            
            #center
          if self.y<=7 and (board[self.y][self.x+1] == None  or board[self.y][self.x+1].color != self.color) and not self.check(board,self.x+1, self.y):
              possible_moves.append((self.x+1, self.y))
            
            #down
          if self.y+1<=7 and (board[self.y+1][self.x+1] == None  or board[self.y+1][self.x+1].color != self.color) and not self.check(board,self.x+1, self.y+1):
              possible_moves.append((self.x+1, self.y+1))
    
        #left moves 
      if self.x-1>=0:
            #up
          if self.y-1>=0 and (board[self.y-1][self.x-1] == None  or board[self.y-1][self.x-1].color != self.color) and not self.check(board,self.x-1, self.y-1):
              possible_moves.append((self.x+1, self.y-1))
              
          #center
          if self.y<=7 and (board[self.y][self.x-1] == None  or board[self.y][self.x-1].color != self.color) and not self.check(board,self.x-1, self.y):
              possible_moves.append((self.x+1, self.y))
            
          #down
          if self.y+1<=7 and (board[self.y+1][self.x-1] == None  or board[self.y+1][self.x-1].color != self.color) and not self.check(board,self.x-1, self.y+1):
              possible_moves.append((self.x+1, self.y+1))
            
        #up move
      if self.y-1>=0 and (board[self.y-1][self.x] == None  or board[self.y-1][self.x].color != self.color) and not self.check(board,self.x, self.y-1):
          possible_moves.append((self.x,self.y-1))
        
        #down move

      if self.y+1<=7 and (board[self.y+1][self.x] == None  or board[self.y+1][self.x].color != self.color) and not self.check(board,self.x, self.y+1):
          possible_moves.append((self.x, self.y+1))
          
      #Castle
      if self.color=="white":
      
    
        if (board [self.y][self.x].cont == 0 and board[7][-1].cont == 0 and board[7][-1].tag=="r" and 
            not self.check(board,self.x , self.y) and not self.check(board,self.x +1, self.y) and not self.check(board,self.x +2, self.y) and 
            not board[self.y][self.x+1] and not board[self.y][self.x+2] ):
            
          possible_moves.append(self.x+2,self.y)
      
      #Long castle
        if (board [self.y][self.x].cont == 0 and board[7][0].cont == 0 and board[7][0].tag=="r" and 
            not self.check(board,self.x , self.y) and not self.check(board,self.x -1, self.y) and not self.check(board,self.x - 2, self.y) and 
            not board[self.y][self.x-1] and not board[self.y][self.x-2] ):
            
          possible_moves.append(self.x-2,self.y)
      
      else:
        
        if (board [self.y][self.x].cont == 0 and board[0][-1].cont == 0 and board[7][-1].tag=="r" and 
            not self.check(board,self.x , self.y) and not self.check(board,self.x +1, self.y) and not self.check(board,self.x +2, self.y) and 
            not board[self.y][self.x+1] and not board[self.y][self.x+2] ):
            
          possible_moves.append(self.x+2,self.y)
      
      #Long castle
        if (board [self.y][self.x].cont == 0 and board[0][0].cont == 0 and board[0][0].tag=="r" and 
            not self.check(board,self.x , self.y) and not self.check(board,self.x -1, self.y) and not self.check(board,self.x - 2, self.y) and 
            not board[self.y][self.x-1] and not board[self.y][self.x-2] ):
            
          possible_moves.append(self.x-2,self.y)
   
   
            
  def check(self,board, x= None,  y=None):
    if x is None:
      x=self.x
    if y is None:
      y=self.y
    
    #Check rooks and queen attack´s left 
    new_x = x-1
    new_y = y
    
    while(new_x>=0):
      #Empty
      if(board[new_y][new_x]==None):
          new_x-=1
            
        #Non empty   
      else:
        if (board[new_y][new_x].tag=="r" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color :
            return True
        break
         
    #Check rooks and queen attack´s right           
    new_x = x+1
        
    while(new_x<=7):
      #Empty
      if(board[new_y][new_x]==None):
        new_x+=1
                
      #Non empty 
      else:
        if (board[new_y][new_x].tag=="r" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color :
          return True
        break
        
    #Check rooks and queen attack´s up
    
    new_x = x
    new_y = y - 1
    
    while(new_y>=0):
      #Empty
      if(board[new_y][new_x]==None):
        new_y-=1
            
      #Non empty   
      else:
        if (board[new_y][new_x].tag=="r" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color :
          return True
        break
                    
    new_y = y + 1
    while(new_y <= 7):
      
      #Empty
      if(board[new_y][new_x]==None):
        new_y+=1
                
      #Non empty 
      else:
        if (board[new_y][new_x].tag=="r" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color :
          return True
        break              
    
    #Check if a bishop or a queen is attacking
    
    #down right move
    new_x, new_y = x + 1, y + 1
    
    while new_x<=7 and new_y<=7:
      if board[new_y][new_x]==None:
        new_x+=1
        new_y+=1
      
      else:
        if (board[new_y][new_x].tag=="b" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color:
          return True
              
                
        break
        
    #down left move
    new_x, new_y = x - 1, y + 1
    while new_x>=0 and new_y<=7:
      if board[new_y][new_x]==None:
        new_x-=1
        new_y+=1
      
      else:
        if (board[new_y][new_x].tag=="b" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color:
          return True
                     
        break
    
    #up right move
    new_x, new_y = x + 1, y - 1
    while new_x<=7 and new_y>=0:
      if board[new_y][new_x]==None:
        new_x+=1
        new_y-=1
      
      else:
        if (board[new_y][new_x].tag=="b" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color:
          return True
                     
        break
    
    
    #up left move
    new_x, new_y = x - 1, y - 1
    while new_x>=0 and new_y>=0:
      if board[new_y][new_x]==None:
        new_x-=1
        new_y-=1
      
      else:
        if (board[new_y][new_x].tag=="b" or board[new_y][new_x].tag=="q") and self.color!=board[new_y][new_x].color:
          return True
                     
        break
      
    twos=[2,-2]
    ones=[1,-1]
    
    
    #two up/down one side
    #horse attack
    
    for i in twos:
        for j in ones:
          if self.y+i<=7 and self.y+i>=0 and self.x+i>=0 and self.x+i<=7:
            if board[self.y+i][self.x+j]:
              if board[self.y+i][self.x+j].color != self.color and board[self.y+i][self.x+j].tag=="h": # Checar
                return True
                
    for i in twos:
        for j in ones:
          if self.y+i<=7 and self.y+i>=0 and self.x+i>=0 and self.x+i<=7:
            if board[self.y+i][self.x+j]:
              if board[self.y+j][self.x+i].color != self.color and board[self.y+i][self.x+j].tag=="h": #Checa
                return True
  
  
            
