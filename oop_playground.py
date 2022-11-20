class Book:
    # init to initialise - defines class, attributes?
    def __init__(self, title, author, pages, current_page, boolean):
        self.title = title
        self.author = author 
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1 #giving it a value as a class itself??? dont always need the brackets like (self)
        self.boolean = True #for the turn back and forward
        self.boolean = boolean 
        not good practice to 


    #is the above the blueprint?    

    def bookmark_page(self): #method
            self.bookmark = self.current_page

    def turn_page(self):
        self.current_page += 1

    def turn_back_page(self):
        self.current_page -= 1    

    def __len__(self):
        return self.pages    

    def __string__(self): #functions use double __
        return f"Title: {self.title}, Author: {self.author}"


#underscores are class related functions, but the underscores are like behaviours for your class        

my_book = Book("A great book", "me", 198, 1,) #because we've said above that we need - title and author 
print(my_book)
#Tite: A great book, Author:me 

# instance?

# So far have only given it two attributes - title and author
# We're going to give it pages and we want to know the current page 

my_book.bookmark_page()
print(my_book.bookmark)
my_book.turn_page()
my_book.bookmark_page()
print(my_book.bookmark)
my_book.turn_back_page()
my_book.bookmark_page()
print(my_book.bookmark)
# will print 1 - 2 - 1 


#if its got the brackets - its the method its printing
#self - refers to the instance of the object (my_book) - need to initialise it starting with self so it knows what object its referring to 

#w
#challenge - create method that allows you to turn back a page 
# second challenge - amend existing turn page method to turn back or forth - boolean - set to true or false - eg true, turn page forward, false is backwards 

if my_book.boolean:
    my_book.turn_page()
    my_book.bookmark_page()
    print(my_book)
else 
# CRISTIS CODE
# class Book:

#   def __init__(self, title, author, pages, current_page, boolean):
#     self.title = title
#     self.author = author
#     self.pages = pages
#     self.current_page = current_page
#     self.bookmark = 1
#     self.boolean = boolean

#   def bookmark_page(self):
#     self.bookmark = self.current_page

#   def turn_page(self):
#     self.current_page += 1

#   def turn_page_back(self):
#     self.current_page -= 1

#   def __str__(self):
#     return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

#   def __len__(self):
#     return self.pages

# my_book = Book("A great book", "me", 198, 1, False)
# print(my_book)

# my_book.bookmark_page()
# print(my_book.bookmark)
# my_book.turn_page()
# my_book.bookmark_page()
# print(my_book.bookmark)

# if my_book.boolean:
#   my_book.turn_page()
#   my_book.bookmark_page()
#   print(my_book.bookmark)
# else:
#   my_book.turn_page_back()
#   my_book.bookmark_page()
#   print(my_book.bookmark)



--------------------
create class called employee and iniialise object again 

class Employee: 

    def __init__(self, name, saary, phone_number, start_date):
    # everytime we create an object, we need to set these parameters below
        self.name = name

    #create method to get employee details 

    #create method to get contact details from emplyee 


# creating objects for this class 

# instance of a class below - employee 1


#another instance of a class - emplyee 2 


class Employee:

  def __init__(self, name, salary, phone_number, start_date):
    self.name = name
    self.salary = salary
    self.start_date = start_date
    self.phone_number = phone_number

  def get_employment_details(self):
    return (self.name, self.salary, self.start_date)

  def get_contact_details(self):
    return (self.name, self.phone_number)

employee_1 = Employee("Fran", 78000, "12345678", "1st June 2020")
print(employee_1.get_employment_details())

employee_2 = Employee("Ben", 2000000, "09876543", "1st January 2015")
print(employee_2.get_contact_details())














