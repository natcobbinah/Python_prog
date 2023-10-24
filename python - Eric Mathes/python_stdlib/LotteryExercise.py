import random

lottery_values = [1,4,6,2,4,73,83,42,67, 'q','t','y','d','w']

selected_Choices = random.choices(lottery_values, k = 4)
print(f"Any ticket matching these {selected_Choices} four numbers or"
      " letters wins a prize")

# lottery analysis
my_ticket = [1, 4, 2, 'y']

search_ticket = True
while search_ticket:
    print("Searching...")
    if selected_Choices == my_ticket:
        print("You won")
        search_ticket = False
    