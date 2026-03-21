import numpy as np

# This module defines basic geometric entities such as points, vectors, 
# and lines, along with their operations.

class Point:

# The point class represents a point in 3D space. It has x, y, and z coordinates.    
    def __init__(self, x=0, y=0, z=0, array=None): # Allow initialization from an array
        if array is not None:
            assert isinstance(array, (list, np.ndarray)) and len(array) == 3, "Array must be a list or numpy array of length 3"
            self.x, self.y, self.z = array
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def __name__(self):
        return "point"

    def __str__(self):
        return f"point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def copy(self):
        return Point(self.x, self.y, self.z)
    
    def __add__(self, point):
        if not isinstance(point, Point):
            raise ValueError(f"Can only add a point to another point, point is of type {type(point)}")
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError(f"Can only subtract a point from another point, other is of type {type(other)}")
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only multiply a point by a scalar, scalar is of type {type(scalar)}")
        return Point(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only divide a point by a scalar, scalar is of type {type(scalar)}")
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Point(self.x / scalar, self.y / scalar, self.z / scalar)

    def to_vector(self, other):
        assert isinstance(other, Point), f"Can only convert to vector from another point, point is of type {type(other)}"
        return Vector(other.x - self.x, other.y - self.y, other.z - self.z)
    
    def as_vector(self):
        return Vector(self.x , self.y, self.z)
    
    def to_array(self):
        return np.array([self.x, self.y, self.z])
    
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise ValueError("Can only calculate distance to another point")
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def magnitude(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

class Vector:

# The vector class represents a vector in 3D space. It has x, y, and z components. Also includes 
# methods for vector operations such as addition, subtraction, scalar multiplication, 
# dot product, cross product, magnitude, and normalization. Always ensure that the vector is initialized
# with valid data, and provide error handling for invalid operations.

    def __init__(self, x=0, y=0, z=0, point=None, array=None): # Allow initialization from a point or array
        if point is not None:
            assert isinstance(point, Point), f"Point must be an instance of Point, but received {type(point)}"
            self.x = point.x
            self.y = point.y
            self.z = point.z
        elif array is not None:
            assert isinstance(array, (list, np.ndarray)) and len(array) == 3, f"Array must be a list or numpy array of length 3, but received {type(array)}"
            self.x, self.y, self.z = array
        else:
            self.x = x
            self.y = y
            self.z = z

    def __name__(self):
        return "vector"

    def __str__(self):
        return f"vector(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Can only compare with another vector, other is of type {type(other)}")
        return self.x == other.x and self.y == other.y and self.z == other.z
    def copy(self):
        return Vector(self.x, self.y, self.z)
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Can only add another vector, other is of type {type(other)}")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Can only subtract another vector, other is of type {type(other)}")
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only multiply by a scalar, scalar is of type {type(scalar)}")
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError(f"Can only divide by a scalar, scalar is of type {type(scalar)}")
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Can only calculate dot product with another vector, other is of type {type(other)}")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"Can only calculate cross product with another vector, other is of type {type(other)}")
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def magnitude(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError(f"Cannot normalize a zero vector")
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    def to_array(self):
        return np.array([self.x, self.y, self.z])
    
    def to_point(self):
        return Point(self.x, self.y, self.z)
        


class Line:

# The line class represents a line in 3D space. It is defined by a point and a direction vector.
# The line can be represented in parametric form as L(t) = point + t * vector, 
# where t is a scalar parameter.
# The line class includes methods for calculating distances to points, other lines, and planes,
# as well as methods for calculating intersections with points, other lines, and planes.

    def __init__(self, point, vector):
        assert isinstance(point, Point), f"Esperado um objeto do tipo Point, mas recebeu {type(point)}"
        assert isinstance(vector, Vector), f"Esperado um objeto do tipo Vector, mas recebeu {type(vector)}"
        self.point = Point(point.x, point.y, point.z)  # Ensure it's a point instance
        self.vector = Vector(vector.x, vector.y, vector.z)  # Ensure it's a vector instance

    def __str__(self):
        return f"line(point={self.point}, vector={self.vector})" 

    def __repr__(self):
        return self.__str__()
    
    def __name__(self):
        return "line"
    
    def __eq__(self, other):
        if not isinstance(other, Line):
            raise ValueError("Can only compare with another line")
        return np.array_equal(self.point, other.point) and np.array_equal(self.vector, other.vector)
    
    def copy(self):
        return Line(self.point.copy(), self.vector.copy())

    def distance_to_point(self, point):
        # Calculate the distance from the line to a point
        assert isinstance(point, Point), f"Expected a Point object, but received {type(point)}"
        point_vector = Vector(point.x - self.point.x, point.y - self.point.y, point.z - self.point.z)
        cross = point_vector.cross(self.vector)
        return cross.magnitude() / self.vector.magnitude()
    
    def distance_to_line(self, other):
        # Calculate the distance between two lines
        assert isinstance(other, Line), f"Expected a Line object, but received {type(other)}"
        cross = self.vector.cross(other.vector)
        if np.all(cross == 0):
            # Lines are parallel, calculate distance from one line to a point on the other line
            return self.distance_to_point(other.point)
        else:
            # Lines are not parallel, calculate distance using the formula for skew lines
            return abs((other.point - self.point).dot(cross.normalize()))

    def distance_to_plane(self, plane):
        # Calculate the distance from the line to a plane
        assert isinstance(plane, Plane), f"Expected a Plane object, but received {type(plane)}"
        numerator = abs((self.point - plane.point).dot(plane.normal))
        denominator = self.vector.dot(plane.normal)
        if denominator == 0:
            # Line is parallel to the plane
            return numerator / plane.normal.magnitude()
        else:
            return numerator / abs(denominator)
    
    def intersect_point(self, point):  
        # Calculate the intersection of the line with a point
        assert isinstance(point, Point), f"Expected a Point object, but received {type(point)}"
        if self.distance_to_point(point) == 0:
            return point  # The point lies on the line
        else:
            return None  # No intersection, the point is not on the line
        
    def intersect_line(self, other):
        if not isinstance(other, Line):
            raise ValueError(f"Can only intersect with another line, other is of type {type(other)}")
        
        # Calculate the cross product of the direction vectors
        cross = self.vector.cross(other.vector)
        
        # If the cross product is zero, the lines are parallel
        if np.all(cross == 0):
            return None
        
        # Calculate the intersection point using Cramer's rule
        A = np.array([self.vector, -other.vector]).T # Transpose to get the correct shape for solving
        b = self.point.to_array() - other.point.to_array() # Vector from self.point to other.point
        
        try:
            t = np.linalg.solve(A, b)
            intersection_point = self.point + t[0] * self.vector
            return intersection_point
        except np.linalg.LinAlgError:
            return None
    
    def intersect_plane(self, plane):
        if not isinstance(plane, Plane):
            raise ValueError(f"Can only intersect with a plane, other is of type {type(plane)}")
        
        # Calculate the dot product of the line's direction vector and the plane's normal vector
        dot_product = self.vector.dot(plane.normal)
        
        # If the dot product is zero, the line is parallel to the plane
        if dot_product == 0:
            return None
        
        # Calculate the intersection point using the formula for line-plane intersection
        t = (plane.point - self.point).dot(plane.normal) / dot_product
        intersection_point = self.point + t * self.vector
        return intersection_point

class Plane:

# The plane class represents a plane in 3D space. It is defined by a point and a normal vector.
# The plane can be represented in the form of the equation Ax + By + Cz + D
# where (A, B, C) is the normal vector and D is the distance from the origin to the plane along the normal vector.
# The plane class includes methods for calculating distances to points, lines, and other planes,
# as well as methods for calculating intersections with points, lines, and other planes.

    def __init__(self, point, normal=None, line=None):
        if line is not None:
            assert isinstance(line, Line), f"Expected a line object, but received {type(line)}"
            assert isinstance(point, Point), f"Expected point to be a Point object, but received {type(point)}"
            self.point = Point(line.point.x, line.point.y, line.point.z)  # Use the point from the line
            self.normal = Vector(-line.vector.y, line.vector.x, 0).normalize()  # Create a normal vector perpendicular to the line
        else:
            self.point = Point(point.x, point.y, point.z)  # Ensure it's a point instance
            self.normal = Vector(normal.x, normal.y, normal.z).normalize()  # Ensure it's a normalized vector instance

    def __str__(self):
        return f"plane(point={self.point}, normal={self.normal})"

    def __repr__(self):
        return self.__str__()
    
    def __name__(self):
        return "plane"
    
    def __eq__(self, other):
        if not isinstance(other, Plane):
            raise ValueError(f"Can only compare with another plane. other is of type {type(other)}")
        return np.array_equal(self.point, other.point) and np.array_equal(self.normal, other.normal)
    
    def copy(self):
        return Plane(self.point.copy(), self.normal.copy())
    
    def distance_to_point(self, point):
        # Calculate the distance from the plane to a point
        assert isinstance(point, Point), f"Expected a Point object, but received {type(point)}"
        return abs((point - self.point).dot(self.normal))
    
    def distance_to_line(self, line):
        # Calculate the distance from the plane to a line
        assert isinstance(line, Line), f"Expected a Line object, but received {type(line)}"
        return line.distance_to_plane(self)
    
    def distance_to_plane(self, other):
        # Calculate the distance between two planes
        assert isinstance(other, Plane), f"Expected a Plane object, but received {type(other)}"
        if np.all(self.normal == other.normal):
            # Planes are parallel, calculate distance from one plane to a point on the other plane
            return self.distance_to_point(other.point)
        else:
            # Planes are not parallel, they intersect along a line, so the distance is zero
            return 0
            
    def intersect_point(self, point):
        # Calculate the intersection of the plane with a point
        assert isinstance(point, Point), f"Expected a Point object, but received {type(point)}"
        if self.distance_to_point(point) == 0:
            return point  # The point lies in the plane
        else:
            return None  # No intersection, the point is not in the plane
        
    def intersect_line(self, line):
        # Calculate the intersection of the plane with a line
        assert isinstance(line, Line), f"Expected a Line object, but received {type(line)}"
        if self.distance_to_line(line) == 0:
            # Line is parallel to the plane, check if it lies in the plane
            if self.distance_to_point(line.point) == 0:
                return line  # The line lies in the plane
            else:
                return None  # No intersection, the line is parallel and does not lie in the plane
        else:
            # Line is not parallel to the plane, calculate the intersection point
            t = (self.point - line.point).dot(self.normal) / line.vector.dot(self.normal)
            intersection_point = line.point + t * line.vector
            return intersection_point
        
    def intersect_plane(self, other):
        # Calculate the intersection of two planes
        assert isinstance(other, Plane), f"Expected a Plane object, but received {type(other)}"
        if self.distance_to_plane(other) == 0:
            # Planes are parallel, check if they are the same plane
            if self.distance_to_point(other.point) == 0:
                return self  # The planes are the same
            else:
                return None  # No intersection, the planes are parallel and do not coincide
        else:
            # Planes are not parallel, calculate the line of intersection
            direction = self.normal.cross(other.normal).normalize()
            point_on_line = self.intersect_line(Line(self.point, direction))
            return Line(point_on_line, direction)