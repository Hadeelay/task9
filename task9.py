#Question 1 ### class Rectangle
class Rectangle:
    # 1 Define : length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Question 1.1 ### Perimeter method
    def Perimeter(self):
        return 2 * (self.length + self.width)

    ### Area method
    def Area(self):
        return (self.length * self.width)

    #Question 1.2 ### Display method
    def Display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())


        #Question 2 ### class Parallelepipede
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    #  Volume method
    def volume(self):
        return (self.length * self.width * self.height)


My_Rectangle = Rectangle(8,6)
My_Rectangle.Display()
My_Parallelepipede = Parallelepipede(8,6,3)
print("The volume of MyParallelepipede is: ",My_Parallelepipede.volume())