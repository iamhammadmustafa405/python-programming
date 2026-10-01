# encode

str = "Hammad"

print(str.encode("utf-8")) # it is in bytes



# encode() function in Python

# The encode() method converts a string (str) into bytes (bytes).

# Simple example
# text = "Hello"

# result = text.encode()

# print(result)

# Output:

# b'Hello'

# The b means the result is bytes.

# Why do we use encode()?

# Computers often need text converted into bytes when storing or transmitting data, such as:

# Files
# Networks
# APIs
# Databases
# Encoding with UTF-8

# You can specify the encoding:

# text = "Hello"

# result = text.encode("utf-8")

# print(result)

# Output:

# b'Hello'

# For non-English characters, encoding becomes more noticeable:

# text = "سلام"

# result = text.encode("utf-8")

# print(result)