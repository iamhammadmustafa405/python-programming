# 2. .format()
name = "Hammad"
age = 19

print("My name is {} and I am {} years old.".format(name, age))


# You can also specify positions:

print("I am {1} years old and my name is {0}.".format(name, age))

# another way

print("My name is {}".format("Ali"))


# .formatmap --> for dict

do = {
  "age": 45,
  "size": 20
}

print("my age is {age} and my size is {size}".format_map(do))