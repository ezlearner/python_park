class MyClass(object):
    def __init__(self,num):
         self.num=num

    def __eq__(self, other):
         if self.num == other.num:
             return True
         else:
             return False
    def __ne__(self, other):
         if self.num != other.num:
             return True
         else:
             return False

    def __gt__(self, other):
         if self.num > other.num:
             return True
         else:
             return False

    def __lt__(self, other):
         if self.num < other.num:
             return True
         else:
             return False

    def __gte__(self, other):
         if self.num >= other.num:
             return True
         else:
             return False

    def __lte__(self, other):
         if self.num <= other.num:
             return True
         else:
             return False
    def __str__(self):
         return  str(self.num)

    @staticmethod
    def stcMethod():
        print "call Static Method, not need to pass self parameter"

a=MyClass(5)
b=MyClass(5)
c=MyClass(7)

print a==b
print a == c

print a >= c
print a <= c
print a < c
print a > c
print a!=c

print a
print b
print c

c.stcMethod()
