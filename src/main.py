from models import UnityGridEngine
import sys

def main():
    # This now loads existing data from your JSON file automatically
    engine = UnityGridEngine()
    
    while True:
        print("\n" + "◈" * 45)
        print("      UNITYGRID: GLOBAL DISASTER RESPONSE      ")
        print("" + "◈" * 45)
        print("1. Global Inventory Overview")
        print("2. Log Incoming Aid (Supply Update)")
        print("3. Register Humanitarian Volunteer")
        print("4. Emergency Specialist Search")
        print("5. Save and Exit System") # Updated label
        
        choice = input("\n[Admin Selection] > ")

        if choice == '1':
            print("\n--- GLOBAL STOCK STATUS ---")
            for c in engine.centers:
                print(f"📍 {c.city}, {c.country} | {c.inventory}")

        elif choice == '2':
            city = input("Target City: ")
            print("Items: 1. Water (Liters) | 2. Medical Kits | 3. Food Parcels")
            item_map = {"1": "Water (Liters)", "2": "Medical Kits", "3": "Food Parcels"}
            item_choice = input("Select Item #: ")
            qty = int(input("Quantity to add: "))
            
            if engine.update_inventory(city, item_map.get(item_choice), qty):
                print(f"✅ Logistics Updated: {city} received supplies.")
            else:
                print("❌ Location not recognized in the Grid.")

        elif choice == '3':
            name = input("Volunteer Name: ")
            spec = input("Specialty (Medical/Logistics/Rescue): ")
            contact = input("Contact/Email: ")
            # Using the engine to handle adding to maintain clean architecture
            engine.volunteers.append({"name": name, "spec": spec, "contact": contact})
            print(f"✅ {name} added to Global Response Team.")

        elif choice == '4':
            search_spec = input("Search for specialty: ").lower()
            results = [v for v in engine.volunteers if v['spec'].lower() == search_spec]
            print(f"\n--- Results for {search_spec.capitalize()} ---")
            if not results:
                print("No specialists found for that category.")
            for r in results:
                print(f"👤 {r['name']} | 📞 {r['contact']}")

        elif choice == '5':
            # IMPORTANT: This saves your work to data/relief_data.json
            print("Saving data...")
            engine.save_state() 
            print("Terminating UnityGrid Secure Session. Goodbye!")
            break

if __name__ == "__main__":
    main()
