def main():
    # Write your code here!
    # Be careful, all your code must be indented like this comment !
    left_number = 10
right_number = 2

symbol = '+'

result = 0

if not isinstance(left_number,int) or not isinstance(right_number,int):
    print("both left_numbers and right_numbers must be integers")
    exit()
match symbol:
    case '+':
        result = left_number + right_number
    case '-':
        result = left_number - right_number
    case '*':
        result = left_number * right_number
    case '/':
        if  left_number / 0 :
            print('Error: division by zero is not allowed.')
        else :
            result = left_number / right_number
    case _ :
        print('error message')
    

print(f"The result of {left_number} {symbol} {right_number} = {result}")


# Do not modify the code below
if __name__ == "__main__":
    main()
