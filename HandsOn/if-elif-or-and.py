print("Welcome to the Love Calculator!")
name_1 = input("What is your name?\n").lower()
name_2 = input("What is their name?\n").lower()

t = name_1.count('t')
r = name_1.count('r')
u = name_1.count('u')
e = name_1.count('e')
l = name_2.count('l')
o = name_2.count('o')
v = name_2.count('v')
e2 = name_2.count('e')

score1 = str(t + r + u + e)
score2 = str(l + o + v + e2)

score = int(str(score1 + score2))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:     
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


========================================================================================================

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")



========================================================================================================

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
if size == "S":
    bill = 15
    pep = input("Do you want pepperoni? Y or N ")
    if pep == "Y":
        bill += 2
    extra_x = input("Do you want extra cheese? Y or N ")
    if extra_x == "Y":
        bill += 1
elif size == "M":
    bill = 20
    pep = input("Do you want pepperoni? Y or N ")
    if pep == "Y":
        bill += 3
    extra_x = input("Do you want extra cheese? Y or N ")
    if extra_x == "Y":
        bill += 1    
elif size == "L":
    bill = 25
    pep = input("Do you want pepperoni? Y or N ")
    if pep == "Y":
        bill += 3
    extra_x = input("Do you want extra cheese? Y or N ")
    if extra_x == "Y":
        bill += 1    
else:
    print("Type valid character")
    
print(f"Your final bill is: ${bill}")
