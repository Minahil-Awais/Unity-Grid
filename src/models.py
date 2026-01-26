import random

class UnityGridEngine:
    def __init__(self):
        # Professional Hierarchical Data Structure
        self.world_data = {
            "Asia": {
                "Turkey": ["Istanbul", "Ankara", "Gaziantep", "Antakya", "Izmir"],
                "Japan": ["Tokyo", "Osaka"],
                "Pakistan": ["Islamabad", "Peshawar"]
            },
            "Europe": {
                "Germany": ["Berlin", "Munich"],
                "France": ["Paris", "Lyon"],
                "UK": ["London", "Manchester"]
            },
            "Americas": {
                "USA": ["New York", "Los Angeles"],
                "Brazil": ["Sao Paulo", "Rio de Janeiro"],
                "Canada": ["Toronto", "Vancouver"]
            },
            "Africa": {
                "Egypt": ["Cairo"],
                "Kenya": ["Nairobi"],
                "South Africa": ["Cape Town"]
            }
        }
        self.volunteers = []

    def get_inventory(self, city):
        """Simulates real-time inventory for any city."""
        random.seed(city) # Keeps numbers consistent for the same city
        return {
            "Water (L)": random.randint(5000, 100000),
            "Medical": random.randint(100, 5000),
            "Food": random.randint(500, 20000),
            "Personnel": random.randint(10, 250)
        }
