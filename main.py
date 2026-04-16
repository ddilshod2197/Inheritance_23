# 23. Parkovka xarajatlari

class Parking:
    def __init__(self, parking_type, hourly_rate, hours):
        self.parking_type = parking_type    # "Ko‘cha", "Garaj", "Aeroport" va h.k.
        self.hourly_rate = hourly_rate      # $/soat
        self.hours = hours                  # to‘xtab turgan soatlar

    def total_cost(self):
        """Umumiy xarajat = soatlik tarif × soatlar soni"""
        return self.hourly_rate * self.hours

    def __str__(self):
        cost = self.total_cost()
        return f"{self.parking_type:12} | {self.hourly_rate:5.2f}$/soat | {self.hours:4} soat | {cost:7.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class StreetParking(Parking):
    def __str__(self):
        cost = self.total_cost()
        return f"🅿️ Ko‘cha     | {self.hourly_rate:4.2f}$/soat | {self.hours:3} soat → {cost:5.2f}$"


class GarageParking(Parking):
    def __str__(self):
        cost = self.total_cost()
        return f"🏢 Garaj      | {self.hourly_rate:4.2f}$/soat | {self.hours:3} soat → {cost:5.2f}$"


# Qo‘shimcha tur misoli (foydali bo‘lishi mumkin)
class AirportParking(Parking):
    def __str__(self):
        cost = self.total_cost()
        return f"✈️ Aeroport   | {self.hourly_rate:4.2f}$/soat | {self.hours:3} soat → {cost:5.2f}$"


# --------------------------------------------------
# Parkovka xarajatlarini chiqarish
# --------------------------------------------------

def show_parking_costs(parking_list):
    print("\n" + "═" * 65)
    print("       PARKOVKA XARAJATLARI HISOBI        ".center(65))
    print("═" * 65)
    print("Turi          Soatlik tarif   Vaqt     Jami xarajat")
    print("─" * 65)

    total_cost_all = 0

    for p in parking_list:
        print(p)
        total_cost_all += p.total_cost()

    print("─" * 65)
    print(f"JAMI PARKOVKA XARAJATI:                        {total_cost_all:8.2f}$")
    print("═" * 65 + "\n")


# Test ma'lumotlari
parkovkalar = [
    StreetParking("Ko‘cha (markaz)", 4.50, 2.5),
    GarageParking("Yopiq garaj", 6.00, 4),
    StreetParking("Ko‘cha (chekka)", 2.00, 6),
    GarageParking("Tungi garaj", 3.50, 10),
    AirportParking("Aeroport P1", 8.00, 48),
]

show_parking_costs(parkovkalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol parkovkalaringiz:\n")
misol_parkovkalar = [
    StreetParking("Ko‘cha", 5, 3),
    GarageParking("Garaj", 7, 2),
]

show_parking_costs(misol_parkovkalar)
