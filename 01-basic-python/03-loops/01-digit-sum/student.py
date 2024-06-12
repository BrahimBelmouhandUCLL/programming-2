# Write your code here
def digit_sum(n):
    sum = 0
    for i in range (len(str(n))):
        sum += last_digit(n)
        n = remove_last_digit(n)
    return sum
def last_digit(n):
    return int(n) % 10
def remove_last_digit(n):
    return (int(n) //10)
print(digit_sum(159))