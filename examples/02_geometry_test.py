from reference_engine.geometry import Point, Vector, Line
import matplotlib.pyplot as plt
# Example usage of geometry functions, could be used on a 
# jupyter notebook or as a standalone script to test the geometry module.


# ------------ Point Test ------------
# Define two points
point_a = Point(1.0, 2.0, 0.0)
point_b = Point(3.0, 4.0, 0.0)

distance = point_a.distance_to(point_b)

print(f"Distance between point A and point B: {distance}")
# Plot the points and the distance between them
plt.figure()
plt.plot([point_a.x, point_b.x], [point_a.y, point_b.y], 'ro-')
plt.text(point_a.x, point_a.y, 'A', fontsize=12, ha='right')
plt.text(point_b.x, point_b.y, 'B', fontsize=12, ha='left')
plt.title(f"Distance: {distance:.2f}")  

plt.xlim(0, 4)
plt.ylim(0, 5)  
plt.grid()
plt.show()


# ------------ Vector Test ------------
