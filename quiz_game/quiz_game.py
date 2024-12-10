print("Witam w quizie")

playing = input("Chcesz zagrać ")

if playing.lower() != "yes":
    quit()

print("Gramy!")
score = 0

answer = input("Rozwiń skrót CPU ")

if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("Co oznacza skrót GPU? ").lower()

if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("Rozwiń skrót RAM" )

if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
    
answer = input("Co oznacza skrót ROM? ")

if answer == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Uzyskałeś " + str(score) + " punkty/ów.")

print("Masz " + str(score/4 * 100) + " % prawidłowych odpowiedzi ")