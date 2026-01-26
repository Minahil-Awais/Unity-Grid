import streamlit as st
import time
from models import UnityGridEngine

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Unity Grid", page_icon="🌿", layout="wide")

# 2. CUSTOM AESTHETIC CSS (The "Pro" Look)
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');

    /* COLOR PALETTE VARIABLES */
    :root {
        --primary-green: #263E3A;
        --accent-brown: #945031;
        --bg-white: #F5F5F5;
        --text-dark: #1a1a1a;
    }

    /* GLOBAL STYLES */
    .stApp {
        background-color: var(--bg-white);
        font-family: 'Montserrat', sans-serif;
    }
    
    /* HIDE DEFAULT ELEMENTS */
    [data-testid="stSidebar"] {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}

    /* CUSTOM NAVBAR */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        background-color: transparent;
    }
    .logo-box {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .logo-text {
        font-size: 28px;
        font-weight: 700;
        color: var(--primary-green);
        margin: 0;
    }
    .logo-icon {
        font-size: 32px;
        color: var(--accent-brown);
    }
    
    /* HERO SECTION */
    .hero-container {
        text-align: center;
        padding: 80px 20px;
    }
    .hero-quote {
        font-size: 56px;
        font-weight: 800;
        color: var(--primary-green);
        text-transform: uppercase;
        letter-spacing: 2px;
        line-height: 1.1;
        margin-bottom: 20px;
    }
    .hero-sub {
        font-size: 18px;
        color: #555;
        max-width: 600px;
        margin: 0 auto 30px auto;
        line-height: 1.6;
    }

    /* METRIC CARDS */
    div[data-testid="stMetricValue"] {
        color: var(--accent-brown);
        font-size: 24px;
    }
    div[data-testid="stMetricLabel"] {
        color: var(--primary-green);
        font-weight: bold;
    }
    
    /* BUTTON STYLING OVERRIDES */
    .stButton button {
        background-color: var(--primary-green);
        color: white;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: var(--accent-brown);
        color: white;
        transform: scale(1.02);
    }
    
    /* TABLE STYLING */
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. INITIALIZE ENGINE
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
engine = st.session_state.engine

# STATE MANAGEMENT FOR NAVIGATION
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def navigate_to(page):
    st.session_state.page = page

# 4. CUSTOM HEADER (Logo Left, Buttons Right)
col_head1, col_head2 = st.columns([1, 1])

with col_head1:
    # Logo and Name (Using HTML/CSS to match your image exactly)
    st.markdown("""
        <div class='logo-box'>
            <div class='logo-icon'>❖</div>
            <div class='logo-text'>Unity <span style='color:#945031'>Grid</span></div>
        </div>
    """, unsafe_allow_html=True)

with col_head2:
    # Navigation Buttons aligned to the right
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("Awareness", use_container_width=True):
            navigate_to("Home")
    with c2:
        if st.button("Take Action", use_container_width=True):
            navigate_to("Volunteer")
    with c3:
        # The Menu is a dropdown in the UI, but we simulate it as a button to Dashboard here
        if st.button("Dashboard ☰", use_container_width=True):
            navigate_to("Dashboard")

st.markdown("---")

# 5. MAIN PAGE CONTENT LOGIC

if st.session_state.page == "Home":
    # HERO SECTION
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    
    # You can replace this URL with the local path if you upload the image file to 'src'
    st.image("https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    
    st.markdown("""
        <h1 class='hero-quote'>HUMANITY<br>WITHOUT BORDERS</h1>
        <p class='hero-sub'>
            <b>About:</b> A global humanitarian logistics system designed to optimize disaster relief 
            and volunteer deployment across international hubs, including Türkiye.
        </p>
    """, unsafe_allow_html=True)
    
    # "About Project" Functional Button
    if st.button("About Project"):
        with st.expander("Overview & Technologies", expanded=True):
            st.info("""
            **System Architecture:**
            * **Frontend:** Streamlit (Python)
            * **Backend:** Object-Oriented Python (UnityGrid Engine)
            * **Data Structure:** JSON-based persistence with simulated Real-Time Global Nodes.
            
            **Key Features:**
            * Live tracking of supply chains across 15+ countries.
            * Volunteer filtering by Medical, Rescue, and Engineering expertise.
            * Centralized command for rapid disaster response.
            """)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "Dashboard":
    st.title("📊 Global Operations Center")
    st.markdown("Real-time statistics from disaster rehabilitation centers.")
    
    # REAL TIME STATS ROW
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Hubs", len(engine.centers), "+2 New")
    m2.metric("Total Supply Tons", "14,250", "+5%")
    m3.metric("Medical Personnel", "1,840", "+12")
    m4.metric("System Status", "OPTIMAL", delta_color="normal")
    
    st.markdown("### 🌍 Global Inventory (Live Feed)")
    
    # Display the "All Cities" Data
    # Convert object list to dictionary for the dataframe
    data_list = []
    for c in engine.centers:
        row = {"City": c.city, "Country": c.country, "Region": c.region, **c.inventory}
        data_list.append(row)
        
    st.dataframe(data_list, use_container_width=True)

elif st.session_state.page == "Volunteer":
    st.title("🤝 Take Action")
    st.markdown("Join the grid. Humanity needs your expertise.")
    
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full Name")
        skill = st.selectbox("Expertise", ["Medical - Trauma", "Search & Rescue", "Civil Engineering", "Translator"])
    with c2:
        contact = st.text_input("Email Address")
        location = st.selectbox("Preferred Deployment Region", ["Middle East", "Europe", "Asia-Pacific", "Africa"])
        
    if st.button("Submit Application"):
        st.success(f"Thank you, {name}. Your profile has been added to the {skill} roster.")
        time.sleep(2)
        st.balloons()
