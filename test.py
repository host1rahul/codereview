def calculate_area(length, breath):  # Bug: misspelled "breadth" as "breath"
  """
  This function calculates the area of a rectangle.
  """
  area = lenght * breath  # Bug: used "lenght" instead of "length"
  return area

# Example usage with another bug (incorrect calculation for circle area)
radius = 5
circle_area = calculate_area(radius, radius)  # Bug: This calculates square of radius instead of pi * radius^2
print(f"Area of circle with radius {radius} is: {circle_area}")