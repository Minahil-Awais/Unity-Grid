import streamlit as st
import plotly.graph_objects as go
from models import UnityGridEngine, EmergencyRegistry

# 1. PAGE SETUP
st.set_page_config(page_title="Unity Grid Global", page_icon="🌿", layout="wide")

# 2. STATE MANAGEMENT
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'lang' not in st.session_state:
    st.session_state.lang = "English"

# 3. TRANSLATION DICTIONARY
translations = {
    "English": {"home": "Awareness", "act": "Take Action", "dash": "Global Ops", "quote": "HUMANITY WITHOUT BORDERS", "sub": ""},
    "Turkish": {"home": "Farkındalık", "act": "Harekete Geç", "dash": "Küresel Operasyonlar", "quote": "SINIRSIZ İNSANLIK", "sub": ""},
    "Spanish": {"home": "Conciencia", "act": "Tomar Acción", "dash": "Ops Globales", "quote": "HUMANIDAD SIN FRONTERAS", "sub": ""},
    "French": {"home": "Sensibilisation", "act": "Agir", "dash": "Ops Mondiales", "quote": "L'HUMANITÉ SANS FRONTIÈRES", "sub": ""},
    "Russian": {"home": "Осведомленность", "act": "Действовать", "dash": "Глобальные операции", "quote": "ЧЕЛОВЕЧЕСТВО БЕЗ ГРАНИЦ", "sub": ""},
    "Arabic": {"home": "وعي", "act": "اتخاذ إجراء", "dash": "العمليات العالمية", "quote": "إنسانية بلا حدود", "sub": ""},
    "Chinese": {"home": "意识", "act": "采取行动", "dash": "全球行动", "quote": "无国界的人性", "sub": ""},
    "Hindi": {"home": "जागरूकता", "act": "कार्रवाई करें", "dash": "वैश्विक अभियान", "quote": "सीमाओं के बिना मानवता", "sub": ""}
}
t = translations.get(st.session_state.lang, translations["English"])

# 4. AESTHETIC CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');
    
    :root {
        --primary: #263E3A;  /* Deep Green */
        --accent: #945031;   /* Terracotta Brown */
        --bg: #F9F9F9;
    }

    .stApp { background-color: var(--bg); font-family: 'Montserrat', sans-serif; }
    .block-container { padding-top: 1rem !important; margin-top: 0px !important; }
    [data-testid="stHeader"] { display: none; }
    
    .nav-box { display: flex; justify-content: space-between; align-items: center; padding: 15px 0px; margin-bottom: 20px; border-bottom: 2px solid #e0e0e0; }
    .logo-text { font-size: 32px; font-weight: 800; color: var(--primary); letter-spacing: -1px; }
    .logo-grid { color: var(--accent); }
    
    .stButton button { background-color: var(--accent) !important; color: white !important; border-radius: 5px; border: none; padding: 8px 25px; font-weight: 600; transition: 0.3s; }
    .stButton button:hover { opacity: 0.8; transform: translateY(-2px); }
    
    .hero-quote { font-size: 52px; font-weight: 800; color: var(--primary); line-height: 1.1; margin-bottom: 15px; }
    .hero-sub { color: #555; font-size: 16px; max-width: 600px; line-height: 1.6; text-align: justify; }
    
    div[data-testid="stMetricValue"] { color: var(--primary); }
    </style>
""", unsafe_allow_html=True)

# 5. HEADER & NAVIGATION
col_logo, col_nav = st.columns([1, 1.5])

with col_logo:
    st.markdown(f"""
        <div class='nav-box' style='border:none;'>
            <div class='logo-container' style='display:flex; align-items:center; gap:10px;'>
                <svg width="40" height="40" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" stroke="#263E3A" stroke-width="8" fill="none" />
                    <path d="M50 5 L50 95 M5 50 L95 50" stroke="#945031" stroke-width="8" />
                    <circle cx="50" cy="50" r="15" fill="#263E3A" />
                </svg>
                <div class='logo-text'>Unity <span class='logo-grid'>Grid</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_nav:
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])
    if c1.button(t['home']): st.session_state.page = "Home"
    if c2.button(t['act']): st.session_state.page = "Take Action"
    with c3:
        menu_choice = st.selectbox("Menu ☰", ["Global Ops", "Precautionary", "Emergency Contacts", "Volunteering"], label_visibility="collapsed")
        if menu_choice == "Global Ops": st.session_state.page = "Dashboard"
        elif menu_choice == "Precautionary": st.session_state.page = "Precautionary"
        elif menu_choice == "Emergency Contacts": st.session_state.page = "Contacts"
        elif menu_choice == "Volunteering": st.session_state.page = "Volunteer"
    with c4:
        flags = {"English": "🇬🇧", "Turkish": "🇹🇷", "Spanish": "🇪🇸", "French": "🇫🇷", "Russian": "🇷🇺", "Arabic": "🇸🇦", "Chinese": "🇨🇳", "Hindi": "🇮🇳"}
        lang = st.selectbox("", list(translations.keys()), format_func=lambda x: f"{flags[x]} {x}", label_visibility="collapsed")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

st.markdown("---")

# 6. PAGE CONTENT

if st.session_state.page == "Home":
    # ---------------- HOME PAGE ----------------
    col_text, col_img = st.columns([1, 1])
    
    with col_text:
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-quote'>{t['quote']}</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='hero-sub'>
            <b>UnityGrid</b> is an advanced logistical framework designed to bridge the gap between global resource surplus and local disaster needs. 
            By centralizing humanitarian data, UnityGrid ensures that aid reaches the most vulnerable locations—from <b>Istanbul</b> to <b>Tokyo</b>—without delay.
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("ℹ️ ABOUT PROJECT"):
            with st.expander("Project Overview & Technical Profile", expanded=True):
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

    with col_img:
        # Illustration of humanity/unity on the RIGHT side
        
        st.image("https://cdn-icons-png.flaticon.com/512/3209/3209955.png", width=450)

elif st.session_state.page == "Dashboard":
    # ---------------- GLOBAL OPS ----------------
    st.markdown(f"## 🌍 {t['dash']} Center")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Regions", "195", "Global Coverage")
    m2.metric("Disaster Zones", "11", "High Alert", delta_color="inverse")
    m3.metric("Relief Teams", "4,210", "+120 Today")
    m4.metric("Donations", "$1.2M", "+5%")

    st.markdown("### 📡 Live Disaster Threat Map")
    zones = st.session_state.engine.get_disaster_zones()
    
    lat = [z['lat'] for z in zones]
    lon = [z['lon'] for z in zones]
    colors = [z['color'] for z in zones]
    sizes = [z['radius'] * 1.5 for z in zones]

    fig = go.Figure()
    
    # 1. Base Map (Navy/Functional Look)
    fig.add_trace(go.Scattergeo(
        locationmode='country names',
        marker=dict(size=2, color='#888'), 
    ))
    
    # 2. Disaster Zones Overlay
    fig.add_trace(go.Scattergeo(
        lat=lat, lon=lon,
        mode='markers',
        marker=dict(size=sizes, color=colors, opacity=0.8, line=dict(width=1, color='white')),
        name='Alert Zones'
    ))
    
    # 3. Functional Navy-Blue Styling
    fig.update_geos(
        projection_type="natural earth",
        showland=True, landcolor="#1B263B",    # Navy-Blue Land
        showocean=True, oceancolor="#0D131E",  # Dark Ocean
        showcountries=True, countrycolor="#555",
        showlakes=True, lakecolor="#0D131E"
    )
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📦 Global Inventory Database")
    c_cont, c_coun = st.columns(2)
    selected_continent = c_cont.selectbox("Select Continent", list(st.session_state.engine.world_data.keys()))
    selected_country = c_coun.selectbox("Select Country", st.session_state.engine.world_data[selected_continent])
    inv = st.session_state.engine.get_inventory(selected_country)
    
    st.info(f"Logistics Status: **{selected_country}**")
    cols = st.columns(5)
    for i, (k, v) in enumerate(inv.items()):
        cols[i].metric(k, f"{v:,}")

elif st.session_state.page == "Precautionary":
    # ---------------- PRECAUTIONARY ----------------
    st.title("🛡️ Frontline Safety Protocols")
    
    with st.expander("🔴 Earthquake (Immediate Action)", expanded=True):
        st.markdown("**DROP, COVER, HOLD ON:** Indoors? Stay under a desk. Outdoors? Move to open areas.")
    with st.expander("🌊 Tsunami (Coastal Warning)"):
        st.markdown("**HIGHER GROUND:** If shaking lasts >20s, move inland/uphill immediately.")
    with st.expander("💧 Flood (Flash Warnings)"):
        st.markdown("**TURN AROUND, DON'T DROWN:** Do not drive through flooded roads. 6 inches of water can stall a car.")
    with st.expander("🌪️ Cyclone / Hurricane"):
        st.markdown("**FORTIFY:** Board up windows. Stock 3 days of water. Stay indoors away from glass.")
    with st.expander("🌪️ Tornado"):
        st.markdown("**LOWEST LEVEL:** Go to a basement or interior room without windows. Cover your head.")

elif st.session_state.page == "Contacts":
    # ---------------- CONTACTS ----------------
    st.title("☎️ Global Emergency Hotlines")
    st.markdown("Rapid access to emergency services by country.")
    
    # Use the Registry Class for Data
    contact_list = []
    for country, numbers in EmergencyRegistry.contacts.items():
        contact_list.append({"Country": country, **numbers})
    
    st.dataframe(contact_list, use_container_width=True)

elif st.session_state.page == "Volunteer":
    # ---------------- VOLUNTEER ----------------
    st.title("🤝 Join the Global Grid")
    v1, v2 = st.columns(2)
    with v1:
        st.text_input("Full Name")
        st.text_input("Email")
        st.selectbox("Expertise", ["Medical", "Rescue", "Logistics"])
    with v2:
        st.selectbox("Preferred Deployment", list(st.session_state.engine.world_data.keys()))
        if st.button("Submit Application"):
            st.success("Application received.")

elif st.session_state.page == "Take Action":
    # ---------------- TAKE ACTION ----------------
    st.title("🚀 Power the Mission")
    
    col_donate, col_items = st.columns(2)
    
    with col_donate:
        st.markdown("### 💳 Financial Contribution")
        st.markdown("Funds are allocated strictly to transport logistics and medical procurement.")
        amt = st.select_slider("Select Amount ($)", [10, 50, 100, 500, 1000])
        if st.button(f"Donate ${amt}"):
            st.balloons()
            st.success(f"Transaction of ${amt} Processed via Stripe Secure Gateway.")
            
    with col_items:
        st.markdown("### 📦 Material Aid")
        st.markdown("We accept shipments of the following certified items:")
        st.markdown("""
        * ✅ Sealed Medical Kits (ISO Certified)
        * ✅ Water Purification Tablets
        * ✅ Thermal Blankets
        * ✅ Solar Power Banks
        """)
        if st.button("Schedule Pickup"):
            st.info("Logistics partner DHL will contact you for pickup details.")
