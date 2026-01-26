import json
import os
import random

class ReliefCenter:
    def __init__(self, city, country, region, capacity):
        self.city = city
        self.country = country
        self.region = region
        # Simulate "Real-Time" Inventory
        self.inventory = {
            "Water (Liters)": random.randint(1000, 50000),
            "Medical Kits": random.randint(50, 5000),
            "Food Parcels": random.randint(200, 10000),
            "Blankets": random.randint(100, 2000),
            "Tents": random.randint(10, 500)
        }
        self.capacity = capacity

class UnityGridEngine:
    def __init__(self):
        self.centers = []
        self.volunteers = []
        self.load_mock_global_data()

    def load_mock_global_data(self):
        # A list of major global hubs to simulate "All Cities" coverage
        global_hubs = [
            ("Istanbul", "Turkey", "Eurasia"), ("Gaziantep", "Turkey", "Middle East"),
            ("New York", "USA", "North America"), ("London", "UK", "Europe"),
            ("Berlin", "Germany", "Europe"), ("Tokyo", "Japan", "Asia"),
            ("Seoul", "South Korea", "Asia"), ("Sydney", "Australia", "Oceania"),
            ("Cairo", "Egypt", "Africa"), ("Nairobi", "Kenya", "Africa"),
            ("Sao Paulo", "Brazil", "South America"), ("Mexico City", "Mexico", "North America"),
            ("Mumbai", "India", "Asia"), ("Dubai", "UAE", "Middle East"),
            ("Toronto", "Canada", "North America"), ("Paris", "France", "Europe")
        ]
        
        for city, country, region in global_hubs:
            self.centers.append(ReliefCenter(city, country, region, "High"))

    def update_inventory(self, city_name, item, qty):
        for center in self.centers:
            if center.city == city_name:
                if item in center.inventory:
                    center.inventory[item] += qty
                else:
                    center.inventory[item] = qty

    def save_state(self):
        # In a real app, this saves to a database. 
        # Here we just pass because we are regenerating data on load for the demo.
        pass
