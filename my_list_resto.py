# Write a python program that do the following:
# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

my_list_menu = [100, 250, 318, 400, 20, 69, 28, 8, 2003, 12] #item
print("List's items for today: ", my_list_menu, "\nCommands:\n"
        "   1 -> Get the length of the list\n" # len()
        "   2 -> Insert an item on the list\n" # .insert()
        "   3 -> Remove an item on the list\n" # .remove()
        "   4 -> Sort the items in ascending order\n" # .sort()
        "   5 -> Sort the items in descending order\n" # .sort(,reverse=True)
        "   6 -> Select one item on the list\n" # my_list_menu[int(input("Enter the index: "))]
        "   7 -> Modify an item on the list\n" # my_list_menu[index] = num
        "   8 -> Select an item then remove it from the list\n" # .pop()
        "   9 -> Calculate the summation of the whole list\n" # .sum()
        "   10 -> Get the smallest number on the list\n" # .min()
        "   11 -> Get the largest number on the list\n" # .max()
        ) 

user_req = int(input("Enter your request [1-11]: "))
if user_req == 1:
    list_length = len(my_list_menu)
    print(f"List length: {list_length}")

elif user_req == 2:
    my_list_menu.insert(int(input("Enter the index: ")),int(input("Enter the number you want to insert: ")))
    print(f"Updated list: {my_list_menu}")

elif user_req == 3:
    my_list_menu.remove(int(input("Enter the item you want to remove: ")))
    print(f"Updated list: {my_list_menu}")

elif user_req == 4:
    my_list_menu.sort()
    print(f"Updated list: {my_list_menu}")

elif user_req == 5:
    my_list_menu.sort(reverse=True)
    print(f"Updated list: {my_list_menu}")