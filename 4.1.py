marks = int(input("Enter marks: "))
if (marks in range(0,25)):
       print ("Your grade is F")
elif (marks in range(25,45)):
       print ("Your grade is E")
elif (marks in range(45,50)):
       print ("your grade is D")
elif (marks in range(50,60)):
       print ("Your grade is C")
elif (marks in range(60,80)):
       print ("Your grade is B")
elif (marks in range(80,100)):
       print ("Your grade is A")
else:
       print ("Incorrect marks")