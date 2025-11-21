from typing import Optional
import math
def calculate_area(shape: str, x: float, y: Optional[float] = None) -> float:
    """Calculate the area of a basic geometric shape.

    Parameters:
        shape: One of "rectangle", "square", or "circle" (case-insensitive).
        x: For rectangle: width; for square/circle: side/radius.
        y: For rectangle only: height. Ignored for other shapes.

    Returns:
        The computed area as a float.

    Raises:
        ValueError: If inputs are invalid or shape is unsupported.
    """
    if not isinstance(shape, str):
        raise ValueError("shape must be a string")

    normalized_shape = shape.strip().lower()

    if normalized_shape == "rectangle":
        if y is None:
            raise ValueError("y (height) is required for rectangle")
        return float(x) * float(y)
    elif normalized_shape == "square":
        return float(x) * float(x)
    elif normalized_shape == "circle":
        return math.pi * float(x) * float(x)
    else:
        raise ValueError(f"unsupported shape: {shape}")

if __name__ == "__main__":
    # Example usages
    print("Rectangle 3 x 4:", calculate_area("rectangle", 3, 4))
    print("Square side=5:", calculate_area("square", 5))
    print("Circle r=2:", calculate_area("circle", 2))

