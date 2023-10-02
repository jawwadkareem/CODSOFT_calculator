import math
import sys
class Calculator:
    def __init__(self):
        print()
        print(' '*20+'='*20+'Welcome, these are the basic operations you can perform using my calculator'+'='*20)
        print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Average\n7. Exit')
        user_in = int(input('Which operation do you want to perform?'))
        if user_in == 1:
            print(self.add())
        elif user_in == 2:
            print(self.sub())
        elif user_in == 3:
            print(self.mult())
        elif user_in == 4:
            print(self.div())
        elif user_in == 5:
            print(self.pow())
        elif user_in == 6:
            print(self.avgg())
        elif user_in == 7:
            sys.exit()
        self.__init__()
    def __str__(self):
        return 'A calculator which can help you to solve basic mathematical operations'
    def add(self):
        user_addnum = input('Enter the numbers you want to add separated by commas ')
        addnum = user_addnum.split(',')
        res = 0
        resdesc = ''
        for i in range(len(addnum)):
            res += int(addnum[i])
            if i == len(addnum) -1:
                resdesc += f'{addnum[i]} = {res}\n'
            else:
                resdesc += f'{addnum[i]}+'
        return resdesc

    def mult(self):
        user_multnum = input('Enter the numbers you want to multiply separated by commas ')
        multnum = user_multnum.split(',')
        res = 1
        resdesc = ''
        for i in range(len(multnum)):
            res *= int(multnum[i])
            if i == len(multnum) - 1:
                resdesc += f'{multnum[i]} = {res}\n'
            else:
                resdesc += f'{multnum[i]}*'
        return resdesc

    def sub(self):
        user_subnum = input('Enter the numbers you want to subtract in correct order separated by commas ')
        subnum = user_subnum.split(',')
        res =  int(subnum[0])
        resdesc = f'{subnum[0]}-'
        for i in range(1,len(subnum)):
            res -= int(subnum[i])
            if i == len(subnum) - 1:
                resdesc += f'{subnum[i]} = {res}\n'
            else:
                resdesc += f'{subnum[i]}-'
        return resdesc
    def avgg(self):
        res = self.add()
        no_of_operands = len(res.split('+'))
        add_res = res.split(' ')
        add_res = int(add_res[-1])
        resdesc = f'{add_res}/{no_of_operands} = {add_res/no_of_operands}'
        return resdesc

    def div(self):
        divident = int(input('Enter Dividend: '))
        divider = int(input('Enter Divider: '))
        res = divident/divider
        resdesc = f'{divident}/{divider} = {res}'
        rem = divident%divider
        if rem!=0:
            resdesc +=f'\nRemainder = {rem}'
        return resdesc

    def pow(self):
        number = int(input('Enter Number: '))
        print('Select exponent from the options given below ')
        print('1. Square Root\n2. Cube Root\n3. Square\n4. Cube\n5. Not from the above')
        user_choice = int(input('Your Choice: '))
        if user_choice == 1:
            res = math.sqrt(number)
            resdesc = f'Square root of {number} = {res}'
        elif user_choice == 2:
            res = math.cbrt(number)
            resdesc = f'Cube root of {number} = {res}'
        elif user_choice == 3:
            res = number**2
            resdesc = f'Square of {number} = {res}'
        elif user_choice == 4:
            res = number**3
            resdesc = f'Cube of {number} = {res}'
        elif user_choice == 5:
            exp = int(input('Enter exponent: '))
            res = number**exp
            resdesc = f'{number} raise to {exp} = {res}'
        return resdesc
cal = Calculator()
print(cal)