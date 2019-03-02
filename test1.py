#print('Some legend try to run')


class Person:
  #  def printer_self(self):
   #     print(self)

    #def set_name(self, x):
     #   self.name = x

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = int(age)
    #def __str__(self):
   #     return f"Person object with name={self.name} and surname={self.surname}"
    def full_name(self):
        return f"{self.name} {self.surname}"
    def get_older(self, years=1):
        return f"Vasja get older and now is {self.age + years}"


if __name__=="__main__":
    p1 = Person("Vasja",'Vasin','55')

 #   p2 = Person("Vovan" "Vovochkin" "55")
    print (p1.get_older(5))
    print(p1.full_name())
    print(p1.surname)
 #   print(p2.name)


def distance(x1,y1,x2,y2):
    a = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return(a)


