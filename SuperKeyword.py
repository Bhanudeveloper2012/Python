class A:
    def test1(self):
        print("This was printing from the class A")

class B(A):
    def test1(self):
        print("This was printing from the class B")
        super().test1()

class C(A):
    def test1(self):
        print("This was printing from the class C")
        super().test1()

class D(B,C):
    def test2(self):
        print("This was printing from the class D")
        

obj=D()
obj.test1()
