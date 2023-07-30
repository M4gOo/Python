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

