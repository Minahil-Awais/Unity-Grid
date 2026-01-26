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
    "English": {"home": "Awareness", "act": "Take Action", "dash": "Global Ops", "quote": "HUMANITY WITHOUT BORDERS"},
    "Turkish": {"home": "Farkındalık", "act": "Harekete Geç", "dash": "Küresel Operasyonlar", "quote": "SINIRSIZ İNSANLIK"},
    "Spanish": {"home": "Conciencia", "act": "Tomar Acción", "dash": "Ops Globales", "quote": "HUMANIDAD SIN FRONTERAS"},
    "French": {"home": "Sensibilisation", "act": "Agir", "dash": "Ops Mondiales", "quote": "L'HUMANITÉ SANS FRONTIÈRES"},
    "Russian": {"home": "Осведомленность", "act": "Действовать", "dash": "Глобальные операции", "quote": "ЧЕЛОВЕЧЕСТВО БЕЗ ГРАНИЦ"},
    "Arabic": {"home": "وعي", "act": "اتخاذ إجراء", "dash": "العمليات العالمية", "quote": "إنسانية بلا حدود"},
    "Chinese": {"home": "意识", "act": "采取行动", "dash": "全球行动", "quote": "无国界的人性"},
    "Hindi": {"home": "जागरूकता", "act": "कार्रवाई करें", "dash": "वैश्विक अभियान", "quote": "सीमाओं के बिना मानवता"}
}
t = translations.get(st.session_state.lang, translations["English"])

# 4. AESTHETIC CSS (Fixed Syntax for CSS Properties)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');
    
    :root {
        --primary: #263E3A; 
        --accent: #945031;
        --bg: #F9F9F9;
    }

    .stApp { background-color: var(--bg); font-family: 'Montserrat', sans-serif; }
    .block-container { padding-top: 1rem !important; }
    [data-testid="stHeader"] { display: none; }
    
    .logo-text { font-size: 32px; font-weight: 800; color: var(--primary); letter-spacing: -1px; }
    .logo-grid { color: var(--accent); }
    
    .stButton button { 
        background-color: var(--accent) !important; 
        color: white !important; 
        border-radius: 5px; 
        border: none; 
        padding: 8px 25px; 
        font-weight: 600; 
    }
    
    .hero-quote { font-size: 52px; font-weight: 800; color: var(--primary); line-height: 1.1; margin-bottom: 15px; }
    .hero-sub { color: #555; font-size: 18px; max-width: 800px; line-height: 1.6; text-align: justify; }
    </style>
""", unsafe_allow_html=True)

# 5. HEADER & NAVIGATION
col_logo, col_nav = st.columns([1, 1.5])

with col_logo:
    st.markdown(f"""
        <div style='display:flex; align-items:center; gap:10px;'>
            <svg width="40" height="40" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" stroke="#263E3A" stroke-width="8" fill="none" />
                <path d="M50 5 L50 95 M5 50 L95 50" stroke="#945031" stroke-width="8" />
                <circle cx="50" cy="50" r="15" fill="#263E3A" />
            </svg>
            <div class='logo-text'>Unity <span class='logo-grid'>Grid</span></div>
        </div>
    """, unsafe_allow_html=True)

with col_nav:
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])
    # Functional Navigation Buttons
    if c1.button(t['home'], key="nav_awareness"): 
        st.session_state.page = "Home"
    if c2.button(t['act'], key="nav_take_action"): 
        st.session_state.page = "Take Action"
    
    with c3:
        menu_choice = st.selectbox("Menu ☰", ["Global Ops", "Precautionary", "Emergency Contacts", "Volunteering"], label_visibility="collapsed")
        if menu_choice == "Global Ops": st.session_state.page = "Dashboard"
        elif menu_choice == "Precautionary": st.session_state.page = "Precautionary"
        elif menu_choice == "Emergency Contacts": st.session_state.page = "Contacts"
        elif menu_choice == "Volunteering": st.session_state.page = "Volunteer"
    
    with c4:
        flags = {"English": "🇬🇧", "Turkish": "🇹🇷", "Spanish": "🇪🇸", "French": "🇫🇷", "Russian": "🇷🇺", "Arabic": "🇸🇦", "Chinese": "🇨🇳", "Hindi": "🇮🇳"}
        lang_sel = st.selectbox("", list(translations.keys()), format_func=lambda x: f"{flags[x]} {x}", label_visibility="collapsed")
        if lang_sel != st.session_state.lang:
            st.session_state.lang = lang_sel
            st.rerun()

st.markdown("---")

# 6. PAGE CONTENT

if st.session_state.page == "Home":
    # ---------------- HOME PAGE ----------------
    col_text, col_img = st.columns([1.2, 1])
    
    with col_text:
        st.markdown(f"<div class='hero-quote'>{t['quote']}</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='hero-sub'>
            A global humanitarian logistics system designed to optimize disaster relief and volunteer deployment 
            across international hubs, including <b>Türkiye</b>.
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- THE ABOUT PROJECT BUTTON ---
        if st.button("ℹ️ ABOUT PROJECT", key="about_btn"):
            st.markdown("---")
            st.markdown("""
            ### UnityGrid: Global Crisis Response & Resource Optimizer
            **UnityGrid** is an advanced logistical framework designed to bridge the gap between global resource surplus and local disaster needs. By centralizing humanitarian data, UnityGrid ensures that aid reaches the most vulnerable locations—from **Istanbul** to **Tokyo**—without delay.

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
            st.markdown("---")

    with col_img:
        # Illustration on the RIGHT side
        st.image("https://cdn-icons-png.flaticon.com/512/3209/3209955.png", width=450)

elif st.session_state.page == "Dashboard":
    # ---------------- DASHBOARD (GLOBAL OPS) ----------------
    st.markdown(f"## 🌍 {t['dash']} Center")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Regions", "195", "Global")
    m2.metric("Disaster Zones", "11", "Alert", delta_color="inverse")
    m3.metric("Relief Teams", "4,210", "+120")
    m4.metric("Donations", "$1.2M", "+5%")

    # NAVY BLUE MAP
    zones = st.session_state.engine.get_disaster_zones()
    fig = go.Figure(go.Scattergeo(
        lat=[z['lat'] for z in zones], lon=[z['lon'] for z in zones],
        mode='markers', marker=dict(size=12, color=[z['color'] for z in zones], opacity=0.8)
    ))
    fig.update_geos(
        projection_type="natural earth", showland=True, landcolor="#1B263B",
        showocean=True, oceancolor="#0D131E", showcountries=True, countrycolor="#555"
    )
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    # Inventory Lookup
    c_cont, c_coun = st.columns(2)
    sel_continent = c_cont.selectbox("Select Continent", list(st.session_state.engine.world_data.keys()))
    sel_country = c_coun.selectbox("Select Country", st.session_state.engine.world_data[sel_continent])
    inv = st.session_state.engine.get_inventory(sel_country)
    st.info(f"Logistics Status: {sel_country}")
    cols = st.columns(5)
    for i, (k, v) in enumerate(inv.items()):
        cols[i].metric(k, f"{v:,}")

elif st.session_state.page == "Precautionary":
    st.title("🛡️ Frontline Safety Protocols")
    with st.expander("🔴 Earthquake (Immediate Action)", expanded=True):
        st.markdown("**DROP, COVER, HOLD ON.** Move to open areas if outdoors.")
    with st.expander("🌊 Tsunami (Coastal Warning)"):
        st.markdown("**HIGHER GROUND.** Move inland/uphill immediately.")

elif st.session_state.page == "Contacts":
    st.title("☎️ Global Emergency Hotlines")
    contact_list = [{"Country": c, **n} for c, n in EmergencyRegistry.contacts.items()]
    st.dataframe(contact_list, use_container_width=True)

elif st.session_state.page == "Volunteer":
    st.title("🤝 Join the Global Grid")
    v1, v2 = st.columns(2)
    with v1:
        st.text_input("Full Name")
        st.selectbox("Expertise", ["Medical", "Rescue", "Logistics"])
    with v2:
        st.text_input("Email")
        if st.button("Submit Application"):
            st.success("Application received.")

elif st.session_state.page == "Take Action":
    st.title("🚀 Power the Mission")
    col_donate, col_items = st.columns(2)
    with col_donate:
        st.markdown("### 💳 Financial Contribution")
        amt = st.select_slider("Select Amount ($)", [10, 50, 100, 500, 1000])
        if st.button(f"Donate ${amt}"):
            st.balloons()
            st.success(f"Transaction of ${amt} Processed.")
    with col_items:
        st.markdown("### 📦 Material Aid")
        st.markdown("* ✅ Sealed Medical Kits\n* ✅ Water Tablets\n* ✅ Blankets")
        if st.button("Schedule Pickup"):
            st.info("Logistics partner will contact you.")
