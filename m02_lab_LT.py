# m02_lab_LT.py
# Logan Till
# 2025-06-21
# Honor Roll


# this will print the title of the program
print('\n***************************************')
print('Honor Roll (by Logan Till)')
print('***************************************\n')


# Import Libraries
# Input File
# Output File
# Constants
WELCOME = ('Welcome!\nThis program will determin whether or not a student has made the Deans List or Honor Roll.\n')
GOODBYE = ('Thank you for using this program!')
# Variables


# Program Logic
print(WELCOME)

while True:
   # Get the student's last name
   last_name = input('Please enter the student\'s last name (or type "zzz" to quit): ')
   if last_name.lower() == 'zzz':
      break
   # Get the student's first name
   first_name = input('Please enter the student\'s first name: ')

   # Get the student's GPA
   try:
      gpa = float(input('Please enter the student\'s GPA: '))
   except ValueError:
      print('Invalid GPA. Please enter a numeric value.')
      continue

   # Determine if the student is on the Dean's List or Honor Roll
   if gpa >= 3.5:
      status = 'made the Dean\'s List'
   elif gpa >= 3.25:
      status = 'made Honor Roll'
   else:
      status = 'not made Honor Roll'

   print(f'{first_name}{last_name} has a GPA of {gpa:.2f} and has {status}.\n')

# End of Program
print(GOODBYE)