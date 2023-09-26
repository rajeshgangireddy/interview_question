# Function which outputs true if rect1 and rect2 are overlapping
# Check if the rectangles are overlapping
# rectangle format: (x1, y1, x2, y2)
# x1 and y1 are the coordinates of the lower left corner
# x2 and y2 are the coordinates of the upper right corner
def rectangles_overlap(rectangle_1: tuple, rectangle_2: tuple) -> bool:
    """
    Check if two rectangles overlap.

    Parameters:
    rectangle_1 (tuple): Coordinates of the first rectangle in the format (x1, y1, x2, y2).
    rectangle_2 (tuple): Coordinates of the second rectangle in the format (x1, y1, x2, y2).

    Returns:
    bool: True if the rectangles overlap, False otherwise.
    """
    x1_1, y1_1, x2_1, y2_1 = rectangle_1
    x1_2, y1_2, x2_2, y2_2 = rectangle_2

    # Check if either rectangle has zero area
    if x1_1 == x2_1 or y1_1 == y2_1 or x1_2 == x2_2 or y1_2 == y2_2:
        return False

    is_overlap = (x1_1 < x2_2) and (x2_1 > x1_2) and (y1_1 < y2_2) and (y2_1 > y1_2)

    # Note : A cleaner solution would be to use s
    return is_overlap


# Test cases
rectangle1 = (91, 14, 95, 23)
rectangle2 = (82, 73, 86, 79)
rectangle3 = (84, 18, 96, 77)

print(rectangles_overlap(rectangle1, rectangle2))
print(rectangles_overlap(rectangle1, rectangle3))
print(rectangles_overlap(rectangle2, rectangle3))
