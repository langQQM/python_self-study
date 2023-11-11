class Shape():
    def __init__(self, w, l) -> None:
        self.width=w
        self.len=l
    
    def print_size(self):
        print("""{} by {}
              """.format(self.width,self.len))

class Square(Shape):
    def area(self):
        return self.width*self.len

    def print_size(self):
        # return super().print_size()
        print("""I am {} by {}""".format(self.width, self.len))

a_square=Square(10,20)
a_square.print_size()
print(a_square.area())