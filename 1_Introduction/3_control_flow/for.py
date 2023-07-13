# for variable in collection:
#   instructions
#   .
#   .
#   .


# x: str = input("Addad ra vared konid")
# x: int = int(x)

x = int(input())
# list_1 = [0, 1, 2, 3, 4]

# for i in list_1:
#     print("+" * (i + 1))

# for i in range(0, x, 1):
#     print("+" * (i + 1))

# -----*-----
# ----***----
# ---*****---
# --*******--
# -*********-
# ***********
# for i in range(1, x + 1):
#     x1 = x - i
#     x2 = 2 * i - 1
#     print(x1 * "-" + x2 * "*" + x1 * "-")


#    *
#    *
#    *
# *******
#    *
#    *
#    *
# for i in range(1, 2 * x):
#     if i == 2 * x // 2:
#         print("*" * (2 * x - 1))
#     else:
#         print((x - 1) * " " + "*" + (x - 1) * " ")

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 1-
# for i in range(1, x + 1):
#     x1 = x - i
#     x2 = 2 * i - 1
#     print(x1 * " " + x2 * "*" + x1 * " ")

# for i in range(x - 1, 0, -1):
#     x1 = x - i
#     x2 = 2 * i - 1
#     print(x1 * " " + x2 * "*" + x1 * " ")

# 2-
# for i in range(1, 2 * x):
#     if i <= x:
#         a = x - i
#         b = 2 * i - 1
#         print(" " * a + "*" * b + " " * a)
#     else:
#         a = i - x
#         b = (4 * x) - 1 - (2 * i)
#         print(" " * a + "*" * b + " " * a)

# x x x x
# x     x
# x     x
# x x x x

# for i in range(x):
#     if i == 0 or i == x - 1:
#         print("x " * x)
#     else:
#         print("x " + "  " * (x - 2) + "x")

# x           x
#   x       x
#     x   x
#       x
#     x   x
#   x       x
# x           x

# ONE WAY:
# if x % 2 == 1:
#     b = x - 2
#     for i in range(x // 2):
#         a = i
#         c = i
#         print(a * "  " + "x " + b * "  " + "x " + a * "  ")
#         b -= 2
#         # Or we can say
#         # b = x-(2*i)-2
#         # since:
#         # a+b+c = x-2
#         # a = c = i
#         # so
#         # 2*i+b = x-2
#         # and then
#         # b = x-2*i-2

#     print("  " * (x // 2) + "x " + "  " * (x // 2))

#     b = 1
#     c = a = (x // 2) - 1
#     for i in range(x // 2):
#         print(a * "  " + "x " + b * "  " + "x " + a * "  ")
#         a -= 1
#         c -= 1
#         b += 2

# SOME OTHER WAY

# if x % 2 == 1:
#     a1 = 0
#     b1 = x - 2

#     a2 = x // 2 - 1
#     b2 = 1
#     for i in range(x):
#         if i < x // 2:
#             print(a1 * "  " + "x " + b1 * "  " + "x " + a1 * "  ")
#             a1 += 1
#             b1 -= 2
#         elif i == x // 2:
#             print("  " * (x // 2) + "x " + "  " * (x // 2))
#         else:
#             print(a2 * "  " + "x " + b2 * "  " + "x " + a2 * "  ")
#             a2 -= 1
#             b2 += 2
