import arcade
import math

def rotate_point_list(points, center_x, center_y, angle_degrees):
    """
    Rotates a list of (x, y) points around a specified center.

    :param points: A list of points, where each point is a tuple or list [x, y].
    :param center_x: The x-coordinate of the center of rotation.
    :param center_y: The y-coordinate of the center of rotation.
    :param angle_degrees: The angle in degrees to rotate.
    :return: A new list of the rotated points.
    """
    rotated_points = []
    for point in points:
        x, y = point
        # Use the arcade library's built-in function to rotate the point
        new_x, new_y = arcade.math.rotate_point(x, y, center_x, center_y, angle_degrees)
        rotated_points.append([new_x, new_y])
        return rotated_points

    # Example usage:
    # Define a list of points (e.g., a simple triangle)
    original_points = [[50, 60], [10, 30], [30, 10]]
    # Define the center of rotation
    center_x, center_y = 30, 40
    # Define the angle to rotate (e.g., 90 degrees)
    angle = 78

    # Rotate the points
    new_points = rotate_point_list(original_points, center_x, center_y, angle)



print("Original Points:", original_points)
print("Rotated Points:", new_points)