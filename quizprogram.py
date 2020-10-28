cor = 0

print("What is the sin of 0?")
ans = int(input("Answer: "))
if(ans==0):
    print("Correct!")
    cor = cor + 1    
else:
    print("Wrong. You got", cor, "answers correct. Good luck next time!")
    exit()

print("What is the cos of 0?")
ans = int(input("Answer: "))
if(ans==1):
    print("Correct!")
    cor = cor + 1    
else:
    print("Wrong. You got", cor, "answers correct. Good luck next time!")
    exit()

print("You got", cor, "answers correct. Thanks for playing!")
