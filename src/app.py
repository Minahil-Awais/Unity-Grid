import streamlit as st
import plotly.graph_objects as go
from models import UnityGridEngine

# 1. PAGE SETUP
st.set_page_config(page_title="Unity Grid", page_icon="🌿", layout="wide")

# 2. DESIGNER CSS (Using your specific colors)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    
    :root {
        --primary: #263E3A; /* Your Green */
        --accent: #945031;  /* Your Brown */
        --bg: #F5F5F5;
    }

    .stApp { background-color: var(--bg); font-family: 'Inter', sans-serif; }
    
    /* Navigation Bar */
    .nav-container { display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; }
    .logo-text { font-size: 26px; font-weight: 700; color: var(--primary); }
    
    /* Hero Section */
    .quote-text { font-size: 50px; font-weight: 800; color: var(--primary); line-height: 1.1; margin-bottom: 20px; }
    .para-text { font-size: 18px; color: #444; line-height: 1.6; margin-bottom: 30px; }
    
    /* Hide default Streamlit elements */
    [data-testid="stSidebar"] {display: none;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. INITIALIZE
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
if 'page' not in st.session_state:
    st.session_state.page = "Home"

engine = st.session_state.engine

# 4. TOP NAVIGATION
col_logo, col_btns = st.columns([1, 1])
with col_logo:
    st.markdown(f"<div class='logo-text'>🌍 Unity <span style='color:#945031'>Grid</span></div>", unsafe_allow_html=True)
with col_btns:
    c1, c2, c3 = st.columns(3)
    if c1.button("Awareness"): st.session_state.page = "Home"
    if c2.button("Take Action"): st.session_state.page = "Volunteer"
    if c3.button("Menu ☰"): st.session_state.page = "Dashboard"

st.markdown("---")

# 5. PAGE LOGIC

if st.session_state.page == "Home":
    col_img, col_txt = st.columns([1, 1], gap="large")
    
    with col_img:
        # High-quality Illustration Placeholder (Hands forming globe)
        st.image("https://cdn-icons-png.flaticon.com/512/3843/3843034.png", width=450)
    
    with col_txt:
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        st.markdown("<p style='color:#945031; font-weight:bold; letter-spacing:2px;'>GLOBAL RESPONSE NETWORK</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='quote-text'>HUMANITY<br>WITHOUT BORDERS</h1>", unsafe_allow_html=True)
        st.markdown("""
            <p class='para-text'>
            A global humanitarian logistics system designed to optimize disaster relief 
            and volunteer deployment across international hubs, including Türkiye. 
            Unity Grid connects resources with needs in real-time.
            </p>
        """, unsafe_allow_html=True)
        if st.button("ABOUT PROJECT"):
            st.write("Unity Grid is built on Python, Streamlit, and Plotly to manage global crises efficiently.")

elif st.session_state.page == "Dashboard":
    st.markdown("<h2 style='color:#263E3A;'>🌍 Global Operations Center</h2>", unsafe_allow_html=True)
    
    # TOP METRICS
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Hubs", "42", "+2", delta_color="normal")
    m2.metric("Total Supply Tons", "84,200", "+1,450", delta_color="normal")
    m3.metric("Response Time", "4.2 hrs", "-0.5", delta_color="inverse")

    # DRILL DOWN INTERFACE
    st.markdown("### Interactive Grid Explorer")
    d1, d2, d3 = st.columns(3)
    
    continent = d1.selectbox("1. Select Continent", list(engine.world_data.keys()))
    country = d2.selectbox("2. Select Country", list(engine.world_data[continent].keys()))
    city = d3.selectbox("3. Select City Hub", engine.world_data[continent][country])

    # THE GLOBE MAP
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        projection_type="orthographic",
        showcountries=True, countrycolor="#444",
        showland=True, landcolor="#263E3A",
        showocean=True, oceancolor="#F5F5F5",
        lataxis_showgrid=False, lonaxis_showgrid=False
    )
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")
    
    col_map, col_stats = st.columns([1.5, 1])
    
    with col_map:
        st.plotly_chart(fig, use_container_width=True)
    
    with col_stats:
        st.markdown(f"#### 📦 {city} Inventory")
        inv = engine.get_inventory(city)
        for item, val in inv.items():
            st.write(f"**{item}:** {val:,}")
        st.progress(random.randint(40, 95))
        st.caption("Hub Capacity Usage")
