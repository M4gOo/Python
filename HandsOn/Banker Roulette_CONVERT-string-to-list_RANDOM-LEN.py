
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


num_items = len(names)

random_choice = random.randint(0, num_items -1)

who_will_pay = names [random_choice]

print(f"{who_will_pay} is going to buy the meal today!")
