# FREEZE CODE BEGIN
x = int(input("Enter a number:\n"))
y = int(input("Enter a number:\n"))
z = int(input("Enter a number:\n"))
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

maximum = find_max(x, y, z)
print(f"Maximum value: {maximum}")
# FREEZE CODE END

