print("give me a string: ")
string=input()
L=len(string)
if L>3:
    print(string[0]+string[1]+string[L-2]+string[L-1])
else:
    print("you have to enter a string longer than 3 characters")