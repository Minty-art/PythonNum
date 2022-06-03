
chances=5
rightans=7
question=int input("Guess a Number")
for i in chances:
    question= int input("Guess a Number")
    if (question not rightans and question < rightans):
            print("Wrong! It's a bit lower than that.")
        else if (question not rightans and question > rightans):
            print("Wrong! It's higher than that.")
        else:
            print("Correct!")