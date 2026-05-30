from pathlib import Path

import sys

import streamlit as st

BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(BASE_DIR / "src"))

from recommendation import recommend


#CSS CODE

st.markdown("""
<style>

/* ==========================
   GLOBAL THEME
========================== */

.stApp {
    background-color: #050505;
}

/* ==========================
   SIDEBAR
========================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111827,
        #0f172a
    );

    border-right: 1px solid #1f2937;
}

/* Sidebar collapse button */

[data-testid="collapsedControl"] {
    background-color: #161b22;
    color: white !important;
    border-radius: 8px;
    padding: 6px;
}

/* ==========================
   TITLE
========================== */

.cinewise-title {

    font-family: 'Bebas neue', sans-serif;

    font-size: 4.5rem;

    font-weight: 800;
            
    text-align: center;

    color: #ffffff;

    -webkit-text-stroke: 1px #161b22;

    text-shadow:
        0 0 10px rgba(255,255,255,0.1);
}

.cinewise-subtitle {

    text-align: center;

    color: #b5b5b5;

    font-size: 1.2rem;

    margin-bottom: 40px;
}

/* ==========================
   BUTTON
========================== */

.stButton > button {

    width: 160px;

    display: block;

    margin-left: auto;

    margin-right: auto;

    background-color: #1DB954;

    color: white;

    border: none;

    border-radius: 12px;

    font-weight: 700;

    padding: 12px;
}

.stButton > button:hover {

    background-color: #1ed760;

    transform: translateY(-2px);

    box-shadow:
        0 0 15px rgba(29,185,84,0.4);
}

/* ==========================
   INPUTS
========================== */

.stSelectbox div[data-baseweb="select"] {

    background-color: #1e293b !important;

    border: 1px solid #334155 !important;

    color: white !important;

    border-radius: 12px;
}

.stNumberInput input {

    background-color: #0a0f1a !important;

    color: white !important;

    border: 1px solid #334155 !important;

    border-radius: 12px;
}

.stSelectbox label,
.stNumberInput label {

    color: white !important;

    font-weight: 500;
}

/* ==========================
   DEVELOPER BADGE
========================== */

.developer-badge {
    position: fixed;
    top: 60px;
    right: 25px;

    color: white;
    font-size: 16px;
    font-weight: 600;

    z-index: 9999;
}

/* ==========================
   CONTAINER CARDS
========================== */

[data-testid="stVerticalBlockBorderWrapper"] {

    background: linear-gradient(
        145deg,
        #10151c,
        #151b24
    );

    border: 1px solid #232c37;

    border-radius: 20px;

    padding: 18px;

    margin-bottom: 18px;

    max-width: 750px;

    margin-left: auto;

    margin-right: auto;

    transition: all 0.3s ease;
}

/* ==========================
   PROGRESS BAR
========================== */

.stProgress > div > div > div > div {

    background-color: #1DB954;
            
}          
            
</style>
""", unsafe_allow_html=True)


#HTML CODE

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">       
    
    <div class="developer-badge">
        Developed by Jyothis P K
    </div>

    <div class="cinewise-title">
    📽️ CineWise 📽️
    </div>

    <div class="cinewise-subtitle">
    ... Pick Your Cinema Wisely ...
    </div>
    """, unsafe_allow_html=True)


#python code

with st.sidebar :

    st.subheader("🎛️ Preferences")

    
    region = st.selectbox("select region",[
            "kerala",           
            "tamil nadu",       
            "karnataka",        
            "andhra pradesh",    
            "telangana",         
            "maharashtra",      
            "west bengal",      
            "punjab",            
            "gujarat",           
            "rajasthan",         
            "uttar pradesh",     
            "madhya pradesh",    
            "bihar",            
            "delhi",             
            "odisha",            
            "north east",        
            "jammu and kashmir", 
            "north india",      
            "south india"]
            )

    weather = st.selectbox("select weather",[
            "rainy","sunny","cloudy","winter","hot","foggy","calm"
            ]
            )

    age=st.number_input(
        "enter you age",
        min_value=1,
        max_value=100,
        value=18
    )
    
    if "movies" not in st.session_state:
        st.session_state.movies = []

    col1, col2, col3 = st.columns([1,4,1])

    with col2:
        if st.button("Recommend"):
            st.session_state.movies = recommend(
                region,
                weather,
                age
            )

for movie in st.session_state.movies:

        left, center, right = st.columns([1,5,1])

        with center:

            with st.container():

                st.markdown(
                    f"### 🎥 {movie['name']}"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"🌐 {movie['language']}")
                    st.write(f"🎭 {movie['genre']}")

                with col2:
                    st.write(f"🗓️ {movie['year']}")
                    st.write(f"⭐ {movie['rating']}")

                st.progress(movie["score"])

                st.write(
                    f"🎯 Match Score: {movie['score']*100:.0f}%"
                )


#CSS CODE TO HIDE INBUILT STREAMLIT UI FEATURES

st.markdown("""
<style>

footer {
    visibility: hidden;
}

header {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)
