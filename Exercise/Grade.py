score=int(input("Enter your Score :"))

if (score>=80 and score<=100):
    print("The Score is :Grade A")
elif(score>=75 and score <=79):
    print("The Score is :Grade B+")
elif(score>=70 and score<= 74):
    print("The Score is :Grade B")
elif(score>=65 and score<=69):
    print("The Score is :Grade C+")
elif(score>=60 and score<=64):
    print("The Score is :Grade C")
elif(score>=55 and score<=59):
    print("The Score is :Grade D+")
elif(score>=50 and score<=54):
    print("The Score is :Grade D")
elif(score>=0 and score<=49):
    print("The Score is : Grade F")
else:
    print("The Score is :NO Grade")