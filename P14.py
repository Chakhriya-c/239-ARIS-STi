def rain_water(area_rai, rain_density_mm_per_hour, raining_hours):
    area_sq_m = area_rai * 1600
    
    total_rainfall_mm = rain_density_mm_per_hour * raining_hours
    
    total_rain_water_liters = total_rainfall_mm * area_sq_m
    
    return total_rain_water_liters

area = input('Area name:')
print('{}: rain water = {:,.2f} L'.format(area, rain_water(
float(input('Size of the area (in rai):')),
float(input('The area rain density (in mm/h):')), 

float(input('The number of raining hours:'))
)))