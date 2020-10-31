def my_question(questions,answers):
    cor = 0
    print(questions)
    ans = int(input("Answers: "))
    if ans == answers:
        print('correct')
        cor=cor+1
    
    else:
        print("Wrong,you have got",cor,"correct answers")
    
    
question1 = ("What is the value of sin 0?")
answer = 0

my_question(question1, answer)
print("You got", cor, "answers correct. Thanks for playing!")


