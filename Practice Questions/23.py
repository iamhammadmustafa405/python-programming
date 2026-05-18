# 23:  Use a while loop to reverse a given number.
n= 1234
reverse = 0
while n>0:
    digit= n%10
    reverse = reverse*10 + digit
    n= n//10
print(f"The reverse Number is: {reverse}")