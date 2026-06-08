class Address:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode
    def displayAddress(self):
        
        return f"{self.street},{self.city}-{self.zipcode}"
    
class Student:
    def __init__(self,name,age,address):
        
        self.name=name
        self._age=age #making the age protected attributes;
        self.address=address
        self.courses=[]
        #property for age
    @property#control access to variables 
    def age(self):
        return self._age#we have taken age in our function
    
    @age.setter
    def age(self,value):
        if value>0 and value<100:
            self._age=value
        else:
            print("invalid age ! age must be in between 1 and 99")
    #method to add courses
    def addCourses(self,course):
        self.courses.append(course)
    def display(self):
        print("student Name:",self.name)
        print("age:",self.age)
        print("Adddress:",self.address.displayAddress())
        print("Courses:",self.courses)
        
        
class ScholarShipStudent(Student):
    
    def __init__(self,name,age,address,scholarShipAmount):
        super().__init__(name,age,address)
        self.scholarShipAmount=scholarShipAmount
        
        
    #overriding display()
    def display(self):
        super().display()
        print("scholarShip Amount:" ,self.scholarShipAmount)
        
        
#creating adddress object
addr=Address("Tezpur Universit","tezpur","784028")
addr2=Address("Tezpur Universit","tezpur","784028")

#create Scholar Ship student obh
s1=ScholarShipStudent("kaushal",22,addr,5000)
s2=ScholarShipStudent("Adity",21,addr2,3000)


#mutable behaviour : adding courses
s1.addCourses("Python")
s1.addCourses("Machine learning")
s1.addCourses("Advance Programming")
s2.addCourses("Python")
s2.addCourses("Machine learning")
s2.addCourses("Advance Programming")
 
 
 #property validation


 
 #display details
s1.display()
s2.display()




        
        
    
