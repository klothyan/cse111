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

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    density_of_water = 998.2  # in kg/m^3
    pressure_loss = -friction_factor * (length / diameter) * (density_of_water * velocity**2 / 2) / 1000  # Convert to kPa
    return pressure_loss

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

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

# Call the main function for pytest
pytest.main(["-v", "--tb=line", "-rN", __file__])
