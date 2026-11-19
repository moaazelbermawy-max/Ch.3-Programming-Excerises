#Moaaz Elbermawy
#Ch. 3 Programming Excerises
#11/19/26
import turtle
   

#1
userDay = int(input("What day is it? (1-7)"))
if userDay == 1:
    print("Monday")
elif userDay == 2:
    print("Tuesday")
elif userDay == 3:
    print("Wednesday")
elif userDay == 4:
    print("Thursday")
elif userDay == 5:
    print("Friday")
elif userDay == 6:
    print("Saturday")
elif userDay == 7:
    print("Sunday")
else:
    print("User Input Invalid")
#2
#Collect user input for rectangles
rectLength1 = float(input("What is the length of the rectangle?"))
rectWidth1 = float(input("What is the width of the rectangle?"))
rectArea1 = rectLength1 * rectWidth1
rectLength2 = float(input("What is the length of the second rectangle?"))
rectWidth2 = float(input("What is the width of the second rectangle?"))
rectArea2 = rectLength2 * rectWidth2
#Display Results
if rectArea1 > rectArea2:
    print("Rectangle 1 has a greater area")
elif rectArea1 < rectArea2:
    print("Rectangle 2 has a greater area")
else:
    print("They both have the same area.")

#3
userAge = int(input("Enter your age"))
if userAge <= 1:
    print('You are an infant')
elif userAge > 1 and userAge < 13:
    print('You are a child')
elif userAge >= 13 and userAge < 20:
    print('You are a teenager')
else:
    print('You are an adult')


#4
#Convert 1-10 into a Roman Numeral
romanNum = int(input('Enter a number 1-10: '))
if romanNum < 1 or romanNum > 10:
    print('Error: Number out of range (1-10). Please try again.')
elif romanNum == 1:
    print('I')
elif romanNum == 2:
    print('II')
elif romanNum == 3:
    print('III')
elif romanNum == 4:
    print('IV')
elif romanNum == 5:
    print('V')
elif romanNum == 6:
    print('VI')
elif romanNum == 7:
    print('VII')
elif romanNum == 8:
    print('VIII')
elif romanNum == 9:
    print('IX')
elif romanNum == 10:
    print('X')

#5
mass = float(input("Enter the objects mass in kilos: "))

weight = mass * 9.8

print(f'Weight: {weight:.2f} newtons')
if weight > 500:
    print('The object is too heavy...')
elif weight < 100:
    print('The object is too light...')


#6
month = int(input("Enter the month in numeric form: "))
day = int(input('Enter the day: '))
year = int(input('Enter the two digit year: '))

#Checks if month = year
if month*day == year:
    print("The date is magic")
else:
    print("The date is not magic")

#7
color1 = input("Enter the first primary color (lowercase):")
color2 = input("Enter the second primary color (lowercase):")

if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
    print('Purple')
elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
    print('Orange')
elif (color1 == 'yellow' and color2 == 'blue') or (color1 == 'blue' and color2 == 'yellow'):
    print('Green')
else:
    print('Error: You must enter primary colors.')

#8
people = int(input('How many people are coming?'))
dogs_per_person=int(input('Enter the number of hot dogs per person:'))

tD = people * dogs_per_person

#Round up
dogPacks=(tD + 9)//10
bunsPacks=(tD + 7)//8

total_dogs_purchased = dogPacks*10
total_buns_purchased = bunsPacks*8

dogsLeft = total_dogs_purchased - tD
bunsLeft = total_buns_purchased - tD

print(f'Minimum packages of hot dogs required: {dogPacks}')
print(f'Minimum packages of hot dog buns required: {bunsPacks}')
print(f'Hot dogs left over: {dogsLeft}')
print(f'Hot dog buns left over: {bunsLeft}')


#9
pocket = int(input('Enter a pocket 0-36: '))

if pocket < 0 or pocket > 36:
    print('Error: Must enter a number between 0-36')
elif pocket == 0:
    print("Green")
#Even pockets 
elif (1 <= pocket <= 10 or 19 <= pocket <= 28) and pocket % 2 == 0:
    print('Black')
elif (11 <= pocket <= 18 or 29 <= pocket <= 36) and pocket % 2 != 0:
    print('Black')
else:
    print('Red')

#10
pennies = int(input('Enter number of pennies: '))
nickels = int(input('Enter number of nickels: '))
dimes = int(input('Enter number of dimes: '))
quarters = int(input('Enter number of quarters: '))

totalCents = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)
totalValue = totalCents / 100

if totalCents == 100:
    print('You won the game!!!!!')
elif totalCents > 100:
    print(f'Sorry you lost, that was more than one dollar. Your total value was ${totalValue:.2f}.')
else:
    print(f'Sorry you lost, that was less than one dollar. Your total value was ${totalValue:.2f}.')

#11
# Giving points based on books
books = int(input('Enter number of books purchased: '))

if books >= 8:
    points = 60
elif books >= 6:
    points = 30
elif books >= 4:
    points = 15
elif books >= 2:
    points = 5
elif books == 0:
    points = 0
else:
    points = 0
print(f'Points: {points}')

#12
#Collecting input
packages = int(input('Number of packages purchased: '))

retailPrice = 99.0
#Checking price
if packages >= 100:
    discountRate = 0.40
elif packages >= 50:
    discountRate = 0.30
elif packages >= 20:
    discountRate = 0.20
elif packages >= 10:
    discountRate = 0.10
else:
    discountRate = 0.00

subtotal = packages * retailPrice
discountAmount = subtotal * discountRate
totalAmount = subtotal - discountAmount

print(f'Discount amount: ${discountAmount:.2f}')
print(f'Total amount after discount: ${totalAmount:.2f}')

#13
weight = float(input("Enter the weight of the package: "))

#Shipping rate based on weight
if weight <= 2:
    rate = 1.50
elif weight <= 6:
    rate = 3.00
elif weight <= 10:
    rate = 4.00
else:
    rate = 4.75

shippingCharges = weight * rate

print(f'Shipping Charges: ${shippingCharges:.2f}')


#14
totalSecs = int(input('Enter a number of seconds: '))

#Using floor divison 
if totalSecs >= 86400:
    days = totalSecs // 86400
    leftover = totalSecs % 86400
    hours = leftover // 3600
    leftover = leftover % 3600
    minutes = leftover // 60
    seconds = leftover % 60
    print(f'{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds. ')
elif totalSecs >= 3600:
    hours = totalSecs // 3600
    leftover = totalSecs % 3600
    minutes = leftover // 60
    seconds = leftover % 60
    print(f'{hours} hours, {minutes} minutes, and {seconds} seconds. ')
elif totalSecs >= 60:
    minutes = totalSecs // 60
    seconds = totalSecs % 60
    print(f'{minutes} minutes, and {seconds} seconds. ')
else:
    print(f'{totalSecs} seconds. ')

#15
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    days = 29
else:
    days = 28

print(f'In {year} February has {days} days. ')


#16
print('Reboot the computer and try to connect.')
answer = input('Did that fix the problem? ')

#Keeps going
if answer != 'yes':
    print('Reboot the router and try to connect.')
    answer = input('Did that fix the problem? ')
    if answer != 'yes':
        print('Make sure the cables between the router and modem are plugged in firmly.')
        answer = input('Did that fix the problem? ')
        if answer != 'yes':
            print('Move the router to a new location.')
            answer = input('Did that fix the problem? ')
            if answer != 'yes':
                print('Get a new router.')
#17
#Gathering inputs
veggie = input('Is anyone in your party a vegetarian? ').lower()
vegan = input('Is anyone in your party a vegan? ').lower()
gluten = input('Is anyone in your party gluten-free? ').lower()
#Checking restaurants
print('Here are your restaurant choices:')
if veggie == 'no' and vegan == 'no' and gluten == 'no':
    print("   Joe's Gourmet Burgers")
if vegan == 'no':
    print("   Main Street Pizza Company")
print("   Corner Cafe")
if vegan == 'no' and gluten == 'no':
    print("   Mama's Fine Italian")
print("   The Chef's Kitchen")
#18
# Hit the Target Game
import turtle
   
# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction
   
# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
   
# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
   
# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
   
# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1−10): "))
   
# Calculate the distance.
distance = force * FORCE_FACTOR
 
# Set the heading.
turtle.setheading(angle)
 
# Launch the projectile.
turtle.pendown()
turtle.forward(distance)
 
# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')
        if (angle < 60):
            print('Try increasing the angle.')
        elif(angle>60):
            print('Try decreasing the angle.')
        if (force<9):
            print('Try increasing the force.')
        elif(force>9.5):
            print('Try decreasing the force.')


