import streamlit as st
from models import UnityGridEngine

# 1. Page Configuration
st.set_page_config(page_title="UnityGrid | Global Response", page_icon="🌍", layout="wide")

# 2. Advanced Professional Styling (CSS)
st.markdown("""
    <style>
    /* Hide Sidebar for a clean web-app look */
    [data-testid="stSidebar"] {display: none;}
    .block-container {padding-top: 2rem;}
    
    /* Global Background */
    .stApp {
        background-color: #FDFDFD;
    }

    /* Top Navigation Simulation */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        border-bottom: 1px solid #eee;
        margin-bottom: 30px;
    }

    /* Hero Text Styling */
    .hero-title {
        font-size: 4.5rem;
        font-weight: 850;
        color: #1a1a1a;
        line-height: 0.9;
        margin-bottom: 0px;
    }
    .hero-green {
        color: #4CAF50;
        font-size: 4.5rem;
        font-weight: 850;
        margin-top: -10px;
    }
    .hero-desc {
        color: #555;
        font-size: 1.1rem;
        max-width: 500px;
        margin-top: 20px;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #000000;
        color: white;
        border-radius: 0px;
        padding: 10px 30px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True) # FIXED: changed from stdio to html

# 3. Initialize Data Engine
if 'engine' not in st.session_state:
    st.session_state.engine = UnityGridEngine()
engine = st.session_state.engine

# 4. TOP CONTROL PANEL (Navigation)
col_logo, col_space, col_menu = st.columns([1, 1, 1])
with col_logo:
    st.markdown("<h3 style='margin:0;'>🌍 UNITYGRID</h3>", unsafe_allow_html=True)
with col_menu:
    choice = st.selectbox(
        "Menu", 
        ["Home / Awareness", "Logistics Dashboard", "Volunteer Registry", "Specialist Search"],
        label_visibility="collapsed"
    )

st.markdown("---")

# 5. PAGE LOGIC
if choice == "Home / Awareness":
    col_text, col_img = st.columns([1.2, 1])
    
    with col_text:
        st.markdown("<div style='background-color: #4CAF50; width: 60px; height: 12px; margin-bottom: 30px;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 class='hero-title'>DISASTERS</h1>", unsafe_allow_html=True)
        st.markdown("<h1 class='hero-title'>WON'T AFFECT</h1>", unsafe_allow_html=True)
        st.markdown("<h1 class='hero-green'>UNITYGRID</h1>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class='hero-desc'>
                UnityGrid is a professional logistics coordination platform designed to optimize 
                humanitarian aid following the February 6th earthquakes and future global crises.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ABOUT PROJECT"):
            st.toast("Redirecting to Documentation...")

    with col_img:
        # High quality image that looks like your globe reference
        st.image("https://images.unsplash.com/photo-1516937941344-00b4e0337589?auto=format&fit=crop&q=80&w=800")

elif choice == "Logistics Dashboard":
    st.header("📊 Global Resource Inventory")
    data = [{"City": c.city, "Country": c.country, **c.inventory} for c in engine.centers]
    st.dataframe(data, use_container_width=True)

elif choice == "Volunteer Registry":
    st.header("🤝 Register Professional Aid")
    with st.form("reg_form"):
        name = st.text_input("Full Name")
        spec = st.selectbox("Specialty", ["Medical", "Rescue", "Logistics"])
        if st.form_submit_button("Register to Grid"):
            engine.volunteers.append({"name": name, "spec": spec, "contact": "Secured"})
            engine.save_state()
            st.success("Successfully registered to the global database!")

elif choice == "Specialist Search":
    st.header("🔍 Search Global Network")
    query = st.text_input("Enter specialty (e.g., Medical)").lower()
    if query:
        results = [v for v in engine.volunteers if v['spec'].lower() == query]
        if results:
            for r in results:
                st.info(f"👤 {r['name']} | Specialty: {r['spec']}")
        else:
            st.warning("No specialists found for that category.")
