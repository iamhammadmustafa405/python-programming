# 114: create a file of numbers and calculate the sum and average.
with open("num.txt", "r") as f:
    data= f.read()
    data=  data.split(",")
    sum = 0
    for i in data:
        sum += int(i)
    avg= sum/len(data)
print(f"The Sum of Numbers is {sum} & The Average of Numbers is {avg} in the file.")