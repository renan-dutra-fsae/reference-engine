import numpy as np

# The World class represents a physical simulation environment that contains multiple bodies and a global reference frame.
from reference_engine import Frame
from reference_engine.body import Particle, RigidBody
from reference_engine import Integrator
from reference_engine import Force
from reference_engine.geometry import Vector,Point
from reference_engine.constraints import PositionConstraint

# The World class manages the collection of bodies and forces, and provides a method to advance the simulation by a time step.
# The step method applies all forces to their associated bodies, updates the state of each body using the integrator, and increments the simulation time.
# The add_particle and add_rigid_body methods allow users to create and add new bodies to the world, while the add_force method allows users to apply forces to the bodies in the simulation.
# The World class serves as the central hub for managing the simulation and coordinating the interactions between bodies and forces.

class World:

    def __init__(self, world_origin=None):

        self.solver_iterations  = 10
        self.forces = []
        self.bodies = []  # Should diffentiate bodies from particles later
        self.constraints = []
        self.time = 0.0
        self.integrator = Integrator()
        self.world_frame = Frame("World", world_origin if world_origin is not None else np.zeros(3))

    def set_solver_iterations(self, iterations):
        self.solver_iterations = iterations

    def add_particle(self, body_name, mass=0.0, position=None, velocity=None):
        particle = Particle(body_name, mass, position, velocity)
        self.bodies.append(particle)
        return particle

    def add_rigid_body(self, body_name, mass=0.0, parent_frame=None, origin=None, angular_velocity=None):
        body = RigidBody(body_name, mass, parent_frame, origin, angular_velocity)
        self.bodies.append(body)
        return body

    def add_force(self, force):
        if not isinstance(force, Force):
            raise ValueError(f"Force must be of type Force, got {type(force)}")
        self.forces.append(force)

    def add_position_constraint(self, constraint_name, p1=None, p2=None, rest_length=0.0):
        assert isinstance(p1, Particle), f"p1 must be a Particle, got {type(p1)}"
        assert isinstance(p2, Particle), f"p2 must be a Particle, got {type(p2)}"
        constraint = PositionConstraint(constraint_name, p1, p2, rest_length)
        self.constraints.append(constraint)

    def step(self, dt):
        for p in self.bodies:
            p.prev_position = p.position.copy()

        for body in self.bodies: #Clear forces on each body before applying new forces
            body.clear_forces()

        for force in self.forces: #Apply each force to its associated bodies
            force.apply()

        for body in self.bodies: #Integrate motion of each body
            self.integrator.step(body, dt)
        
        for _ in range(self.solver_iterations): #Iteratively solve constraints (simple Gauss-Seidel style)
            for constraint in self.constraints:
                constraint.solve()

        self.time += dt