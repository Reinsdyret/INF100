from math import sqrt


def side_length(x1, y1, x2, y2):
    """Returns the length of the side between the points (x1,y1) and (x2,y2)"""
    # din kode her
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def mid(x1_or_y1, x2_or_y2, x3_or_y3, a, b, c):
    """
    Returns midpoint coordinate given:
    coordinates x1_or_y1, x2_or_y2, x3_or_y3
    and sidelengths a (opposite (x1,y1)), b (opposite (x2,y2)), c (opposite (x3,y3))
    """
    # din kode her
    


def incircle_radius(a, b, c):
    """Returns the radius of the incircle of a triangle with sidelengths a, b and c"""
    # din kode her


def find_incircle(x1, y1, x2, y2, x3, y3):
    """
    Finds and prints the center and radius of the incircle
    of a triangle with corners (x1,y1), (x2,y2), (x3,y3)
    """

    print(f"Your triangle is ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}).\n")

    print("First we calculate the sidelengths.")
    side1 = 0  # side opposite (x1,y1)
    side2 = 0  # side opposite (x2,y2)
    side3 = 0  # side opposite (x3,y3)

    print("Then we find the center.")
    center_x = 0
    center_y = 0
    print(f"The center is {center_x, center_y}.\n")

    print("Finally we calculate the radius of the incircle.")
    radius = 0
    print(f"The incircle has radius {radius}.")


print("Define your triangle:")
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
x3 = int(input("x3 = "))

y1 = int(input("y1 = "))
y2 = int(input("y2 = "))
y3 = int(input("y3 = "))

find_incircle(x1, y1, x2, y2, x3, y3)
