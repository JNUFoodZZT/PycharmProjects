"""
用户输入两个数字返回其和，并做异常处理
"""

print('Give me two numbers and i will back you these addation.'
      '\n you can input q to quit whenever you are tried.')
while True:
    first_num = input('the first num is:')
    second_num = input('the second num is:')
    try:
        if first_num =='q' or second_num =='q':
            break
        sum = int(first_num) + int(second_num)
    except ValueError:
        print('please give me numbers instead of others.')
    else:
        print(f"the sum is {sum}.")
