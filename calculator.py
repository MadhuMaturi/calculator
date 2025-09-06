import math
class Calculator:
    def add(self,a,b):
        res=a+b
        print(res) 
    def sub(self,a,b):
        res=a-b
        print(res)
    def mul(self,a,b):
        res=a*b
        print(res)
    def div(self,a,b):
        if b!=0:
            res=a/b
            print(res)
        else:
            print("undefined")
class Scientific_Calculator(Calculator): 
    def sqrt(self,a):
        res=math.sqrt(a)
        print(res)
    def power(self,a,b):
        res=math.pow(a,b)
        print(res)
    def logarithm(self,a):
        if a<=0:
            print("Logaritmic is undefined for zero or undefined numbers")
        else:
            res=math.log(a)
            print(res)
    def cosine(self,a):
        res=math.cos(math.radians(a))
        print(res)
    def sine(self,a):
        res=math.sin(math.radians(a))
        print(res)
class Advance_Scientific_Calculator(Scientific_Calculator):
    def factorial(self,a):
        if a<0:
            print("Factorial is not defined for negative numbers")
        else:
            fact=1
            for i in range(2,a+1):
                fact=fact*i
            print(fact)
    def gcd(self,a,b):
        if a==0 or b==0:
            print("gcd is undefined for zero")
        else:
            result=1
            for i in range(1,min(a,b)+1):
                if a%i==0 and b%i==0:
                    result=i
            print(result)
    def lcm(self,a,b):
        if a==0 or b==0:
            print("lcm is undefined for zero")
        else:
            result=1
            for i in range(min(a,b),1+(a*b)):
                if i%a==0 and i%b==0:
                    result=i
                    break
            print(result)


while True:
   print("1.Arithmetic Calculator\n2.Scientific Calculator\n3.Advance Scientific Calculator\n")
   choice=int(input("Enter your Choice: "))
   if choice in[1,2,3]:
       if choice==1:
           gen_cal=Calculator()
           while True:
               print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
               ch=int(input("Enter your choice: "))
               if ch in [1,2,3,4]:
                   a=int(input("Enter First number: "))
                   b=int(input("Enter Second number: "))
                   if ch==1:
                       gen_cal.add(a,b)
                   elif ch==2:
                       gen_cal.sub(a, b)
                   elif ch==3:
                       gen_cal.mul(a,b)
                   elif ch==4:
                       gen_cal.div(a,b)
                   continue_as=input("Do you want to  use a General calculator(y/n): ")
                   if continue_as in['n','N']:
                       break
                   elif continue_as in ['y','Y']:
                       continue
                   else:
                       print("Please enter a valid choice")
               else:
                   print("Invalid choice")
       elif choice==2:
           scientific_cal=Scientific_Calculator()
           while True:
               print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square Root\n6.Power\n7.logarithm\n8.Cosine\n9.Sine\n")
               ch=int(input("Enter your choice: "))
               if ch in [1,2,3,4,5,6,7,8,9]:
                   a=int(input("Enter First number: "))
                   if ch==1:
                       b=int(input("Enter Second number: "))
                       scientific_cal.add(a,b)
                   elif ch==2:
                       b=int(input("Enter Second number: "))
                       scientific_cal.sub(a, b)
                   elif ch==3:
                       b=int(input("Enter Second number: "))
                       scientific_cal.mul(a,b)
                   elif ch==4:
                       b=int(input("Enter Second number: "))
                       scientific_cal.div(a,b)
                   elif ch==5:
                       scientific_cal.sqrt(a)
                   elif ch==6:
                       b=int(input("Enter power: "))
                       scientific_cal.power(a, b)
                   elif ch==7:
                       scientific_cal.logarithm(a)
                   elif ch==8:
                       scientific_cal.cosine(a)
                   elif ch==9:
                       scientific_cal.sine(a)
                   continue_as=input("Do you want to use a Scientific calculator(y/n): ")
                   if continue_as in['n','N']:
                       break
                   elif continue_as in ['y','Y']:
                       continue
                   else:
                       print("Please enter a valid choice")
               else:
                   print("Invalid choice")
       elif choice==3:
           advanced_scientific_cal=Advance_Scientific_Calculator()
           while True:
               print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square Root\n6.Power\n7.logarithm\n8.Cosine\n9.Sine\n10.Factorial\n11.Gcd\n12.Lcm\n")
               ch=int(input("Enter your choice: "))
               if ch in [1,2,3,4,5,6,7,8,9,10,11,12]:
                   a=int(input("Enter First number: "))
                   if ch==1:
                       b=int(input("Enter Second number: "))
                       advanced_scientific_cal.add(a,b)
                   elif ch==2:
                       b=int(input("Enter Second number: "))
                       advanced_scientific_cal.sub(a, b)
                   elif ch==3:
                       b=int(input("Enter Second number: "))
                       advanced_scientific_cal.mul(a,b)
                   elif ch==4:
                       b=int(input("Enter Second number: "))
                       advanced_scientific_cal.div(a,b)
                   elif ch==5:
                       advanced_scientific_cal.sqrt(a)
                   elif ch==6:
                       b=int(input("Enter power: "))
                       advanced_scientific_cal.power(a, b)
                   elif ch==7:
                       advanced_scientific_cal.logarithm(a)
                   elif ch==8:
                       advanced_scientific_cal.cosine(a)
                   elif ch==9:
                       advanced_scientific_cal.sine(a)
                   elif ch==10:
                       advanced_scientific_cal.factorial(a)
                   elif ch==11:
                       b=int(input("Enter second number: "))
                       advanced_scientific_cal.gcd(a,b)
                   elif ch==12:
                       b=int(input("Enter second number: "))
                       advanced_scientific_cal.lcm(a,b)
                   continue_as=input("Do you want to use an Advanced scientific calculator(y/n): ")
                   if continue_as in['n','N']:
                       break
                   elif continue_as in ['y','Y']:
                       continue
                   else:
                       print("Please enter a valid choice")
               else:
                   print("Invalid choice")
   continue_as=input("Do you want to continue (y/n): ")
   if continue_as in ['n','N']:
       break
   elif continue_as in['y','Y']:
       continue
   else:
       print("Invalid choice")
                