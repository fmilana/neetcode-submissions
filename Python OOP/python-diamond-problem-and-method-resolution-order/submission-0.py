class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("C")

class C(A):
    def print_method(self) -> None:
        print("B")

class D(C, B): 
    pass


# Do not change the code below
d = D()
d.print_method()
