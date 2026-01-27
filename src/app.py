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
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');
    
    :root {
        --primary: #263E3A; 
        --accent: #945031;
    }

    .stApp { background-color: white; font-family: 'Montserrat', sans-serif; }
    
    .logo-title { font-size: 36px; font-weight: 800; color: var(--primary); letter-spacing: -1px; }
    .logo-sub { color: var(--accent); }

    .hero-quote { 
        font-size: 48px; 
        font-weight: 800; 
        color: var(--primary); 
        line-height: 1.1; 
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .hero-text {
        font-size: 18px; color: #555; line-height: 1.6;
        border-left: 5px solid var(--accent); padding-left: 15px; margin-bottom: 30px;
    }

    .stButton button {
        background-color: var(--primary); color: white; border-radius: 4px; font-weight: bold; border: none; padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: var(--accent);
    }
    
    /* Precaution Cards */
    .prec-card { background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid var(--accent); margin-bottom: 10px; }
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
        if lang != st.session_state.
