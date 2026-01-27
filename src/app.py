import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random

# ==========================================
# 0. MOCK DATA CLASSES (To ensure standalone functionality)
# ==========================================
class UnityGridEngine:
    def __init__(self):
        self.world_data = {
            "Asia": ["Japan", "India", "China", "Türkiye", "Lebanon"],
            "Europe": ["Germany", "France", "Italy", "Ukraine"],
            "North America": ["USA", "Canada", "Mexico"],
            "South America": ["Brazil", "Chile", "Peru"],
            "Africa": ["Egypt", "South Africa", "Morocco"]
        }
        self.inventory_db = {
            "Japan": {"Medical Kits": 1200, "Blankets": 5000, "Water (L)": 15000, "Generators": 80},
            "Türkiye": {"Medical Kits": 3500, "Blankets": 12000, "Water (L)": 45000, "Generators": 150},
            "USA": {"Medical Kits": 8000, "Blankets": 25000, "Water (L)": 100000, "Generators": 500},
        }

    def get_disaster_zones(self):
        # Lat/Lon for visual map
        return [
            {"lat": 36.20, "lon": 36.16, "risk": "High", "type": "Earthquake", "radius": 15, "color": "#FF4B4B"}, # Antakya
            {"lat": 35.67, "lon": 139.65, "risk": "Moderate", "type": "Tsunami Warning", "radius": 10, "color": "#FFA500"}, # Tokyo
            {"lat": 33.89, "lon": 35.50, "risk": "Critical", "type": "Supply Shortage", "radius": 8, "color": "#FF4B4B"}, # Beirut
            {"lat": 28.61, "lon": 77.20, "risk": "High", "type": "Heat Wave", "radius": 12, "color": "#FFA500"}, # Delhi
            {"lat": 19.43, "lon": -99.13, "risk": "Moderate", "type": "Seismic", "radius": 10, "color": "#FFFF00"}, # Mexico City
            {"lat": -6.20, "lon": 106.84, "risk": "High", "type": "Flood", "radius": 14, "color": "#FF4B4B"}, # Jakarta
        ]

    def get_inventory(self, country):
        # O(1) Lookup logic as per Technical Profile
        if country in self.inventory_db:
            return self.inventory_db[country]
        return {"Medical Kits": random.randint(100, 1000), "Blankets": random.randint(500, 5000), "Water (L)": random.randint(1000, 10000), "Generators": random.randint(5, 50)}

class EmergencyRegistry:
    contacts = {
        "USA": {"Police": 911, "Ambulance": 911, "Fire": 911},
        "UK": {"Police": 999, "Ambulance": 999, "Fire": 999},
        "Türkiye": {"Police": 155, "Ambulance": 112, "Fire": 110, "AFAD": 122},
        "Japan": {"Police": 110, "Ambulance": 119, "Fire": 119},
        "India": {"Police": 100, "Ambulance": 102, "Fire": 101},
        "France": {"Police": 17, "Ambulance": 15, "Fire": 18},
        "Germany": {"Police": 110, "Ambulance": 112, "Fire": 112},
        "China": {"Police": 110, "Ambulance": 120, "Fire": 119},
    }

# ==========================================
# 1. PAGE CONFIGURATION & STATE
# ==========================================
st.set_page_config(page_title="Unity Grid Global", page_icon="🌐", layout="wide")

if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'lang' not in st.session_state:
    st.session_state.lang = "English"

# Translations for Nav Elements
translations = {
    "English": {"aware": "AWARENESS", "act": "TAKE ACTION", "menu": "MENU"},
    "Turkish": {"aware": "FARKINDALIK", "act": "HAREKETE GEÇ", "menu": "MENÜ"},
    "Spanish": {"aware": "CONCIENCIA", "act": "TOMAR ACCIÓN", "menu": "MENÚ"},
    "French": {"aware": "SENSIBILISATION", "act": "AGIR", "menu": "MENU"},
}
t = translations.get(st.session_state.lang, translations["English"])

# ==========================================
# 2. CSS STYLING
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');
    
    :root {
        --primary: #263E3A; 
        --accent: #945031;
        --light: #F4F4F4;
    }

    .stApp { background-color: white; font-family: 'Montserrat', sans-serif; }
    
    /* Header Styling */
    .header-container { padding-bottom: 20px; border-bottom: 1px solid #ddd; margin-bottom: 30px; }
    .logo-title { font-size: 36px; font-weight: 800; color: var(--primary); letter-spacing: -1px; }
    .logo-sub { color: var(--accent); }

    /* Hero Section */
    .hero-quote { 
        font-size: 48px; 
        font-weight: 800; 
        color: var(--primary); 
        line-height: 1.1; 
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .hero-text {
        font-size: 18px;
        color: #555;
        line-height: 1.6;
        margin-bottom: 30px;
        border-left: 5px solid var(--accent);
        padding-left: 15px;
    }

    /* Button Overrides */
    .stButton button {
        background-color: var(--primary);
        color: white;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: var(--accent);
        transform: scale(1.02);
    }

    /* Info Box */
    .info-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid var(--primary);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER & NAVIGATION
# ==========================================
col_logo, col_nav = st.columns([1, 2])

with col_logo:
    # Logo and Title Top Left
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 15px;">
            <svg width="50" height="50" viewBox="0 0 100 100">
                 <circle cx="50" cy="50" r="45" stroke="#263E3A" stroke-width="8" fill="none" />
                 <path d="M50 5 L50 95 M5 50 L95 50" stroke="#945031" stroke-width="8" />
                 <circle cx="50" cy="50" r="15" fill="#263E3A" />
            </svg>
            <div class="logo-title">UNITY <span class="logo-sub">GRID</span></div>
        </div>
    """, unsafe_allow_html=True)

with col_nav:
    # Navigation Buttons Top Right
    c1, c2, c3, c4 = st.columns([1, 1, 1.5, 1])
    
    # 1. Awareness Button
    if c1.button(t['aware'], use_container_width=True):
        st.session_state.page = "Awareness"
        st.rerun()
        
    # 2. Take Action Button (Goes to Volunteer)
    if c2.button(t['act'], use_container_width=True):
        st.session_state.page = "Volunteer"
        st.rerun()

    # 3. Menu Dropdown
    with c3:
        # We use a selectbox that acts as a navigator
        menu_options = [t['menu'], "Home", "Global Ops", "Precautionary", "Emergency Contacts"]
        selected_menu = st.selectbox("Navigation", menu_options, label_visibility="collapsed")
        
        if selected_menu == "Global Ops":
            st.session_state.page = "Dashboard"
            st.rerun()
        elif selected_menu == "Precautionary":
            st.session_state.page = "Precautionary"
            st.rerun()
        elif selected_menu == "Emergency Contacts":
            st.session_state.page = "Contacts"
            st.rerun()
        elif selected_menu == "Home":
            st.session_state.page = "Home"
            st.rerun()

    # 4. Language Selector
    with c4:
        lang = st.selectbox("Lang", ["English", "Turkish", "Spanish", "French"], label_visibility="collapsed")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

st.markdown("---")

# ==========================================
# 4. MAIN PAGE LOGIC
# ==========================================

# ----------------- HOME PAGE -----------------
if st.session_state.page == "Home":
    col_img, col_txt = st.columns([1, 1.2])
    
    with col_img:
        # Illustration
        st.image("https://img.freepik.com/free-vector/global-volunteer-solidarity-concept-illustration_114360-17415.jpg", 
                 caption="Connecting Resources to Needs", use_container_width=True)
        
    with col_txt:
        # Right Side Content
        st.markdown(f"<div class='hero-quote'>HUMANITY WITHOUT BORDERS</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='hero-text'>
        A global humanitarian logistics system designed to optimize disaster relief and volunteer deployment 
        across international hubs, including <b>Türkiye</b>.
        </div>
        """, unsafe_allow_html=True)
        
        # ABOUT PROJECT Button (Expander)
        with st.expander("ℹ️ ABOUT PROJECT", expanded=False):
            st.markdown("""
            ### UnityGrid: Global Crisis Response & Resource Optimizer
            **UnityGrid** is an advanced logistical framework designed to bridge the gap between global resource surplus and local disaster needs. By centralizing humanitarian data, UnityGrid ensures that aid reaches the most vulnerable locations—from **Istanbul** to **Tokyo**—without delay.

            #### 🏮 The Vision
            Disasters do not respect borders. **UnityGrid** was built on the principle of "Global Solidarity," providing a standardized platform for tracking life-saving supplies and specialized human capital. This project serves as a prototype for how Management Information Systems (MIS) can be leveraged to minimize human suffering during environmental crises.

            #### 🚀 Impactful Capabilities
            * **Cross-Border Logistics:** Pre-configured with international hubs, including high-priority zones in **Türkiye** (Antakya, Istanbul) and global cities (Tokyo, Beirut).
            * **Specialist Deployment:** A rapid-search algorithm to filter volunteers by mission-critical skills like "Medical" or "Rescue."
            * **Inventory Resilience:** Object-Oriented architecture allows for real-time scaling of aid centers as new crisis zones emerge.

            #### 🛠️ Technical Profile
            * **Architecture:** Object-Oriented Programming (OOP) using Python.
            * **Naming Standards:** Strict adherence to **PascalCase** for classes (`AidCenter`, `UnityGridEngine`) to ensure enterprise-level readability.
            * **Data Logic:** Implements dictionary-based inventory mapping for **O(1)** efficiency in resource updates.
            """)

# ----------------- AWARENESS PAGE -----------------
elif st.session_state.page == "Awareness":
    st.title("📊 Global Awareness Monitor")
    st.markdown("Understanding the frequency and impact of natural disasters is the first step toward effective preparation.")
    
    col_a1, col_a2 = st.columns(2)
    
    with col_a1:
        st.markdown("### Rising Trends in Climate Events")
        # Mock Data for Chart
        years = [2018, 2019, 2020, 2021, 2022, 2023]
        events = [120, 145, 160, 190, 210, 245]
        fig_trend = px.line(x=years, y=events, labels={'x': 'Year', 'y': 'Recorded Disasters'}, markers=True)
        fig_trend.update_traces(line_color='#945031', line_width=4)
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with col_a2:
        st.markdown("### Most Common Threats (2025)")
        data = {'Type': ['Floods', 'Earthquakes', 'Wildfires', 'Storms'], 'Count': [45, 20, 35, 60]}
        fig_pie = px.pie(data_frame=data, names='Type', values='Count', color_discrete_sequence=['#263E3A', '#945031', '#D4AC0D', '#884EA0'])
        st.plotly_chart(fig_pie, use_container_width=True)

    st.info("💡 **Did you know?** Early warning systems can reduce disaster damage by up to 30%.")

# ----------------- GLOBAL OPS (DASHBOARD) -----------------
elif st.session_state.page == "Dashboard":
    st.title("🌍 Global Operations System")
    
    # 1. Live Statistics
    st.markdown("### 📡 Live Situation Report")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Regions", "195", "Global Coverage")
    m2.metric("Disaster Zones", "6", "Critical Alert", delta_color="inverse")
    m3.metric("Relief Teams", "4,210", "+120 Deployed")
    m4.metric("Aid Delivered", "15,000 tons", "+5% vs Last Wk")
    
    st.markdown("---")

    # 2. Map & Inventory
    col_map, col_inv = st.columns([2, 1])
    
    with col_map:
        st.subheader("📍 Live Threat Map")
        zones = st.session_state.engine.get_disaster_zones()
        
        fig = go.Figure(go.Scattergeo(
            lat=[z['lat'] for z in zones], lon=[z['lon'] for z in zones],
            text=[f"{z['type']} ({z['risk']})" for z in zones],
            mode='markers', 
            marker=dict(
                size=[z['radius']*1.2 for z in zones], 
                color=[z['color'] for z in zones], 
                opacity=0.8,
                line=dict(width=1, color='white')
            )
        ))
        fig.update_geos(
            projection_type="natural earth",
            showland=True, landcolor="#1B263B",    
            showocean=True, oceancolor="#0D131E",  
            showcountries=True, countrycolor="#555"
        )
        fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        
    with col_inv:
        st.subheader("📦 Inventory Database")
        c_cont = st.selectbox("Select Continent", list(st.session_state.engine.world_data.keys()))
        c_coun = st.selectbox("Select Country", st.session_state.engine.world_data[c_cont])
        
        inv = st.session_state.engine.get_inventory(c_coun)
        st.success(f"Logistics Hub: **{c_coun}**")
        
        for item, count in inv.items():
            st.progress(min(count/100000, 1.0), text=f"{item}: {count:,}")

# ----------------- PRECAUTIONARY PAGE -----------------
elif st.session_state.page == "Precautionary":
    st.title("🛡️ Precautionary Protocols")
    st.markdown("Standard operating procedures for immediate survival.")
    
    with st.expander("🔴 Earthquake", expanded=True):
        st.markdown("""
        * **DROP:** Drop to your hands and knees.
        * **COVER:** Cover your head and neck with your arms. Crawl under a sturdy table.
        * **HOLD ON:** Hold on to your shelter until shaking stops.
        """)
        
    with st.expander("🌊 Tsunami"):
        st.markdown("""
        * If you feel an earthquake near the coast, move to high ground immediately.
        * Do not wait for an official warning.
        * Stay away from the beach.
        """)
        
    with st.expander("💧 Flood"):
        st.markdown("""
        * **Turn Around, Don't Drown!** Never drive through flooded roads.
        * Move to higher floors.
        * Disconnect electrical appliances if safe to do so.
        """)
        
    with st.expander("🌪️ Tornado"):
        st.markdown("""
        * Go to the lowest level (basement).
        * Stay away from windows.
        * If outside, find a ditch and cover your head.
        """)
        
    with st.expander("❄️ Snow Storm / Blizzard"):
        st.markdown("""
        * Stay indoors.
        * Keep dry and warm.
        * If stranded in a vehicle, run the engine for 10 mins every hour for heat (check exhaust).
        """)
        
    with st.expander("☀️ Heat Wave"):
        st.markdown("""
        * Stay hydrated. Drink water even if not thirsty.
        * Avoid strenuous activity during midday.
        * Check on elderly neighbors.
        """)

# ----------------- EMERGENCY CONTACTS -----------------
elif st.session_state.page == "Contacts":
    st.title("☎️ Emergency Hotlines")
    st.markdown("Direct lines to national emergency services.")
    
    contact_list = []
    for country, numbers in EmergencyRegistry.contacts.items():
        row = {"Country": country}
        row.update(numbers)
        contact_list.append(row)
        
    st.dataframe(pd.DataFrame(contact_list).set_index("Country"), use_container_width=True)

# ----------------- VOLUNTEER (TAKE ACTION) -----------------
elif st.session_state.page == "Volunteer":
    st.title("🤝 Take Action: Join the Grid")
    st.markdown("Your skills can save lives. Register for the global deployment roster.")
    
    with st.form("volunteer_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            age = st.number_input("Age", min_value=18, max_value=80)
        with c2:
            skill = st.selectbox("Primary Skill", ["Medical (Doctor/Nurse)", "Search & Rescue", "Logistics/Driver", "Translation", "Engineering"])
            region = st.selectbox("Preferred Region", ["Asia", "Europe", "Americas", "Africa", "Global (Any)"])
            
        submitted = st.form_submit_button("Submit Application")
        
        if submitted:
            if name and email:
                st.balloons()
                st.success(f"Thank you, {name}. You have been added to the {skill} roster for {region}.")
            else:
                st.error("Please fill in all required fields.")
