class Calculator:
    
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        self.selection=0
        self.operationSelection()
    def getNumber1(self):
       return self.sayi1
   
    def getNumber2(self):
       return self.sayi2
   
    
    def sum(self):
       sum=0
       sum=self.sayi1+self.sayi2
       print("Sum value------> "+str(sum))
   
    def subtraction (self):
        subtraction=self.sayi1-self.sayi2
        print("subtraction value------> "+str(subtraction))

    def multiplication(self):
        multiplication=self.sayi1*self.sayi2
        print("multiplication value------> "+str(multiplication))

    
    def division (self):
        if(self.sayi2!=0):
            division=self.sayi1/self.sayi2
            print("division value------> "+str(division))
        else:
            print("Error: Cannot divide by zero")

    
    
    def operationSelection(self):
        
        print("Pls select that want to do process")
        
        print("1----->sum\n2----->subtraction\n3----->multiplication\n4----->division")
        
        self.selection=int(input())
        
        if(self.selection==1):
            self.sum()
        elif (self.selection==2):
            self.subtraction()
        elif (self.selection==3):
            self.multiplication()
        elif (self.selection==4):
            self.division()
print("pls give a number ")

sayi1 = float(input())

print("pls give another number ")

sayi2 = float(input())
 
        
c1 = Calculator(sayi1, sayi2)
