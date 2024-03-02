##Functions##

##Establish Menu##

def show_menu():
	print("Welcome to the multi-purpose calculator program! Please select from the following: ")
	print("To calculate the sum of some values you input, type 1.")
	print("To calculate the surface area of a rectangle, type 2.")
	print("To calculate the volume of a cuboid, type 3.")
	print("to find the max value out of a set of numbers, type 4.")
	print("To find the average of a set of numbers type 5.")
	print("To find the average of a set of numbers, AND to determine which number is closest to the average, type 6.")
	print("Type 0 to quit.")

##Establish sum functions, as the repl instructions specify, inputs are gathered within the function for this one.##
##Function asks how many values will be entered. Sets initial total to 0. For each value, it adds the value to the variable "total"
def sum_of_values():
	total=0
	print("How many numbers do you want to sum?")
	qty_values=int(input(">"))
	print("Enter number(s):")
	for x in range(0,qty_values,1):
		value=float(input(">"))
		total=total+value
	return total

##Establish rectangle calculator, function recieves two labeled arguments and returns their product##
def rectangle_area(l,w):
    a=l*w
    return a

##Establish cuboid calculator, function recieves three labeled arguments and returns their product##
def volume_cuboid(l,w,h):
	v=l*w*h
	return v

##Establish maximium finder. Function recieves one argument in the form of a list "a". For each item in the list, it checks if it is bigger than the last biggest value stored in the variable "max". The initial max value is set to 0.##
##The function returns the variable "max"
def find_max(a):
    max=0
    for item in a:
          if item>=max:
                max=item
    return max

##Establish average finder. Function recieves two arguments, one in the form of a list "a" which is established in the main calling routine and the other as the number of values entered in that list "b"##
##The function adds these values to a collection similar to the sum function, then divides by the number of values "b"
def average(a,b):
    collection=0
    for item in a:
        collection=item+collection
    average = collection/b
    return average

##This function recieves two arguments, one is again a list of values "a" and the other "b" is the average of the values passed from the main calling routine by calling the previous "average"##   
##This function finds the minimum "min" of a list of values##
##Each value is the absolute value "abs" of each value in list the user enters "a" minus the average passed in "i-b".##
##This second list is indexed in the same way as list "a" using "a,key=lambda i:"##
def closest_average(a,b):
    y=min(a,key=lambda i: abs(i-b))
    return y
    


##Lastly, this function allows the user to retry their selection until they make a vaid choice.##
##If an invalid choice is made, it makes the first conditional if statement true##
##It does this by making a giant function that sandwiches all of the menu input code##
##Could we still consider this "The main calling routine" or is that just the two lines of code at the bottom?##
##In the main calling routine, right after calling the "show_menu" function, the computer calls the tryagain function.##
##This initial call sets the argument to 0, and the program moves on to the menu input code##
##After checking to see if the input was 0-6, it hits the else statement at the bottom##
##This else statement is also a part of the "tryagain" definition##
##So, if you input anything other than 0-6, the function argument becomes "1" and sets the first if statement to true and moves on to the input code again##
##After you run a calculation, the same thing is allowed to happen, but with the menu shown again by setting the argument in "try_again" to "2"##
def tryagain(again):
    if again==1:
        print('Sorry that is not a valid selection. Try Again. ')
    elif again ==2:
        show_menu()

        
    choice = int(input(">"))    
##Sum code runs everything within the function, prints the sum##
    if choice==1:
        sum=sum_of_values()
        print(sum)
        #This is repeated in every choice. I could have made it a function but I'd already spent too much time on this...##
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)

##Rectangle area code. Collects a limited number of labeled inputs for the function's 2 arguments. Catches and prints the function's calculation.##
    elif choice==2:
        print("What are the dimensions of your rectangle?")
        length=float(input("Length > "))
        width=float(input("Width > "))
        area=rectangle_area(length,width)
        print(area,"square units")
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)

##Cuboid area code. Collects a limited number of labeled inputs for the function's 3 arguments. Catches and prints the function's calculation.##
    elif choice==3:
        print("What are the dimensions of your cuboid?")
        length=float(input("Length > "))
        width=float(input("Width > "))
        height=float(input("Height> "))
        volume=volume_cuboid(length,width,height)
        print(volume,"cubic units")
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)
##Max finder code. Collects as many inputs as the user requests and stores them in the list "numbers". ##
##Catches and prints the function's calculations.##
    elif choice==4:
        print("How many numbers do you have? Tell me and I'll find the maximum.")
        n=int(input(">"))
        numbers=[]
        print("Enter number(s):")
        for x in range (0,n,1):
            number=float(input(">"))
            numbers.append(number)
        print(f"The maximum is {find_max(numbers)}")
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)

##Average code. Collects as many inputs as the user requests and stores them in the list "numbers". ##
##Catches and prints the function's calculations##            
    elif choice==5:
        print("How many numbers do you have? Tell me and I'll find the average.")
        n=int(input(">"))
        numbers=[]
        print("Enter number(s):")
        for x in range (0,n,1):
            number=float(input(">"))
            numbers.append(number)
        print(f"The average is {average(numbers,n)} ")
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)

##Closest to average code. Collects as many inputs as the user requests and stores them in the list "numbers". ##
##Catches and prints the average, a list of the values the user provides as input, and which value is closest to that average.##        
    elif choice==6:
        print("How many numbers do you have? Tell me and I'll find the average and which is closest.")
        n=int(input(">"))
        numbers=[]
        print("Enter number(s):")
        for x in range (0,n,1):
            number=float(input(">"))
            numbers.append(number)
        print(f"The numbers you entered are: ")
        print(numbers)
        avg=average(numbers,n)
        print(f"The average is {avg}")
        print(f"The closest to the average is", closest_average(numbers,avg))
        print("Enter any value to return to the main menu.")
        more=input(">")
        if more:
                tryagain(2)
##Quit##
    elif choice==0:
        print("Goodbye")

##User enters something not on the menu.##
    else:
        return tryagain(1) 
          
##This is the very fist step the computer takes after establishing all of the function definitions.##
show_menu()
tryagain(0)
