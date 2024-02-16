# class Circle:
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius*self.radius
          
# Area_of_Circle = Circle(3)
# print("Area of Circle:", Area_of_Circle.area())

# #######################################################################################
# class Book:
#     def __init__(self, title,author,page,isbn):
#         self.title=title
#         self.author=author
#         self.page=page
#         self.isbn=isbn

#     def display_info(self):
#         return ( "The title of book is " + (self.title) + " and book's author is " + (self.author) + "." + " It has pages of " + str(self.page) + "." + " The ISBN number is " +  str(self.isbn)+ ".")
    
# Book_Info = Book("Python","Uttam",384,1234567890)
# print(Book_Info.display_info())
######################################################################################

class Car:
    def __init__(self, make, model, year) -> None:
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        return ("Car make is " + self.make + ".\n" + "Car model is " + self.model + ".\n"+"Car's year is " + str(self.year) + ".")
    
car = Car("Ford","Mustang",2024)
print(car.display_info())
print("#########################################################\n")

##########################################################################################################
#Car is a parent class and it inheritance by electric car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size) -> None:
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        return (super().display_info()+ "\nAnd it takes battey_size of " + str(self.battery_size))
    
electricCar = ElectricCar("Tesla", "Model S", 2024, 850)
print(electricCar.display_info())

#     def display_info(self):
#         return super().display_info()
    
# electricCar = ElectricCar("Ford","Hummer",2024)
# print(electricCar.display_info())
        