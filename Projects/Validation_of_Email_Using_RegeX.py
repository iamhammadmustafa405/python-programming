# Email Validation Using RegeX Module
import re
email_condition= "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Your Email: ")

if re.search(email_condition,user_email):
    print("Right Email!")
else:
    print("Wrong Email!")



#  Basic RegeX  Notes:
# 1. Basic Character Patterns
# Pattern	Meaning	Example
# a	exact character	matches a
# abc	exact word	matches abc
# .	any single character	a.c → abc, a1c
# \	escape special character	\. means dot
# 2. Character Classes
# Pattern	Meaning	Example
# [abc]	a or b or c	a or b
# [a-z]	lowercase letters	m, z
# [A-Z]	uppercase letters	A, X
# [0-9]	digits	5, 9
# [a-z0-9]	letters or numbers	a3, x9
# 3. Predefined Classes
# Pattern	Meaning	Example
# \d	digit (0–9)	5
# \D	not digit	a
# \w	word char (a-z, 0-9, _)	abc_1
# \W	not word char	@, #
# \s	space	" "
# \S	non-space	abc
# 4. Quantifiers (Repetition)
# Pattern	Meaning	Example
# a+	1 or more	a, aaa
# a*	0 or more	``, a, aaaa
# a?	0 or 1	a or nothing
# a{3}	exactly 3	aaa
# a{2,5}	2 to 5 times	aa, aaaa
# 5. Position Anchors
# Pattern	Meaning	Example
# ^	start of string	^abc
# $	end of string	abc$
# ^abc$	exact match	only abc
# 6. Common Combinations (Very Important)
# Email structure
# ^[a-z]+[._]?[a-z0-9]+@\w+\.\w{2,3}$
# Phone number (Pakistan example)
# ^03[0-9]{9}$
# Username (simple)
# ^[a-zA-Z0-9_]{3,15}$
# Password (basic strong rule)
# ^(?=.*[A-Z])(?=.*[0-9]).{8,}$
# 7. Grouping & OR
# Pattern	Meaning	Example
# (abc)	group	treat as one unit
# `a	b`	OR
# `(cat	dog)`	either word
# 8. Practical Template Thinking (How to build regex)

# A pattern usually follows:

# START → USERNAME → SYMBOL → DOMAIN → EXTENSION → END
# ^         ...        @        ...        .xx      $

