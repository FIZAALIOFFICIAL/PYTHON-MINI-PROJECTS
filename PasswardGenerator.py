import random
import string

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = string.punctuation
p = a + b + c + d
p_len = int(input("Enter your passward length: ")) 
passward = ""
for i in range(0,p_len,+1):
    passward = passward + random.choice(p)

print(f"Your random passward is: {passward}")