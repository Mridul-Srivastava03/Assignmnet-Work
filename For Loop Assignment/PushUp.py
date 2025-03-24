ans = "No"
for i in range(1,51):
    if i == 50:
        print("Congratulations! You made it")
        break
    if(i % 10 == 0):
        ans = input("Are you tired?\n")
        if(ans == "yes" or ans == "y"):
            print(f'You did a total of {i} push-ups.')
            break
        elif(ans == "no" or ans == "n"):
            print(f'{50-i} push-ups are remaining.')