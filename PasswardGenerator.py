import random
import string

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
p = a + b + c + d
print("------------------------------------------")
print("--------RANDOM PASSwARD GENERATOR---------")
print("------------------------------------------")
print()
p_len = int(input("Enter your passward length: ")) 
passward = ""
for i in range(0,p_len,+1):
    passward = passward + random.choice(p)

print()
print(f"Required Passward Length: {p_len}")
print(f"Passward: {passward}")