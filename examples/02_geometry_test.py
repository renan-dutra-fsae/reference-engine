from reference_engine.geometry import Point, Vector, Line
import numpy as np
import matplotlib.pyplot as plt
# Example usage of geometry functions, could be used on a 
# jupyter notebook or as a standalone script to test the geometry module.


# ------------ Point Test ------------
# Define two points
#point_a = Point(1.0, 2.0, 0.0)
#point_b = Point(5.0, 5.0, 0.0)

# point_a = Point(1.0, 2.0, 0.0)
# point_b = Point(1.0, 2.0, 0.0)
# 
# distance = point_a.distance_to(point_b)
# 
# print(f"Point A: {point_a}")
# print(f"Point B: {point_b}")
# print(f"{point_a.__name__} to {point_b.__name__} distance: {distance:.2f}")
# 
# 
# print(f"Distance between point A and point B: {distance}")
# # Plot the points and the distance between them
# plt.figure()
# plt.plot([point_a.x, point_b.x], [point_a.y, point_b.y], 'ro-')
# plt.text(point_a.x, point_a.y, 'A', fontsize=12, ha='right')
# plt.text(point_b.x, point_b.y, 'B', fontsize=12, ha='left')
# plt.title(f"Distance: {distance:.2f}")  
# 
# plt.xlim(0, 10)
# plt.ylim(0, 10)  
# plt.grid()
# plt.show()


# ------------ Vector Test ------------

# Define two vectors
# vector_a = Vector(3.0, 4.0, 1.0)
# vector_b = Vector(1.0, 2.0, 5.0)
# vector_c = Point(1.0, 2.0, 0.0).point_to_vector(Point(3.0, 4.0, 0.0))
# 
# print("\n" + "="*18 + " Vector Test " + "="*19 + "\n")
# 
# 
# print(f"Vector A: {vector_a} + Vector B: {vector_b} = {vector_a + vector_b}")
# print(f"Vector A: {vector_a} - Vector C: {vector_c} = {vector_a - vector_c}")
# 
# print("\n" + "="*50 + "\n")
# 
# dot_product = vector_a.dot(vector_b)
# cross_product = vector_a.cross(vector_b)
# print(f"Vector A: {vector_a}")
# print(f"Vector B: {vector_b}")
# print(f"Vector C (from Point A to Point B): {vector_c}")
# print(f"Dot product of Vector A and Vector B: {dot_product:.2f}")
# print(f"Cross product of Vector A and Vector B: {cross_product}")
# 
# print("\n" + "="*50 + "\n")
# 
# magnitude_a = vector_a.magnitude()
# magnitude_b = vector_b.magnitude()
# magnitude_c = vector_c.magnitude()
# print(f"Magnitude of Vector A: {magnitude_a:.2f}")
# print(f"Magnitude of Vector B: {magnitude_b:.2f}")
# print(f"Magnitude of Vector C: {magnitude_c:.2f}")
# 
# print("\n" + "="*50 + "\n")
# 
# 
# vector_b_scaled = vector_b * 0.5
# print(f"Vector B scaled by 0.5: {vector_b_scaled}")
# print(f"Original Vector B: {vector_b}")
# print(f"New magnitude of Vector B: {vector_b_scaled.magnitude():.2f}")
# 
# 
# vector_c_scaled = vector_c * 3.0
# print(f"Vector C scaled by 3: {vector_c_scaled}")
# print(f"Original Vector C: {vector_c}")
# print(f"New magnitude of Vector C: {vector_c_scaled.magnitude():.2f}")
# 
# vector_a_divided = vector_a / 2.0
# print(f"Vector A divided by 2: {vector_a_divided}") 
# print(f"Original Vector A: {vector_a}")
# print(f"New magnitude of Vector A: {vector_a_divided.magnitude():.2f}")
# 
# print("\n" + "="*50 + "\n")
# 
# vector_a_normalized = vector_a.normalize()
# print(f"Normalized Vector A: {vector_a_normalized}")
# print(f"Original Vector A: {vector_a}")
# print(f" Magnitude: {vector_a_normalized.magnitude():.2f}")
# 
# print("\n" + "="*50 + "\n")
# 
# 
# array_a = vector_a.to_array()
# print(f"Vector A as array: {array_a}")
# print(f"Vector A: {vector_a.__class__.__name__}")
# print(f"Array A: {array_a.__class__.__name__}")
# 
# print("\n" + "="*18 + " End of Test " + "="*19 + "\n")


# ------------ Line Test 2d------------

#point_x = Point(1.0, 2.0, 0.0)
point_x = Point(array=np.array([1.0, 2.0, 0.0]))
vector_X = Vector(3.0, 4.0, 0.0)
#vector_X = Vector(point = point_X)
line_1 = Line(point_x, vector_X)

test_point = Point(7.0, 6.0, 0.0)
test_vector = Vector(1.0, 1.0, 0.0)
test_line = Line(Point(3.0, 3.0, 0.0), Vector(-1.0, 5.0, 0.0))

print(f"Line 1: {line_1}")

def plot_line(lines= [], length=5.0, **kwargs):
    for line in lines:
        start = line.point - line.vector.normalize().to_point()*length
        end = line.point  + line.vector.normalize().to_point()*length
        plt.plot([start.x, end.x], [start.y, end.y], **kwargs)


fig, ax = plt.subplots()
plot_line([line_1, test_line], length=50.0, color= 'blue' , label= 'Lines')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.grid()
ax.legend()
plt.show()