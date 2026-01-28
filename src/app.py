import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random

# ==========================================
# 0. MOCK DATA CLASSES
# ==========================================
class UnityGridEngine:
    def __init__(self):
        self.world_data = {
            "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo (Brazzaville)", "DR Congo", "Côte d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
            "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
            "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"],
            "North America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"],
            "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
            "Oceania": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
        }
        self.inventory_db = {
            "Japan": {"Medical Kits": 1200, "Blankets": 5000, "Water (L)": 15000, "Generators": 80},
            "Türkiye": {"Medical Kits": 3500, "Blankets": 12000, "Water (L)": 45000, "Generators": 150},
            "USA": {"Medical Kits": 8000, "Blankets": 25000, "Water (L)": 100000, "Generators": 500},
        }

    def get_disaster_zones(self):
        return [
            {"lat": 36.20, "lon": 36.16, "risk": "High", "type": "Earthquake", "radius": 15, "color": "#FF4B4B"}, # Antakya
            {"lat": 35.67, "lon": 139.65, "risk": "Moderate", "type": "Tsunami Warning", "radius": 10, "color": "#FFA500"}, # Tokyo
            {"lat": 33.89, "lon": 35.50, "risk": "Critical", "type": "Supply Shortage", "radius": 8, "color": "#FF4B4B"}, # Beirut
            {"lat": 28.61, "lon": 77.20, "risk": "High", "type": "Heat Wave", "radius": 12, "color": "#FFA500"}, # Delhi
            {"lat": 19.43, "lon": -99.13, "risk": "Moderate", "type": "Seismic", "radius": 10, "color": "#FFFF00"}, # Mexico City
            {"lat": -6.20, "lon": 106.84, "risk": "High", "type": "Flood", "radius": 14, "color": "#FF4B4B"}, # Jakarta
        ]

    def get_inventory(self, country):
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

# Translation Logic
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
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    :root { --primary: #263E3A; --accent: #F5F5F0; }

    /* Main App Contrast */
    .stApp { background-color: white; }
    
    /* Standard Text - Only target body text, not buttons */
    p, span, label, .stMetric div { color: #263E3A !important; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { color: #263E3A !important; font-family: 'Montserrat', sans-serif; font-weight: 800; }

    /* NAVIGATION BUTTONS - Force White Text on Primary Background */
    div.stButton > button:first-child {
        background-color: var(--primary) !important;
        color: #945031 !important;
        border: none !important;
        font-weight: 700 !important;
        width: 100%;
    }
    
    /* Logo Styling */
    .logo-title { font-size: 32px; font-weight: 800; color: var(--primary); }
    .logo-sub { color: var(--accent); }

    /* Responsive Columns */
    [data-testid="column"] { width: 100% !important; flex: 1 1 100% !important; min-width: 100% !important; }
    @media (min-width: 768px) {
        [data-testid="column"] { min-width: 0 !important; flex: 1 !important; width: auto !important; }
    }

    /* Hero Styling */
    .hero-quote { font-size: calc(24px + 1.5vw); font-weight: 800; color: var(--primary); line-height: 1.1; }
    </style>
""", unsafe_allow_html=True)
# ==========================================
# 3. HEADER & NAVIGATION LOGIC
# ==========================================
col_logo, col_nav = st.columns([1, 2])

with col_logo:
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
    c1, c2, c3, c4 = st.columns([1, 1, 1.5, 1])
    
    # 1. Awareness Button
    if c1.button(t['aware'], use_container_width=True):
        st.session_state.page = "Awareness"
        st.rerun()
        
    # 2. Take Action Button
    if c2.button(t['act'], use_container_width=True):
        st.session_state.page = "Volunteer"
        st.rerun()

    # 3. Menu Dropdown (Persistent Callback)
    with c3:
        def menu_callback():
            selection = st.session_state.menu_selection
            if selection == "Global Ops": st.session_state.page = "Dashboard"
            elif selection == "Precautionary": st.session_state.page = "Precautionary"
            elif selection == "Emergency Contacts": st.session_state.page = "Contacts"
            elif selection == "Home": st.session_state.page = "Home"

        menu_options = ["Menu", "Home", "Global Ops", "Precautionary", "Emergency Contacts"]
        st.selectbox("Navigation", menu_options, key="menu_selection", on_change=menu_callback, label_visibility="collapsed")

    # 4. Language Selector
    with c4:
        lang = st.selectbox("Lang", ["English", "Turkish", "Spanish", "French"], label_visibility="collapsed")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

st.markdown("---")

# ==========================================
# 4. PAGE CONTENT
# ==========================================

if st.session_state.page == "Home":
    # ----------------- HOME PAGE -----------------
    col_img, col_txt = st.columns([1, 1.2])
    
    with col_img:
        st.image("https://images.unsplash.com/photo-1593113598332-cd288d649433?ixlib=rb-4.0.3&auto=format&fit=crop&w=1170&q=80", 
                 caption="UnityGrid: Connecting Resources to Needs", use_container_width=True)
        
    with col_txt:
        st.markdown(f"<div class='hero-quote'>HUMANITY WITHOUT BORDERS</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='hero-text'>
        A global humanitarian logistics system designed to optimize disaster relief and volunteer deployment 
        across international hubs, including <b>Türkiye</b>.
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(" ABOUT PROJECT"):
             with st.expander("UnityGrid: Global Crisis Response & Resource Optimizer", expanded=True):
                st.markdown("""
                ### 🏮 The Vision
                Disasters do not respect borders. **UnityGrid** was built on the principle of "Global Solidarity," providing a standardized platform for tracking life-saving supplies and specialized human capital. This project serves as a prototype for how Management Information Systems (MIS) can be leveraged to minimize human suffering during environmental crises.

                ### 🚀 Impactful Capabilities
                * **Cross-Border Logistics:** Pre-configured with international hubs, including high-priority zones in **Türkiye** (Antakya, Istanbul) and global cities (Tokyo, Beirut).
                * **Specialist Deployment:** A rapid-search algorithm to filter volunteers by mission-critical skills like "Medical" or "Rescue."
                * **Inventory Resilience:** Object-Oriented architecture allows for real-time scaling of aid centers as new crisis zones emerge.

                ### 🛠️ Technical Profile
                * **Architecture:** Object-Oriented Programming (OOP) using Python.
                * **Naming Standards:** Strict adherence to **PascalCase** for classes (`AidCenter`, `UnityGridEngine`) to ensure enterprise-level readability.
                * **Data Logic:** Implements dictionary-based inventory mapping for **O(1)** efficiency in resource updates.
                """)

elif st.session_state.page == "Awareness":
    # ----------------- AWARENESS PAGE (UPDATED) -----------------
    st.title("📊 Global Awareness Monitor")
    st.markdown("Data-driven insights into the frequency, cost, and human impact of natural disasters (2020-2025).")
    
    # TOP KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Global Events (2024)", "421", "+12% YoY", help="Recorded natural disasters causing >$1M damage")
    k2.metric("Economic Cost", "$310B", "Critical", delta_color="inverse", help="Total adjusted economic loss")
    k3.metric("Displaced Persons", "8.4M", "High", delta_color="inverse")
    k4.metric("Climate Anomalies", "19", "Record High")
    
    st.markdown("---")

    col_a1, col_a2 = st.columns([1.5, 1])
    
    with col_a1:
        st.subheader("📈 Rising Frequency by Disaster Type")
        # Advanced Mock Data Generation
        years = [2020, 2021, 2022, 2023, 2024, 2025]
        df_trends = pd.DataFrame({
            "Year": years * 3,
            "Count": [
                45, 48, 52, 60, 75, 82,   # Floods
                30, 35, 33, 40, 55, 65,   # Storms
                12, 10, 15, 14, 22, 18    # Wildfires
            ],
            "Type": ["Floods"]*6 + ["Storms"]*6 + ["Wildfires"]*6
        })
        
        fig_area = px.area(df_trends, x="Year", y="Count", color="Type", 
                          color_discrete_sequence=['#263E3A', '#945031', '#D4AC0D'],
                          labels={"Count": "Recorded Events"},
                          title="Global Disaster Frequency Trend")
        fig_area.update_layout(hovermode="x unified", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_area, use_container_width=True)
        
    with col_a2:
        st.subheader("🌍 Impact by Region")
        # Donut Chart for Impact
        df_pie = pd.DataFrame({
            "Region": ["Asia Pacific", "Africa", "Americas", "Europe", "Middle East"],
            "Affected (M)": [45, 25, 15, 5, 10]
        })
        fig_donut = px.pie(df_pie, values="Affected (M)", names="Region", hole=0.5,
                           color_discrete_sequence=px.colors.sequential.RdBu,
                           title="Human Impact Distribution (%)")
        fig_donut.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_donut, use_container_width=True)

    st.info("💡 **Insight:** While frequency is rising globally, effective Early Warning Systems (EWS) in Asia have reduced mortality rates by 40% despite higher event counts.")

elif st.session_state.page == "Dashboard":
    # ----------------- DASHBOARD (Global Ops) -----------------
    st.title("🌍 Global Operations System")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Regions", "195", "Global Coverage")
    m2.metric("Disaster Zones", "6", "Critical Alert", delta_color="inverse")
    m3.metric("Relief Teams", "4,210", "+120 Deployed")
    m4.metric("Aid Delivered", "15,000 tons", "+5% vs Last Wk")
    
    st.markdown("---")

    col_map, col_inv = st.columns([2, 1])
    
    with col_map:
        st.subheader("📍 Live Threat Map")
        zones = st.session_state.engine.get_disaster_zones()
        fig = go.Figure(go.Scattergeo(
            lat=[z['lat'] for z in zones], lon=[z['lon'] for z in zones],
            text=[f"{z['type']} ({z['risk']})" for z in zones],
            mode='markers', 
            marker=dict(size=[z['radius']*1.5 for z in zones], color=[z['color'] for z in zones], opacity=0.8)
        ))
        fig.update_geos(projection_type="natural earth", showland=True, landcolor="#1B263B", showocean=True, oceancolor="#0D131E", showcountries=True, countrycolor="#555")
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

elif st.session_state.page == "Precautionary":
    # ----------------- PRECAUTIONARY (UPDATED) -----------------
    st.title("🛡️ Frontline Safety Protocols")
    st.markdown("Comprehensive survival guides structured by event phase: **Prepare, Survive, Recover**.")
    
    # 1. EARTHQUAKE
    with st.expander("🔴 Earthquake (Seismic Activity)", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### 1. Prepare")
            st.markdown("""
            * **Secure Heavy Items:** Anchor bookshelves and TVs to walls.
            * **Go-Bag:** Pack water, flashlight, and first aid.
            * **Identify Safe Spots:** Under sturdy tables or interior walls.
            """)
        with c2:
            st.markdown("#### 2. Survive (During)")
            st.markdown("""
            * **DROP** to your hands and knees.
            * **COVER** your head and neck. Crawl under shelter.
            * **HOLD ON** until the shaking stops completely.
            * **DO NOT** run outside during shaking.
            """)
        with c3:
            st.markdown("#### 3. Recover (After)")
            st.markdown("""
            * **Check for Gas Leaks:** Smell gas? Leave immediately.
            * **Aftershocks:** Expect smaller tremors.
            * **Tsunami Risk:** If near coast, move to high ground.
            """)

    # 2. FLOOD
    with st.expander("🌊 Flash Floods & Storm Surge"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### 1. Prepare")
            st.markdown("""
            * **Know Your Zone:** Are you in a low-lying area?
            * **Elevate Utilities:** Move critical electronics to higher floors.
            * **Waterproof Documents:** Seal ID and insurance papers.
            """)
        with c2:
            st.markdown("#### 2. Survive (During)")
            st.markdown("""
            * **Turn Around, Don't Drown:** 6 inches of water can stall a car.
            * **Evacuate:** Follow official orders immediately.
            * **High Ground:** Move to the roof only if trapped (signal for help).
            """)
        with c3:
            st.markdown("#### 3. Recover (After)")
            st.markdown("""
            * **Avoid Floodwater:** It may contain sewage or live wires.
            * **Dry Out:** Mold grows within 24-48 hours.
            * **Disinfect:** Clean everything touched by floodwater.
            """)

    # 3. WILDFIRE
    with st.expander("🔥 Wildfires"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### 1. Prepare")
            st.markdown("""
            * **Defensible Space:** Clear 30ft of brush around home.
            * **N95 Masks:** Stock up for smoke protection.
            * **Evacuation Route:** Plan 2 ways out of your neighborhood.
            """)
        with c2:
            st.markdown("#### 2. Survive (During)")
            st.markdown("""
            * **Leave Early:** Don't wait for flames to be visible.
            * **Close Windows:** Shut vents to keep sparks out.
            * **Low Visibility:** Drive slowly with headlights on.
            """)
        with c3:
            st.markdown("#### 3. Recover (After)")
            st.markdown("""
            * **Hot Spots:** Watch for ground that is still smoking.
            * **Check Air Quality:** Wait for official 'Safe' levels before returning.
            * **Ash Safety:** Wear gloves/masks when cleaning.
            """)
    
    # 4. EXTREME HEAT
    with st.expander("☀️ Extreme Heat Wave"):
        st.markdown("**Core Rule:** Hydrate before you feel thirsty. Check on elderly neighbors/relatives. Keep blinds closed during the day.")

elif st.session_state.page == "Contacts":
    # ----------------- CONTACTS -----------------
    st.title("☎️ Emergency Hotlines")
    
    contact_list = []
    for country, numbers in EmergencyRegistry.contacts.items():
        row = {"Country": country}
        row.update(numbers)
        contact_list.append(row)
        
    st.dataframe(pd.DataFrame(contact_list).set_index("Country"), use_container_width=True)

elif st.session_state.page == "Volunteer":
    # ----------------- VOLUNTEER -----------------
    st.title("🤝 Join the Grid")
    
    with st.form("volunteer_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
        with c2:
            skill = st.selectbox("Primary Skill", ["Medical", "Search & Rescue", "Logistics", "IT Support"])
            
        submitted = st.form_submit_button("Submit Application")
        if submitted:
            st.balloons()
            st.success(f"Thank you, {name}. You have been added to the {skill} roster.")
