print(" _______")
print("|   __  |                             ")
print("|  |__| |\            /\            /     |")
print("|_______| \          /  \          /      |")
print("|          \        /    \        /       |")
print("|           \      /      \      / _______|")
print("|            \    /        \    / |  __   |")
print("|             \  /          \  /  | |__|  |")
print("|              \/            \/   |_______|")
print("                                           by issam")
import random
import string
pl=int(input("length of pwd"))
u=string.ascii_uppercase
l=string.ascii_lowercase
d=string.digits
s=string.punctuation
p=random.choice(u)+random.choice(l)+random.choice(d)+random.choice(s)
for i in range(pl-4):
  p=p+random.choice(u+l+d+s)
print(p)