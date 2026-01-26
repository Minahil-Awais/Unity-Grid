import random

class EmergencyRegistry:
    """
    A collection of global emergency contact numbers.
    Numbers are stored as strings to maintain formatting.
    """
    contacts = {
        "Afghanistan": {"Police": "119", "Ambulance": "102", "Fire": "119"},
        "Australia": {"Police": "000", "Ambulance": "000", "Fire": "000"},
        "Brazil": {"Police": "190", "Ambulance": "192", "Fire": "193"},
        "Canada": {"Police": "911", "Ambulance": "911", "Fire": "911"},
        "China": {"Police": "110", "Ambulance": "120", "Fire": "119"},
        "France": {"Police": "17", "Ambulance": "15", "Fire": "18"},
        "Germany": {"Police": "110", "Ambulance": "112", "Fire": "112"},
        "India": {"Police": "112", "Ambulance": "112", "Fire": "112"},
        "Japan": {"Police": "110", "Ambulance": "119", "Fire": "119"},
        "Mexico": {"Police": "911", "Ambulance": "911", "Fire": "911"},
        "Pakistan": {"Police": "15", "Ambulance": "115", "Fire": "16"},
        "South Africa": {"Police": "10111", "Ambulance": "10177", "Fire": "10177"},
        "UAE": {"Police": "999", "Ambulance": "998", "Fire": "997"},
        "UK": {"Police": "999", "Ambulance": "999", "Fire": "999"},
        "USA": {"Police": "911", "Ambulance": "911", "Fire": "911"}
    }
class UnityGridEngine:
    def __init__(self):
        # 1. THE COMPLETE GLOBAL DATABASE (195 Countries)
        self.world_data = {
            "Africa": [
                "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
                "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)", "DR Congo", "Côte d'Ivoire", 
                "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", 
                "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", 
                "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", 
                "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
                "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
            ],
            "Asia": [
                "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", 
                "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", 
                "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", 
                "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", 
                "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand", 
                "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"
            ],
            "Europe": [
                "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", 
                "Croatia", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", 
                "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", 
                "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", 
                "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", 
                "Ukraine", "United Kingdom", "Vatican City"
            ],
            "North America": [
                "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", 
                "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", 
                "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
                "Trinidad and Tobago", "United States"
            ],
            "South America": [
                "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", 
                "Suriname", "Uruguay", "Venezuela"
            ],
            "Oceania": [
                "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", 
                "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
            ]
        }
        self.volunteers = []

    def get_inventory(self, country):
        """Generates professional mock inventory data for a country."""
        random.seed(country) 
        return {
            "Potable Water (L)": random.randint(10000, 500000),
            "Trauma Kits": random.randint(500, 10000),
            "MREs (Meals)": random.randint(2000, 100000),
            "Field Tents": random.randint(100, 5000),
            "Power Generators": random.randint(10, 500)
        }

    def get_disaster_zones(self):
        """
        Generates lat/lon coordinates for the map to simulate 
        Earthquakes (Red) and Tsunamis (Green).
        """
        zones = []
        # Simulate Earthquake Zones (Red) - Ring of Fire, Turkey, etc.
        eq_coords = [(36.2, 36.1), (35.6, 139.6), (-6.2, 106.8), (34.0, -118.2), (-33.4, -70.6), (27.7, 85.3)]
        for lat, lon in eq_coords:
            zones.append({"lat": lat, "lon": lon, "type": "Earthquake Risk", "color": "red", "radius": 15})
            
        # Simulate Tsunami/Flood Zones (Green) - Coastal Areas
        ts_coords = [(6.9, 79.8), (14.5, 120.9), (-18.1, 178.4), (13.7, 100.5), (25.7, -80.1)]
        for lat, lon in ts_coords:
            zones.append({"lat": lat, "lon": lon, "type": "Tsunami/Flood Risk", "color": "#00FF00", "radius": 12})
            
        return zones
