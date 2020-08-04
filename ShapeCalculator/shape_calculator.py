class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** .5)
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) +", height=" + str(self.height) + ")"

    def get_picture(self):

        if(self.width > 50 or self.height > 50):
            return "Too big for picture."

        output = ""
        for i in range(self.height):
            output += "*" * self.width 
            output += "\n"
        return output
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):

    def __init__(self, length):
        self.set_height(length)
        self.set_width(length)
    
    def set_side(self, length):
        self.set_height(length)
        self.set_width(length)
    
    def __str__(self):
        return "Square(side="+ str(self.width) + ")"
        
    

