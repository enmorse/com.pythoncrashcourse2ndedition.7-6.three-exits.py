# Write three different versions of either Exercise
# 7-4 or Exercise 7-5 that do each of the following
# at least once.
# Use a conditional test in the while statement to
# stop the loop.
# Use an active variable to control how long the
# loop runs.
# Use a break statement to exit the loop when the
# user enters a 'quit' value.
current_number = 10
while current_number > 0:
    print(current_number)
    current_number -= 1

print("Blastoff!")

# prompt = "\nWhat is your name?: "
# prompt += "(\nEnter 'quit' to end the program)"
# active = True
#
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

prompt = "\nPlease enter a city that your would like " \
         "to visit: "
prompt += "\n(Enter 'quit' to end the program)"

while True:
    answer = input(prompt)

    if answer == 'quit':
        break
    else:
        print(f"I would like to visit  {answer.title()} "
              f"too!")
