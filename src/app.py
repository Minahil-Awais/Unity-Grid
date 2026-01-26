import streamlit as st
from models import UnityGridEngine

# 1. Page Configuration
st.set_page_config(page_title="UnityGrid Global", page_icon="🌍", layout="wide")

# 2. Custom CSS for "Aesthetic" Styling
st.markdown("""
    <style>
    .main {
        background-color: #F8F9FA;
    }
    .stSelectbox label {
        color: #1B263B !important;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #415A77;
        color: white;
    }
    .hero-text {
        text-align: center;
        color: #1B263B;
        font-family: 'Helvetica Neue', sans-serif;
    }
    </style>
    """, unsafe_allow_stdio=True)

# 3. Initialize Engine
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
engine = st.session_state.engine

# 4. TOP CONTROL PANEL (Drop-down Menu)
st.markdown("<h1 class='hero-text'>🌍 UNITYGRID</h1>", unsafe_allow_stdio=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    choice = st.selectbox("", ["Home / Overview", "📊 Logistics Dashboard", "📦 Update Supplies", "🤝 Register Volunteer", "🔍 Specialist Search"], label_visibility="collapsed")

st.markdown("---")

# 5. PAGE CONTENT
if choice == "Home / Overview":
    # Hero Image & Welcome
    st.image("https://images.unsplash.com/photo-1593113503872-e4418c9bb70e?auto=format&fit=crop&w=1200&q=80", use_column_width=True)
    
    st.markdown("""
        <div class='hero-text'>
            <h2>Unifying Global Logistics for a Safer World</h2>
            <p style='font-size: 1.2em; color: #777;'>UnityGrid streamlines humanitarian aid deployment across international hubs, 
            bridging the gap between resources and those in need.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats Row
    c1, c2, c3 = st.columns(3)
    c1.metric("Active Hubs", len(engine.centers))
    c2.metric("Total Volunteers", len(engine.volunteers))
    c3.metric("Status", "Operational", delta="Secure")

elif choice == "📊 Logistics Dashboard":
    st.subheader("Global Resource Hub Status")
    data = [{"City": c.city, "Country": c.country, **c.inventory} for c in engine.centers]
    st.table(data)

elif choice == "📦 Update Supplies":
    st.subheader("Inventory Management")
    with st.container():
        city = st.selectbox("Target City", [c.city for c in engine.centers])
        item = st.selectbox("Resource", ["Water (Liters)", "Medical Kits", "Food Parcels"])
        qty = st.number_input("Quantity", min_value=1)
        if st.button("Confirm Supply Drop"):
            engine.update_inventory(city, item, qty)
            engine.save_state()
            st.success(f"Logistics updated for {city}.")

elif choice == "🤝 Register Volunteer":
    st.subheader("Humanitarian Intake")
    name = st.text_input("Full Name")
    spec = st.selectbox("Specialty", ["Medical", "Rescue", "Logistics"])
    contact = st.text_input("Contact Info")
    if st.button("Add to Database"):
        engine.volunteers.append({"name": name, "spec": spec, "contact": contact})
        engine.save_state()
        st.balloons()

elif choice == "🔍 Specialist Search":
    st.subheader("Search the Global Network")
    search = st.text_input("Enter specialty (e.g. Medical)").lower()
    if search:
        results = [v for v in engine.volunteers if v['spec'].lower() == search]
        for r in results:
            st.info(f"👤 {r['name']} | {r['contact']}")
