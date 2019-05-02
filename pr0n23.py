'''
name = input("Enter name")
name2 = input("Enter second name")
print("Here are the names alphabetically:")
if name < name2:
    print(name)
    print(name2)
else:
    print(name2)
    print(name)
 '''

# MIN_SALARY = 30000
# MIN_YEAR = 2
#
# salary = int(input("Enter your salary: "))
# years = int(input("Enter number of years on the job: "))
# if salary >= MIN_SALARY:
#     if years >= MIN_YEAR:
#         print("You qualify for the loan")
#     else:
#         print("You must have been on your current job for at least", MIN_YEAR , "two years to qualify.")
# else:
#     print("You must earn at least", format(MIN_SALARY,',.2f'), " per year to qualify")
#


# if salary >= MIN_SALARY or years >= MIN_YEAR:
#     print("You qualify for the loan")
# else:
#     print("You do not qualify for this loan.")

# max = 5
# total = 0
# print("Input 5 numbers and this program will find the sum")
# for i in range(max):
#     number = int(input("Enter a number: "))
#     total += number
# print("The total is",total)

#0.65% tax on valued lots. Lots are positive integers. Ask for lot number and value to determine
#total tax
# mark_up = 2.5
# another = 'y'
# while another == 'y' or another == 'Y':
#     wholesale = float(input("Enter the item's wholesale cost: "))     #priming read, if invalid, perform other
#     #while loop
#     while wholesale < 0:
#         print("Price can't be a negative number, please try again: ")
#         wholesale = float(input("Enter the item's wholesale cost: "))
#     retail = wholesale * mark_up
#     print('Retail price: $',format(retail,',.2f'),sep = '')
#     another = input("Is there another item? Input y for yes: ")
#
#
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours,':',minutes,':',seconds)
# #inner loop goes around 60 times per 1 iteration of outer loop

# #program to get the average of each student's test score
# student_num = int(input("Enter number of students: "))
# num_test_scores = int(input("Enter number of test scores per student: "))
# for student in range(student_num):
#     total = 0.0
#     for score in range(num_test_scores):
#         test_score = float(input("Enter score: "))
#         total += test_score
#     average = total/num_test_scores
#     print("Student #:",student+1,"Average:",average)
#     print("----------------------")
#
# num_students = int(input("How many students do you have? "))
# num_test_scores = int(input("How many test scores per student? "))
#
# for student in range(num_students):
#     total = 0.0
#     print('Student number', student +1)
#     print('--------------------')
#     for test_num in range(num_test_scores):
#         print('Test number', test_num + 1, end = '')
#         score = float(input(': '))
#         total += score
#     average = total / num_test_scores
#
#     print('The average for student number', student + 1, 'is:', average)
#     print()


#display one row:
for row in range(6):
    for col in range(row+1):
        print(' ',end='')
    print('#')
