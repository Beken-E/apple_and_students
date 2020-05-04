"""
        N students take K apples and distribute them among each other evenly. The
        remaining the undivisible) 
        part remains in the basket. How many apples will
        each single student get? How many apples will remain in the basket?
        The program reads the numbers N and K. It should print the two answers for
        the questions above. 
"""


n = input("How many students here?")
k = input("How much apples in the basket?")

basket = int(k) % int(n) 
for_student = int(k) // int(n) 

print(f"Each student gets {for_student} apple, in basket remain {basket} apple") 


