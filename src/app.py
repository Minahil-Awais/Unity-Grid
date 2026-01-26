import streamlit as st
from models import UnityGridEngine

# Page Setup
st.set_page_config(page_title="UnityGrid Global", page_icon="🌍", layout="wide")

# Initialize the Engine
# We use 'toggle' to ensure the engine stays active across clicks
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()

engine = st.session_state.engine

# Header
st.title("🌍 UnityGrid: Humanitarian Coordination")
st.markdown("---")

# Sidebar Navigation
st.sidebar.header("Control Panel")
menu = ["📊 Dashboard", "📦 Log Incoming Aid", "🤝 Volunteer Registry", "🔍 Emergency Search"]
choice = st.sidebar.radio("Navigate", menu)

if choice == "📊 Dashboard":
    st.subheader("Global Resource Hub Status")
    # Convert data for a professional table
    data = [{"City": c.city, "Country": c.country, **c.inventory} for c in engine.centers]
    st.table(data)

elif choice == "📦 Log Incoming Aid":
    st.subheader("Update Logistics")
    with st.form("supply_form"):
        city = st.selectbox("Select Target City", [c.city for c in engine.centers])
        item = st.selectbox("Resource Type", ["Water (Liters)", "Medical Kits", "Food Parcels"])
        qty = st.number_input("Amount Received", min_value=1, step=1)
        submit = st.form_submit_button("Update Inventory")
        
        if submit:
            engine.update_inventory(city, item, qty)
            engine.save_state()
            st.success(f"Confirmed: {qty} units of {item} added to {city} hub.")

elif choice == "🤝 Volunteer Registry":
    st.subheader("Register New Specialist")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        spec = st.selectbox("Expertise", ["Medical", "Search & Rescue", "Logistics", "Translation", "Engineering"])
    with col2:
        contact = st.text_input("Contact (Email/Phone)")
        
    if st.button("Add to Global Team"):
        if name and contact:
            engine.volunteers.append({"name": name, "spec": spec, "contact": contact})
            engine.save_state()
            st.toast(f"Successfully registered {name}!", icon="✅")
        else:
            st.error("Please fill in all fields.")

elif choice == "🔍 Emergency Search":
    st.subheader("Find Available Specialists")
    search_query = st.text_input("Search by Specialty (e.g., Medical)").lower()
    
    if search_query:
        results = [v for v in engine.volunteers if v['spec'].lower() == search_query]
        if results:
            for r in results:
                st.info(f"👤 **{r['name']}** | Specialty: {r['spec']} | Contact: {r['contact']}")
        else:
            st.warning("No specialists found for that category.")
