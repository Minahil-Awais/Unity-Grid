import json
import os

class AidCenter:
    """Represents a global hub for resource distribution."""
    def __init__(self, city, country, water=0, medical_kits=0, food_parcels=0):
        self.city = city
        self.country = country
        self.inventory = {
            "Water (Liters)": water,
            "Medical Kits": medical_kits,
            "Food Parcels": food_parcels
        }

class VolunteerSpecialist:
    """Represents a skilled responder available for deployment."""
    def __init__(self, name, specialty, contact):
        self.name = name
        self.specialty = specialty.capitalize() # e.g., Surgeon, Engineer, Pilot
        self.contact = contact

class UnityGridEngine:
    """The central management system for global coordination."""
    def __init__(self):
        self.centers = [
            AidCenter("Istanbul", "Türkiye", 5000, 200, 1000),
            AidCenter("Antakya", "Türkiye", 3000, 500, 800),
            AidCenter("Tokyo", "Japan", 4500, 300, 1200),
            AidCenter("Beirut", "Lebanon", 2000, 150, 600),
            AidCenter("Mexico City", "Mexico", 3500, 250, 900)
        ]
        self.volunteers = []

    def update_inventory(self, city_name, item, amount):
        for center in self.centers:
            if center.city.lower() == city_name.lower():
                if item in center.inventory:
                    center.inventory[item] += amount
                    return True
        return False
