'''# Ask user for the number of tasks
TaskNo = int(input('How many tasks do you want to do today? \n'))

# Initialize an empty list to store tasks
TaskList = []

# Collect tasks from the user
for TaskIndex in range(TaskNo):
    task = input(f'Task {TaskIndex + 1}: ')
    TaskList.append(task)

# Print the list of tasks
print(TaskList)'''


def calculate_discount(price, discount_percent):

    if discount_percent >= 0.2:
        cost = price - (price * discount_percent)
        return cost
    else:
        return price


original_price = float(input("Enter the price: "))
discount_percentage=float(input("Enter the discount percentage: "))
print("The cost is", calculate_discount(original_price, discount_percentage))





