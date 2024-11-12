class A:

  def __init__(self,a):
    self.a = a
  def __lt__(self,other):
    if (self.a<other.a):
      return "ob1 is lesser than ob2"
    else:
      return "ob2 is lesser than ob1"
  def __eq__(self,other):
    if (self.a==other.a):
      return "Both are equal"
    else:
      return "None are equal"
ob1 = A(3)
ob2 = A(4)
print("Passed Value :",ob1.a,ob2.a)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print("Passed Value :",ob3.a,ob4.a)
print(ob3 == ob4)