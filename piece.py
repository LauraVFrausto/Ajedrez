class Piece:
    
    def __init__(self, tag, color, x, y):
        
        self.tag = tag
        self.color = color
        self.x = x
        self.y = y
    
    def print(self):
        
        if self.color=="white":
            print(self.tag)
            print("Color blanco")
        
        else:
            print(self.color)
            print("color negro")