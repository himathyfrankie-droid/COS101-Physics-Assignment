# COS 101 Assignment
# Five Physics Formulas

def speed(distance, time):
    return distance / time

def force(mass, acceleration):
    return mass * acceleration

def density(mass, volume):
    return mass / volume

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def potential_energy(mass, gravity, height):
    return mass * gravity * height

print("Speed:", speed(100, 5), "m/s")
print("Force:", force(10, 5), "N")
print("Density:", density(20, 4), "kg/m³")
print("Kinetic Energy:", kinetic_energy(10, 5), "J")
print("Potential Energy:", potential_energy(10, 9.8, 8), "J")