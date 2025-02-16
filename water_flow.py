def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    density_of_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density_of_water * gravity * height) / 1000  # Convert to kPa

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    density_of_water = 998.2  # kg/m^3
    return -friction_factor * (length / diameter) * (density_of_water * velocity**2 / 2) / 1000  # Convert to kPa

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_of_water = 998.2  # kg/m^3
    return (-0.04 * density_of_water * fluid_velocity ** 2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_of_water = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016  # Pa·s
    return (density_of_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_of_water = 998.2  # kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return (-k * density_of_water * fluid_velocity ** 2) / 2000

if __name__ == "__main__":
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    pipe_length_lot = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    pipe_length_house = float(input("Length of pipe from supply to house (meters): "))

    total_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(total_height)
    pressure -= pressure_loss_from_pipe(0.28687, pipe_length_lot, 0.013, 1.65)
    pressure -= pressure_loss_from_fittings(1.65, num_fittings)
    pressure -= pressure_loss_from_pipe(0.28687, pipe_length_house, 0.013, 1.65)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
