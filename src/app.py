import streamlit as st
import plotly.graph_objects as go
from models import UnityGridEngine

# 1. PAGE SETUP
st.set_page_config(page_title="Unity Grid Global", page_icon="🌍", layout="wide")

# 2. STATE MANAGEMENT (Language & Navigation)
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'lang' not in st.session_state:
    st.session_state.lang = "English"

# 3. TRANSLATION DICTIONARY
translations = {
    "English": {"home": "Awareness", "act": "Take Action", "dash": "Global Ops", "quote": "HUMANITY WITHOUT BORDERS", "sub": "Global humanitarian logistics optimized for disaster relief."},
    "Turkish": {"home": "Farkındalık", "act": "Harekete Geç", "dash": "Küresel Operasyonlar", "quote": "SINIRSIZ İNSANLIK", "sub": "Afet yardımı için optimize edilmiş küresel insani lojistik."},
    "Spanish": {"home": "Conciencia", "act": "Tomar Acción", "dash": "Ops Globales", "quote": "HUMANIDAD SIN FRONTERAS", "sub": "Logística humanitaria global optimizada para el socorro en desastres."},
    "French": {"home": "Sensibilisation", "act": "Agir", "dash": "Ops Mondiales", "quote": "L'HUMANITÉ SANS FRONTIÈRES", "sub": "Logistique humanitaire mondiale optimisée pour les secours en cas de catastrophe."},
    "Russian": {"home": "Осведомленность", "act": "Действовать", "dash": "Глобальные операции", "quote": "ЧЕЛОВЕЧЕСТВО БЕЗ ГРАНИЦ", "sub": "Глобальная гуманитарная логистика, оптимизированная для оказания помощи при стихийных бедствиях."},
    "Arabic": {"home": "وعي", "act": "اتخاذ إجراء", "dash": "العمليات العالمية", "quote": "إنسانية بلا حدود", "sub": "لوجستيات إنسانية عالمية محسنة للإغاثة في حالات الكوارث."},
    "Chinese": {"home": "意识", "act": "采取行动", "dash": "全球行动", "quote": "无国界的人性", "sub": "为救灾优化的全球人道主义物流。"},
    "Hindi": {"home": "जागरूकता", "act": "कार्रवाई करें", "dash": "वैश्विक अभियान", "quote": "सीमाओं के बिना मानवता", "sub": "आपदा राहत के लिए अनुकूलित वैश्विक मानवीय रसद।"}
}
t = translations.get(st.session_state.lang, translations["English"])

# 4. AESTHETIC CSS (Professional & Custom Colors)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');
    
    :root {
        --primary: #263E3A;  /* Deep Green */
        --accent: #945031;   /* Terracotta Brown */
        --bg: #F9F9F9;
    }

    /* GENERAL RESET */
    .stApp { background-color: var(--bg); font-family: 'Montserrat', sans-serif; }
    
    /* REMOVE TOP MARGIN */
    .block-container { padding-top: 1rem !important; margin-top: 0px !important; }
    [data-testid="stHeader"] { display: none; }
    
    /* CUSTOM NAVIGATION BAR */
    .nav-box {
        display: flex; justify-content: space-between; align-items: center;
        padding: 15px 0px; margin-bottom: 20px; border-bottom: 2px solid #e0e0e0;
    }
    
    /* LOGO STYLING */
    .logo-container { display: flex; align-items: center; gap: 10px; }
    .logo-text { font-size: 32px; font-weight: 800; color: var(--primary); letter-spacing: -1px; }
    .logo-grid { color: var(--accent); }
    
    /* BUTTON STYLING (#945031) */
    .stButton button {
        background-color: var(--accent) !important;
        color: white !important;
        border-radius: 5px;
        border: none;
        padding: 8px 25px;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton button:hover { opacity: 0.8; transform: translateY(-2px); }
    
    /* HERO TYPOGRAPHY */
    .hero-quote { font-size: 60px; font-weight: 800; color: var(--primary); line-height: 1; margin-bottom: 15px; }
    .hero-sub { color: #555; font-size: 18px; max-width: 500px; line-height: 1.5; }
    
    /* MAP & METRICS */
    div[data-testid="stMetricValue"] { color: var(--primary); }
    </style>
""", unsafe_allow_html=True)

# 5. HEADER & NAVIGATION
col_logo, col_nav = st.columns([1, 1.5])

with col_logo:
    # Custom SVG Logo Recreation
    st.markdown(f"""
        <div class='nav-box' style='border:none;'>
            <div class='logo-container'>
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
    # Navigation Buttons & Language Switcher
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])
    if c1.button(t['home']): st.session_state.page = "Home"
    if c2.button(t['act']): st.session_state.page = "Take Action"
    
    # Dropdown Menu Logic
    with c3:
        menu_choice = st.selectbox("Menu ☰", ["Global Ops", "Precautionary", "Emergency Contacts", "Volunteering"], label_visibility="collapsed")
        if menu_choice == "Global Ops": st.session_state.page = "Dashboard"
        elif menu_choice == "Precautionary": st.session_state.page = "Precautionary"
        elif menu_choice == "Emergency Contacts": st.session_state.page = "Contacts"
        elif menu_choice == "Volunteering": st.session_state.page = "Volunteer"

    # Language Switcher
    with c4:
        flags = {"English": "🇬🇧", "Turkish": "🇹🇷", "Spanish": "🇪🇸", "French": "🇫🇷", "Russian": "🇷🇺", "Arabic": "🇸🇦", "Chinese": "🇨🇳", "Hindi": "🇮🇳"}
        lang = st.selectbox("", list(translations.keys()), format_func=lambda x: f"{flags[x]} {x}", label_visibility="collapsed")
        if lang != st.session_state.lang:
            st.session_state.lang = lang
            st.rerun()

st.markdown("---")

# 6. PAGE CONTENT LOGIC

if st.session_state.page == "Home":
    # ---------------- HOME / AWARENESS ----------------
    col_text, col_img = st.columns([1, 1])
    with col_text:
        st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-quote'>{t['quote']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hero-sub'>{t['sub']}</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("ℹ️ About Project"):
            with st.expander("System Overview & Technologies", expanded=True):
                st.info("""
                **Tech Stack:** Python 3.10+, Streamlit, Plotly Graph Objects.
                **Architecture:** Model-View-Controller (MVC) adaptation for Data Science web apps.
                **Features:** Real-time JSON data parsing, Interactive geospatial mapping, hierarchical data filtering.
                """)

    with col_img:
        # Custom "Hands Connecting" Illustration Placeholder
        st.image("https://cdn-icons-png.flaticon.com/512/1063/1063376.png", width=400)

elif st.session_state.page == "Dashboard":
    # ---------------- GLOBAL OPS ----------------
    st.markdown(f"## 🌿 {t['dash']} Center")
    
    # METRICS
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Regions", "195", "Global Coverage")
    m2.metric("Disaster Zones", "11", "High Alert", delta_color="inverse")
    m3.metric("Relief Teams", "4,210", "+120 Today")
    m4.metric("Donations", "$1.2M", "+5%")

    # INTERACTIVE MAP (With Red/Green Zones)
    st.markdown("### 📡 Live Disaster Threat Map")
    zones = st.session_state.engine.get_disaster_zones()
    
    lat = [z['lat'] for z in zones]
    lon = [z['lon'] for z in zones]
    colors = [z['color'] for z in zones]
    texts = [z['type'] for z in zones]
    sizes = [z['radius'] * 1.5 for z in zones]

    fig = go.Figure()
    
    # Base Map
    fig.add_trace(go.Scattergeo(
        locationmode='country names',
        marker=dict(size=2, color='#263E3A'),
    ))
    
    # Disaster Zones Layer
    fig.add_trace(go.Scattergeo(
        lat=lat, lon=lon,
        text=texts,
        mode='markers',
        marker=dict(size=sizes, color=colors, opacity=0.7, line=dict(width=1, color='white')),
        name='Alert Zones'
    ))
    
    fig.update_geos(
        projection_type="natural earth",
        showland=True, landcolor="#E0E0E0",
        showocean=True, oceancolor="#FFFFFF",
        showcountries=True, countrycolor="#999"
    )
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

    # INVENTORY EXPLORER (All 195 Countries)
    st.markdown("### 📦 Global Inventory Database")
    c_cont, c_coun = st.columns(2)
    
    selected_continent = c_cont.selectbox("Select Continent", list(st.session_state.engine.world_data.keys()))
    selected_country = c_coun.selectbox("Select Country", st.session_state.engine.world_data[selected_continent])
    
    inv = st.session_state.engine.get_inventory(selected_country)
    
    # Display Inventory as Professional Cards
    st.info(f"Logistics Status: **{selected_country}**")
    ic1, ic2, ic3, ic4, ic5 = st.columns(5)
    items = list(inv.items())
    ic1.metric(items[0][0], f"{items[0][1]:,}")
    ic2.metric(items[1][0], f"{items[1][1]:,}")
    ic3.metric(items[2][0], f"{items[2][1]:,}")
    ic4.metric(items[3][0], f"{items[3][1]:,}")
    ic5.metric(items[4][0], f"{items[4][1]:,}")

elif st.session_state.page == "Precautionary":
    # ---------------- PRECAUTIONARY MEASURES ----------------
    st.title("🛡️ Frontline Safety Protocols")
    
    with st.expander("🔴 Earthquake (Immediate Action)", expanded=True):
        st.markdown("""
        1. **DROP, COVER, HOLD ON:** Do not run outside.
        2. **Indoors:** Stay away from glass, windows, outside doors and walls.
        3. **Outdoors:** Move away from buildings, streetlights, and utility wires.
        """)
    
    with st.expander("🌊 Tsunami (Coastal Warning)"):
        st.markdown("""
        1. **Get to High Ground:** If you feel strong shaking, move to higher ground immediately.
        2. **Do Not Wait:** Do not wait for an official warning.
        3. **Stay Out:** Tsunami waves arrive in a series; the first wave may not be the largest.
        """)
        
    with st.expander("🌪️ Hurricane / Cyclone"):
        st.markdown("Secure windows, stock up on water, and follow evacuation orders immediately.")

elif st.session_state.page == "Contacts":
    # ---------------- EMERGENCY CONTACTS ----------------
    st.title("☎️ Global Emergency Hotlines")
    st.markdown("Rapid access to emergency services by country.")
    
    # Mock Data for contacts
    contacts = [
        {"Country": "Turkey", "Ambulance": "112", "Police": "155", "Fire": "110"},
        {"Country": "USA", "Ambulance": "911", "Police": "911", "Fire": "911"},
        {"Country": "UK", "Ambulance": "999", "Police": "999", "Fire": "999"},
        {"Country": "India", "Ambulance": "102", "Police": "100", "Fire": "101"},
        {"Country": "China", "Ambulance": "120", "Police": "110", "Fire": "119"},
        {"Country": "Japan", "Ambulance": "119", "Police": "110", "Fire": "119"},
    ]
    st.dataframe(contacts, use_container_width=True)

elif st.session_state.page == "Volunteer":
    # ---------------- VOLUNTEERING ----------------
    st.title("🤝 Join the Global Grid")
    st.markdown("We need specialists for the 2026 deployment roster.")
    
    v1, v2 = st.columns(2)
    with v1:
        st.text_input("Full Name")
        st.text_input("Email")
        st.selectbox("Expertise", ["Medical - Trauma Surgeon", "Medical - Nurse", "Urban Search & Rescue", "K9 Unit Handler", "Logistics Officer"])
    with v2:
        st.selectbox("Preferred Deployment Zone", list(st.session_state.engine.world_data.keys()))
        st.text_area("Certifications / Experience")
        if st.button("Submit Application"):
            st.success("Application received. The Unity Grid coordinator will contact you within 24 hours.")

elif st.session_state.page == "Take Action":
    # ---------------- TAKE ACTION (DONATIONS) ----------------
    st.title("🚀 Power the Mission")
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("### 💳 Direct Aid Contribution")
        st.info("Your funds go directly to purchasing Medical Kits and Water Filtration units.")
        amount = st.select_slider("Select Donation Amount ($)", options=[10, 50, 100, 500, 1000])
        if st.button(f"Donate ${amount}"):
            st.balloons()
            st.success(f"Thank you! ${amount} has been securely processed via Stripe.")
            
    with c2:
        st.markdown("### 📦 Corporate Partnership")
        st.write("For bulk supply donations (Tents, Generators), please contact supply@unitygrid.org")
