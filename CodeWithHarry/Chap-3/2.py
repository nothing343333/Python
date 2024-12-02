# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name = str(input("Enter your name\n"))
date = str(input("Enter your date\n"))
print(f"""
 Dear {name},
  You are selected!
     {date}       """)