class Parent():
    def __init__(self,last_name,eye_color):
        print('Parent Constructor Called')
        self.last_name=last_name
        self.eye_color=eye_color

    def show_info(self):
        print('Last Name:'+self.last_name)
        print('Eye Color:'+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print ('Child Constructor Called')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys=number_of_toys

    def show_info(self):
        print('Last Name:'+self.last_name)
        print('Eye Color:'+self.eye_color)
        print('Number Of Toys:'+str(self.number_of_toys))
        
       
billy_cyrus = Parent('Cyrus','blue')
billy_cyrus.show_info()

#print(billy_cyrus.last_name)

miley_cyrus = Child('Cyrus','Red',5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
