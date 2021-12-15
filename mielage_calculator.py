#program to calculate mielage

fuel_in_liters = float(input("Enter fuel in liters: "))
distance_in_km = float(input("Enter distance in km: "))
price_per_liter = float(input("Enter price per liter: "))

def calculate_mielage(fuel_in_liters,distance_in_km):
    mielage = distance_in_km/fuel_in_liters
    return mielage

mielage = calculate_mielage(fuel_in_liters,distance_in_km)
print("Mielage is: ",mielage)
print("Total cost is: ",fuel_in_liters*price_per_liter)

print("Total cost per km is: ",distance_in_km/mielage)

