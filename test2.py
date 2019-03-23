
#z = "1234567890"


#l = [1,2,3,4,5,6,7,8,9]


#for i in range(len(l)):
 #   print (l[i])
  #  if l[i] % 2 == 1:
   #   l[i] = (l[i]+1)

#print(l)


#while True:
#    x = input("Enter number: ")
 #   try:
  #      num = float(x)
   # except ValueError:
    #    pass
    #else:
     #   print("It's a number")
      #  break


#def repeat(s, exclaim):
    #result=s * 3
   # if exclaim:
  #      result=result+"!!!"
 #   return result

#r=repeat("wow", False)

#print(r)


#def pifagor(a,b):
 #   c=(a**2 + b**2)**(1/2)
  #  return (c)

#r=pifagor(1, 2)
#print(r)




#l1 = ['ddd', 'fffff', 'lllll','2222','123']

#n=0
#for element in l1:
 #    if len(element)%2 == 1:
  #       n+=1
#print(n)

#dict1={1:"dddd", 33:"ddfefew", 335:4567}
#print(dict1)
#for key in dict1:
 #print(key, ":", dict1[key])


#def func1 (*s):
 #    return s

#a=func1(1, 4, 6 )


#def funk1(**qwargs):
 #   return qwargs

#s = funk1(a =  1, b = 4, nm = 6, ff = 'srtr')
#print(s)

#l = ['sedf', 'xfgsfd', 'dffsdf']

#print(*l, sep='\n')

#names = ['RRRRRRR', 'ffffff', 'dddd']
#name = [name.title() for name in names if name.isalpha()]

#print(name)





class A:
    def __init__(self, name =""):
        self.name = name

    @classmethod
    def method(cls):
        cls.my_list = []

A.method()
print(A.my_list)


