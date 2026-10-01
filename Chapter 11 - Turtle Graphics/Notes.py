# # Turtle Graphics in Python — Full Guide

# ## 1. What is Turtle?

# **Turtle is a Python module used to draw pictures and shapes using code.**

# Imagine a small turtle holding a pen:

# ```text
#        🐢
#         |
#         | moves
#         ↓
#   ─────────────
# ```

# You tell the turtle:

# * move forward
# * turn left/right
# * lift the pen
# * change color
# * draw shapes

# ```python
# import turtle
# ```

# ---

# # 2. Create Your First Turtle

# ```python
# import turtle

# t = turtle.Turtle()

# t.forward(100)

# turtle.done()
# ```

# ### What happens?

# ```text
# Create turtle
#      ↓
# Move forward 100 pixels
#      ↓
# Show window
# ```

# ---

# # 3. `forward()`

# Moves the turtle forward.

# ```python
# t.forward(100)
# ```

# You can also write:

# ```python
# t.fd(100)
# ```

# Both mean the same thing.

# ---

# # 4. `backward()`

# Moves backward.

# ```python
# t.backward(50)
# ```

# Short version:

# ```python
# t.bk(50)
# ```

# ---

# # 5. Turning

# ## Right

# ```python
# t.right(90)
# ```

# ## Left

# ```python
# t.left(90)
# ```

# Angles are measured in degrees.

# ```text
#         90°
#          ↑
#          |
# 180° ← 🐢 → 0°
#          |
#          ↓
#         270°
# ```

# ---

# # 6. Draw a Square

# ```python
# import turtle

# t = turtle.Turtle()

# t.forward(100)
# t.right(90)

# t.forward(100)
# t.right(90)

# t.forward(100)
# t.right(90)

# t.forward(100)
# t.right(90)

# turtle.done()
# ```

# But repeating code is unnecessary.

# ---

# # 7. `for` Loop + Turtle

# ```python
# import turtle

# t = turtle.Turtle()

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.done()
# ```

# ### Why 4?

# A square has **4 sides**.

# ---

# # 8. Draw a Triangle

# ```python
# import turtle

# t = turtle.Turtle()

# for i in range(3):
#     t.forward(100)
#     t.left(120)

# turtle.done()
# ```

# Why `120°`?

# For a regular triangle:

# ```text
# 360 ÷ 3 = 120°
# ```

# ---

# # 9. Draw a Pentagon

# ```python
# for i in range(5):
#     t.forward(100)
#     t.right(72)
# ```

# Because:

# ```text
# 360 ÷ 5 = 72°
# ```

# ### General formula

# For a regular polygon:

# ```text
# turn angle = 360 / number_of_sides
# ```

# ---

# # 10. Pen Control

# ## `penup()`

# Stop drawing.

# ```python
# t.penup()
# ```

# The turtle can move without drawing.

# ## `pendown()`

# Start drawing again.

# ```python
# t.pendown()
# ```

# Example:

# ```python
# t.forward(100)

# t.penup()
# t.forward(50)

# t.pendown()
# t.forward(100)
# ```

# You get two separate lines.

# ---

# # 11. Pen Color

# ```python
# t.pencolor("red")
# ```

# Then:

# ```python
# t.forward(100)
# ```

# Other colors:

# ```python
# t.pencolor("blue")
# t.pencolor("green")
# t.pencolor("black")
# ```

# ---

# # 12. Fill a Shape

# Use:

# ```python
# t.begin_fill()
# ```

# Draw the shape, then:

# ```python
# t.end_fill()
# ```

# Example:

# ```python
# import turtle

# t = turtle.Turtle()

# t.fillcolor("blue")

# t.begin_fill()

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# t.end_fill()

# turtle.done()
# ```

# ---

# # 13. Change Turtle Color

# ```python
# t.color("red")
# ```

# This changes the turtle's drawing color and its appearance.

# You can separately specify:

# ```python
# t.color("red", "yellow")
# ```

# Meaning:

# ```text
# Pen color  → red
# Fill color → yellow
# ```

# ---

# # 14. Change Pen Size

# ```python
# t.pensize(5)
# ```

# or:

# ```python
# t.width(5)
# ```

# Example:

# ```python
# t.pensize(10)
# t.forward(100)
# ```

# ---

# # 15. Turtle Speed

# ```python
# t.speed(1)
# ```

# Slow.

# ```python
# t.speed(10)
# ```

# Fast.

# ```python
# t.speed(0)
# ```

# Fastest.

# Usually:

# ```text
# 1 → slow
# 5 → medium
# 10 → fast
# 0 → fastest
# ```

# ---

# # 16. Turtle Shape

# By default, the turtle looks like a turtle.

# You can change it:

# ```python
# t.shape("turtle")
# ```

# Other common shapes:

# ```python
# t.shape("arrow")
# t.shape("circle")
# t.shape("square")
# t.shape("triangle")
# t.shape("classic")
# ```

# ---

# # 17. Turtle Position

# You can move the turtle to a specific coordinate.

# ```python
# t.goto(100, 50)
# ```

# Coordinates work like this:

# ```text
#              +y
#               ↑
#               |
#        (-x,+y)|(+x,+y)
#               |
#    -----------+----------→ +x
#               |
#        (-x,-y)|(+x,-y)
#               |
#               ↓
#              -y
# ```

# The center is:

# ```text
# (0, 0)
# ```

# ---

# # 18. `setx()` and `sety()`

# Change only X:

# ```python
# t.setx(100)
# ```

# Change only Y:

# ```python
# t.sety(100)
# ```

# ---

# # 19. Current Position

# ```python
# print(t.position())
# ```

# You can also use:

# ```python
# print(t.xcor())
# print(t.ycor())
# ```

# ---

# # 20. Move Without Drawing

# ```python
# t.penup()
# t.goto(100, 100)
# t.pendown()
# ```

# This is useful when creating multiple shapes.

# ---

# # 21. Draw a Circle

# Very easy:

# ```python
# t.circle(50)
# ```

# `50` is approximately the radius.

# Example:

# ```python
# import turtle

# t = turtle.Turtle()

# t.circle(100)

# turtle.done()
# ```

# ---

# # 22. Half Circle

# ```python
# t.circle(100, 180)
# ```

# The second argument is the angle.

# ```text
# circle(radius, extent)
# ```

# For example:

# ```python
# t.circle(100, 90)
# ```

# draws 90° of a circle.

# ---

# # 23. Draw Multiple Circles

# ```python
# for i in range(5):
#     t.circle(50)
#     t.right(72)
# ```

# This creates a flower-like pattern.

# ---

# # 24. Reset Turtle

# ```python
# t.reset()
# ```

# This:

# * clears drawings
# * resets position
# * resets turtle settings

# ---

# # 25. Clear Drawing

# ```python
# t.clear()
# ```

# This removes the drawing but doesn't completely reset the turtle settings.

# ---

# # 26. Hide Turtle

# ```python
# t.hideturtle()
# ```

# Short version:

# ```python
# t.ht()
# ```

# Useful when you want to see only the final drawing.

# ---

# # 27. Show Turtle

# ```python
# t.showturtle()
# ```

# Short version:

# ```python
# t.st()
# ```

# ---

# # 28. Background Color

# You can change the window background:

# ```python
# turtle.bgcolor("black")
# ```

# Example:

# ```python
# import turtle

# turtle.bgcolor("black")

# t = turtle.Turtle()
# t.color("white")

# t.forward(100)

# turtle.done()
# ```

# ---

# # 29. Window Title

# ```python
# turtle.title("My Turtle Program")
# ```

# ---

# # 30. Write Text

# Turtle can write text on the screen.

# ```python
# t.write("Hello Hammad")
# ```

# Example:

# ```python
# import turtle

# t = turtle.Turtle()

# t.write("Hello Python!")

# turtle.done()
# ```

# ---

# # 31. Change Text Size

# ```python
# t.write(
#     "Hello",
#     font=("Arial", 20, "bold")
# )
# ```

# The format is:

# ```python
# font=("font_name", size, "style")
# ```

# Example:

# ```python
# t.write(
#     "Python",
#     font=("Arial", 30, "bold")
# )
# ```

# ---

# # 32. Change Direction

# You can set an exact direction:

# ```python
# t.setheading(90)
# ```

# Common directions:

# ```text
# 0°   → right
# 90°  → up
# 180° → left
# 270° → down
# ```

# ---

# # 33. Get Current Direction

# ```python
# print(t.heading())
# ```

# ---

# # 34. Distance

# You can find distance from the turtle to a point:

# ```python
# t.distance(100, 100)
# ```

# ---

# # 35. Dot

# Draw a dot:

# ```python
# t.dot(20)
# ```

# You can specify color:

# ```python
# t.dot(30, "red")
# ```

# ---

# # 36. Stamp

# `stamp()` makes a copy of the turtle shape.

# ```python
# t.stamp()
# ```

# Example:

# ```python
# for i in range(5):
#     t.stamp()
#     t.forward(50)
# ```

# ---

# # 37. Undo

# ```python
# t.undo()
# ```

# This reverses the last turtle action.

# ---

# # 38. Multiple Turtles

# You can create multiple turtles.

# ```python
# import turtle

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# t1.color("red")
# t2.color("blue")

# t1.forward(100)
# t2.backward(100)

# turtle.done()
# ```

# ---

# # 39. Drawing a Star

# ```python
# import turtle

# t = turtle.Turtle()

# for i in range(5):
#     t.forward(150)
#     t.right(144)

# turtle.done()
# ```

# Why `144°`?

# A 5-point star requires a specific turning angle to create its pattern.

# ---

# # 40. Spiral

# ```python
# import turtle

# t = turtle.Turtle()

# for i in range(50):
#     t.forward(i * 5)
#     t.right(90)

# turtle.done()
# ```

# Here `i` keeps increasing:

# ```text
# 5
# 10
# 15
# 20
# 25
# ...
# ```

# So the lines become longer.

# ---

# # 41. Nested Shapes

# You can put loops inside loops.

# Example:

# ```python
# import turtle

# t = turtle.Turtle()

# for i in range(10):
#     for j in range(4):
#         t.forward(50)
#         t.right(90)

#     t.right(36)

# turtle.done()
# ```

# This creates a repeated square pattern.

# ---

# # 42. Turtle Events

# Turtle can respond to keyboard and mouse actions.

# For example:

# ```python
# def move_forward():
#     t.forward(20)
# ```

# Connect it to a key:

# ```python
# screen = turtle.Screen()

# screen.listen()
# screen.onkey(move_forward, "Up")
# ```

# Now pressing the **Up arrow** moves the turtle.

# ---

# # 43. Simple Keyboard Game

# ```python
# import turtle

# t = turtle.Turtle()
# screen = turtle.Screen()

# def forward():
#     t.forward(20)

# def left():
#     t.left(30)

# def right():
#     t.right(30)

# screen.listen()

# screen.onkey(forward, "Up")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")

# turtle.done()
# ```

# Now you control the turtle using the keyboard.

# ---

# # 44. Important Turtle Methods

# ### Movement

# ```python
# forward()
# backward()
# left()
# right()
# goto()
# setx()
# sety()
# setheading()
# ```

# ### Drawing

# ```python
# circle()
# dot()
# stamp()
# ```

# ### Pen

# ```python
# penup()
# pendown()
# pensize()
# pencolor()
# ```

# ### Appearance

# ```python
# shape()
# color()
# fillcolor()
# speed()
# hideturtle()
# showturtle()
# ```

# ### Screen

# ```python
# bgcolor()
# title()
# ```

# ### Information

# ```python
# position()
# xcor()
# ycor()
# heading()
# distance()
# ```

# ### Control

# ```python
# reset()
# clear()
# undo()
# ```

# ---

# # 45. `Turtle` vs `Screen`

# There are two important things:

# ### Turtle

# Controls the **drawing object**.

# ```python
# t = turtle.Turtle()
# ```

# Then:

# ```python
# t.forward(100)
# t.right(90)
# ```

# ### Screen

# Controls the **window**.

# ```python
# screen = turtle.Screen()
# ```

# Then:

# ```python
# screen.bgcolor("black")
# screen.title("My Game")
# ```

# Think:

# ```text
# Screen → paper/window
# Turtle → pen
# ```

# ---

# # 46. Complete Example

# ```python
# import turtle

# screen = turtle.Screen()
# screen.title("My Square")

# t = turtle.Turtle()

# t.color("blue")
# t.pensize(3)
# t.speed(5)

# t.begin_fill()

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# t.end_fill()

# t.hideturtle()

# turtle.done()
# ```

# ---

# # 47. Common Mistakes

# ### Mistake 1 — Forgetting import

# Wrong:

# ```python
# t = turtle.Turtle()
# ```

# Correct:

# ```python
# import turtle
# t = turtle.Turtle()
# ```

# ---

# ### Mistake 2 — Wrong angle

# For a regular polygon:

# ```text
# 360 / number of sides
# ```

# Example:

# ```text
# Square:
# 360 / 4 = 90°

# Pentagon:
# 360 / 5 = 72°

# Hexagon:
# 360 / 6 = 60°
# ```

# ---

# ### Mistake 3 — Forgetting `turtle.done()`

# Usually finish with:

# ```python
# turtle.done()
# ```

# It keeps the turtle window open.

# ---

# # 48. Turtle Cheat Sheet

# ```python
# import turtle

# t = turtle.Turtle()

# t.forward(100)       # forward
# t.backward(50)       # backward

# t.left(90)           # left
# t.right(90)          # right

# t.penup()            # stop drawing
# t.pendown()          # start drawing

# t.pencolor("red")    # pen color
# t.fillcolor("blue")  # fill color
# t.pensize(5)         # pen thickness

# t.begin_fill()
# t.end_fill()

# t.circle(50)         # circle
# t.dot(20)            # dot

# t.goto(100, 100)     # position
# t.setheading(90)     # direction

# t.speed(5)
# t.shape("turtle")

# t.write("Hello")

# t.hideturtle()
# t.showturtle()

# t.reset()
# t.clear()

# turtle.done()
# ```

# ## Explanation

# Turtle is basically **drawing with Python commands**.
# `forward()` moves, `left()`/`right()` turn, and `penup()`/`pendown()` control whether the turtle draws.
# Loops are especially important because they let you create shapes and patterns without repeating code.
# The two main objects are **Turtle = pen** and **Screen = drawing window**.
# For learning, master **movement → loops → colors/fill → coordinates → events** in that order.
