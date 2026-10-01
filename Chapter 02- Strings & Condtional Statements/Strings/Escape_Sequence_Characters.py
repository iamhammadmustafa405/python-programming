# Escape sequence characters: 
str= "My name is Hammad Mustafa.\n I am 18 Years old."
print(str)
print("Hello\nWorld")
print("Name:\tHammad")
print("Path: C:\\Users\\Admin")
print("He said \"Python is easy\"")


# | Escape sequence | Meaning                          | Example              |
# | --------------- | -------------------------------- | -------------------- |
# | `\n`            | New line                         | `"Hello\nWorld"`     |
# | `\t`            | Tab                              | `"Hello\tWorld"`     |
# | `\\`            | Backslash `\`                    | `"C:\\Users"`        |
# | `\'`            | Single quote `'`                 | `'It\'s good'`       |
# | `\"`            | Double quote `"`                 | `"He said \"Hi\""`   |
# | `\r`            | Carriage return                  | `"Hello\rWorld"`     |
# | `\b`            | Backspace                        | `"Hell\bo"`          |
# | `\f`            | Form feed                        | `"Hello\fWorld"`     |
# | `\v`            | Vertical tab                     | `"Hello\vWorld"`     |
# | `\a`            | Alert/bell                       | `"Hello\a"`          |
# | `\0`            | Null character                   | `"Hello\0"`          |
# | `\ooo`          | Octal value                      | `"\101"` → `A`       |
# | `\xhh`          | Hexadecimal value                | `"\x41"` → `A`       |
# | `\N{name}`      | Unicode character by name        | `"\N{HEART}"` → `♥`  |
# | `\uXXXX`        | Unicode character (4 hex digits) | `"\u0041"` → `A`     |
# | `\UXXXXXXXX`    | Unicode character (8 hex digits) | `"\U00000041"` → `A` |


# A common practical use  of carriage return is updating the same line:

# print("Loading...", end="\r")
# print("Done!      ")

# emojis using their name --> \N{Name}

print("\N{SMILING FACE WITH SMILING EYES}")
print("\N{THUMBS UP SIGN}")
print("\N{SNOWMAN}")