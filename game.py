print("Welcome to computer quize!")

play = raw_input("would you like to play? ").lower()
score = 0

if play != "yes" :
   quit()
print("cool,Let's Play!")

answer = raw_input("What is CPU stands for? ").lower()

if answer == "central processing unit" :
	print ("Correct answer")
	score += 1
else:

	print("Incoorect answer")

answer = raw_input("What is RAM stands for? ").lower()

if answer == "random access memory" :
        print ("Correct answer")
        score += 1
else:

        print("Incoorect answer")

answer = raw_input("What is H stands for? ").lower()

if answer == "hardware" :
        print ("Correct answer")
        score += 1
else:

        print("Incoorect answer")


print("you got "+ str(score) +" questions correct!")
print("you score is "+ str((score / 3) * 100) + "%.")




