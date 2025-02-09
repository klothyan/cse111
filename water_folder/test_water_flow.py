from pytest import approx
import pytest

def water_column_height(tower_height, tank_height):
    water_column = tower_height + (3 * tank_height) / 4
    return water_column

def pressure_gain_from_water_height(height):
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

# Test cases
def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9, 0.01)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, 0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, 0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, 0.001)
