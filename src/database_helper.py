import json
import os

class DatabaseHelper:
    """Handles saving and loading the UnityGrid state to JSON."""
    
    @staticmethod
    def save_to_json(centers, volunteers, file_path="data/relief_data.json"):
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Convert objects to a format JSON understands (dictionaries)
        data = {
            "centers": [
                {
                    "city": c.city,
                    "country": c.country,
                    "inventory": c.inventory
                } for c in centers
            ],
            "volunteers": volunteers
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"\n[System] Data successfully backed up to {file_path}")

    @staticmethod
    def load_from_json(file_path="data/relief_data.json"):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
