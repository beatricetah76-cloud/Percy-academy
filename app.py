import streamlit as st
import random
import time

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Percy Academy", page_icon="🔬", layout="wide")

# --- INITIALIZE DATABASE / STATE ---
if 'xp' not in st.session_state:
    st.session_state.xp = 0
if 'badges' not in st.session_state:
    st.session_state.badges = []
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = [{"user": "John_Doe", "msg": "How do I remember the noble gases?"}]

# --- CONTENT DATA ---
CONTENT = {
    "Physics": {
        "lesson": "Newton's Third Law: For every action, there is an equal and opposite reaction.",
        "experiment": "The Balloon Rocket: Tape a straw to a balloon on a string and watch it propel!",
        "quiz_q": "If a bird pushes down on air, the air pushes ___ on the bird.",
        "options": ["Down", "Up", "Sideways"],
        "correct": "Up",
        "fact": "A neutron star is so dense that a teaspoon of it would weigh 6 billion tons."
    },
    "Chemistry": {
        "lesson": "Exothermic Reactions: A chemical reaction that releases energy through light or heat.",
        "experiment": "Elephant Toothpaste: Mix yeast, hydrogen peroxide, and dish soap.",
        "quiz_q": "Which of these is an example of an exothermic reaction?",
        "options": ["Ice melting", "A candle flame", "Photosynthesis"],
        "correct": "A candle flame",
        "fact": "There is enough gold inside Earth to coat the entire surface in 1.5 feet of it."
    },
    "Biology": {
        "lesson": "The Mitochondria: Known as the powerhouse of the cell, it generates ATP.",
        "experiment": "DNA Extraction: Mash a strawberry with salt and alcohol to see DNA strands.",
        "quiz_q": "What molecule does the mitochondria produce for energy?",
        "options": ["Glucose", "ATP", "Chlorophyll"],
        "correct": "ATP",
        "fact": "The human body has more bacterial cells than human cells."
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Percy Academy")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", ["Dashboard", "Science Lessons", "Practical Experiments", "Community Forum"])

# --- SHARED FUNCTIONS ---
def add_xp(amount):
    st.session_state.xp += amount
    if st.session_state.xp >= 100 and "Science Apprentice" not in st.session_state.badges:
        st.session_state.badges.append("Science Apprentice")
        st.toast("🏆 New Badge Unlocked: Science Apprentice!")

# --- DASHBOARD PAGE ---
if page == "Dashboard":
    st.title("👨‍🔬 Student Dashboard")
    
    # Progress Tracking
    col1, col2, col3 = st.columns(3)
    col1.metric("Total XP", f"{st.session_state.xp}")
    col2.metric("Badges Earned", len(st.session_state.badges))
    col3.metric("Level", (st.session_state.xp // 500) + 1)

    st.markdown("### Your Achievements")
    if st.session_state.badges:
        for badge in st.session_state.badges:
            st.success(f"🏅 {badge}")
    else:
        st.info("Complete quizzes to earn your first badge!")

    st.markdown("---")
    st.markdown("### 💡 Daily Trivial Fact")
    random_subject = random.choice(list(CONTENT.keys()))
    st.info(CONTENT[random_subject]['fact'])

# --- LESSONS PAGE ---
elif page == "Science Lessons":
    subject = st.selectbox("Choose a Subject", ["Physics", "Chemistry", "Biology"])
    st.title(f"{subject} Notes")
    
    # Lesson Details
    st.markdown(f"### Understanding {subject}")
    st.write(CONTENT[subject]['lesson'])
    
    # Diagram Placeholder
    st.info(f"🖼️ [Interactive Diagram of {subject} Principles]")
    
    st.markdown("---")
    st.subheader("📝 Quick Quiz")
    q = CONTENT[subject]['quiz_q']
    answer = st.radio(q, CONTENT[subject]['options'])
    
    if st.button("Submit Answer"):
        if answer == CONTENT[subject]['correct']:
            st.success("Correct! +50 XP")
            add_xp(50)
        else:
            st.error("Try again! Review the notes above.")

# --- EXPERIMENTS PAGE ---
elif page == "Practical Experiments":
    st.title("🧪 The Practical Lab")
    subject = st.radio("Subject", ["Physics", "Chemistry", "Biology"])
    
    st.markdown(f"### Current Experiment: {CONTENT[subject]['experiment']}")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Placeholder for experiment video
    
    st.checkbox("I have completed this experiment safely.")
    if st.button("Claim XP"):
        st.balloons()
        add_xp(100)

# --- FORUM PAGE ---
elif page == "Community Forum":
    st.title("💬 Student Community")
    
    # Post a new message
    with st.form("forum_form"):
        new_post = st.text_input("Ask a question...")
        submitted = st.form_submit_button("Post")
        if submitted and new_post:
            st.session_state.forum_posts.append({"user": "You", "msg": new_post})
            
    # Display posts
    for post in reversed(st.session_state.forum_posts):
        with st.chat_message(post['user']):
            st.write(post['msg'])

# --- OFFLINE ACCESS & DARK MODE NOTE ---
st.sidebar.markdown("---")
st.sidebar.caption("🌙 Dark Mode: Enabled by System")
st.sidebar.caption("📁 Offline Access: Enabled