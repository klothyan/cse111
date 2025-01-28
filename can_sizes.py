import math

def main():
    
    print(f"#1 Picnic {storage_efficiency(compute_surface_area(6.83,10.16),compute_volume(6.83,10.16))}")
    print(f"#1 Tall {storage_efficiency(compute_surface_area(7.78, 11.91),compute_volume(7.78, 11.91))}")
    print(f"#2 {storage_efficiency(compute_surface_area(8.73,11.59),compute_volume(8.73,11.59))}")
    print(f"#2.5 {storage_efficiency(compute_surface_area(10.32, 11.91),compute_volume(10.32, 11.91))}")
    print(f"#3 Cylinder {storage_efficiency(compute_surface_area(10.79,17.78),compute_volume(10.79,17.78))}")
    print(f"#5 {storage_efficiency(compute_surface_area(13.02, 14.299),compute_volume(13.02,14.29))}")
    print(f"#6Z {storage_efficiency(compute_surface_area(5.4, 8.89),compute_volume(5.4, 8.89))}")
    print(f"#8Z short {storage_efficiency(compute_surface_area(6.83, 7.62),compute_volume(6.83, 7.62))}")
    print(f"#10 {storage_efficiency(compute_surface_area(15.72, 17.78),compute_volume(15.72, 17.78))}")
    print(f"#211 {storage_efficiency(compute_surface_area(6.83, 12.38),compute_volume(6.83, 12.38))}")
    print(f"#300 {storage_efficiency(compute_surface_area(7.62, 11.27),compute_volume(7.62, 11.27))}")
    print(f"#303 {storage_efficiency(compute_surface_area(8.1, 11.11),compute_volume(8.1, 11.11))}")







def compute_volume(radius,height):
    return (math.pi * radius * radius * height)




def compute_surface_area(radius , heigth):
    surface_area = 2 * math.pi * radius * (radius + heigth)

    return (surface_area)

    
def storage_efficiency(surface_area, volume):
    return round(volume/surface_area , 2)

    

main()