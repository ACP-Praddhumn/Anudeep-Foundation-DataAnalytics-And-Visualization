# def show():
#     print("outside class show function")
# class Student :
#     name = "abc"
#     age = 0
#     def study(self):
#         show()
#         self.show()
#         print("Study 9 hours")
#     def show(self):
#         print("inside class show function")
    
# # Student().study()
# obj = Student()
# obj.study()
 


# class A:
#     name = "Anant"
#     def show(self):
#         print("This is a A class show method")

# class B(A):
#     pass
# obj = B()
# obj.show()



#MULTILEVEL INHERITANCE
# class A:
#     name = "Anant"
#     def show(self):
#         print("This is a A class show method")

# class B(A):
#     def demo(self):
#         print("This is a demo method of class B")
# class C(B):
#     pass
# obj = C()
# obj.show()
# obj.demo()



#HIERARCHICHAL INHERITANCE
# class A:
#     name = "Anant"
#     def show(self):
#         print("This is a A class show method")

# class B(A):
#     def demo(self):
#         print("This is a demo method of class B")
# class C(A):
#     pass
# obj = C()
# obj.show()
# obj.demo()



#MULTIPLE INHERITANCE
# class A:
#     name = "Anant"
#     def show(self):
#         print("This is a A class show method")

# class B:
#     def demo(self):
#         print("This is a demo method of class B")
# class C(A,B):
#     pass
# obj = C()
# obj.show()
# obj.demo()


#HYBRID INHERITANCE
# class A:
#     name = "Anant"
#     def show(self):
#         print("This is a A class show method")

# class B(A):
#     def demo(self):
#         print("This is a demo method of class B")
        
# class C(A):
#     def pro(self):
#         print("Pro method from class C")
        
# class D(B,C):
#     def demo(self):
#         print(self.name)
#         print(A.name)
#         print(super().name)
#     pass
# obj = D()
# obj.show()
# obj.demo()
# obj.pro()
# def setData(id,name,age):
#     print(f"Name is : {name}")
#     print(f"Name is : {age}")



#METHOD OVERLOADING IS NOT POSSIBLE IN PYTHON (NEW METHOD OVERRIDES THE FIRST ONE AND FIRST DISAPPERS)

# def setData(name,age):
#     print(f"Name is : {name}")
#     print(f"Name is : {age}")

# # second setData() method will override the first one and existence of first one will disappear

# setData("Sanjay",39)
# setData(102,"Anant",21)



# Polymorphism (Method Overriding)
# class Parent:
#     def house(self):
#         print("This is parent house")

# class child(Parent):
#     def show(self):
#         print("This is show function")
#     def house(self):
#         print("This is child house")

# obj = child()
# obj.house()


# METHOD OVERRIDING
# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#     def flight(self):
#         print("Most of the birds can fly but some can not.")

# class sparrow(Bird):
#     def flight(self):
#         print("I can fly")
# class ostrich(Bird):
#     def flight(self):
#         print("I can not fly")

# obj1 = sparrow()
# obj1.flight()
# obj2 = ostrich()
# obj2.flight()


# ENCAPSULATION

# class A:
#     name = "Anant"
#     __age = 12         #private variable(underscore)
#     def demo(self):
#         print("The name is ",self.name)
#     def getAge(self):                         #use getter method to get value (age is binded with this method)
#         return self.__age

# class B(A):
#     pass

# obj = B()
# print(obj.name)

# print(obj.getAge())
# print(obj.__age)



