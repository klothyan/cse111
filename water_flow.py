def water_column_height(tower_height, tank_height):
    water_column = tower_height + (3 * tank_height) / 4
    return water_column

# Example usage
if __name__ == "__main__":
    tower_height = 50  # in meters
    tank_height = 20   # in meters

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity pulling on the water stored in an elevated tank.

    Parameters:
    height (float): The height of the water column in meters.

    Returns:
    float: The pressure in kilopascals (kPa).
    """
    density_of_water = 998.2  # in kg/m^3
    gravity = 9.80665         # in m/s^2
    pressure = (density_of_water * gravity * height) / 1000  # Convert to kPa
    return pressure


# Example usage
if __name__ == "__main__":
    tower_height = 50  # in meters
    tank_height = 20   # in meters

    total_height = water_column_height(tower_height, tank_height)
    print(f"The height of the water column is {total_height} meters.")

    pressure = pressure_gain_from_water_height(total_height)
    print(f"The pressure from the water column is {pressure:.2f} kPa.")


# Test function
def test_water_column_height():
    """
    Test the water_column_height function with multiple test cases.
    """
    water_column_height(0, 0)
    water_column_height(0, 10)
    water_column_height(25, 0)
    water_column_height(48.3, 12.8)


def test_pressure_gain_from_water_height():
    """
    Test the pressure_gain_from_water_height function with multiple test cases.
    """
    pressure_gain_from_water_height(0)
    pressure_gain_from_water_height(7.5)
    pressure_gain_from_water_height(25)
    pressure_gain_from_water_height(57.9)


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    density_of_water = 998.2  # in kg/m^3
    pressure_loss = -(friction_factor * pipe_length * density_of_water * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss



# Run tests
if __name__ == "__main__":
    test_water_column_height()
    test_pressure_gain_from_water_height()


