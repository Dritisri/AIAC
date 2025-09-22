def area_of_rectangle(length: float, breadth: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * breadth

if __name__ == "__main__":
    length = 10
    breadth = 20
    area = area_of_rectangle(length, breadth)
    print(f"The area of the rectangle with length {length} and breadth {breadth} is {area}.")