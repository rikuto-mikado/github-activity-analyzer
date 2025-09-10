import streamlit as st
from utils.github_api import GitHubAPI
from config import Config
from utils import data_processor, visualizer

# --- Page Configuration ---
st.set_page_config(
    page_title=Config.APP_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    """Main function to run the Streamlit application."""
    # --- Header ---
    st.markdown(
        '<div class="main-header">📊 GitHub Activity Analyzer</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # --- Sidebar ---
    st.sidebar.title("🔧 Settings")
    username = st.sidebar.text_input(
        "GitHub Username",
        value="rikuto-mikado",
        help="Enter the GitHub username to analyze",
    )

    if not username:
        st.warning("Please enter a GitHub username.")
        return

    # --- API and Data Fetching ---
    api = GitHubAPI()
    with st.spinner("Testing API connection..."):
        if not api.test_connection():
            st.error("Failed to connect to GitHub API.")
            return

    with st.spinner(f"Fetching data for {username}..."):
        user_info = api.get_user_info(username)
        if not user_info:
            st.error(f"User '{username}' not found. Please check the username.")
            return
        repos = api.get_user_repos(username, per_page=100)
        events = api.get_user_events(username)

    # --- Data Processing ---
    with st.spinner("Processing data..."):
        language_stats = data_processor.process_language_stats(repos)
        total_stars, total_forks = data_processor.get_total_stats(repos)
        processed_events = data_processor.process_activity_events(events)
        top_repos = data_processor.get_top_repos(repos)

    # --- Main Content Display ---
    visualizer.display_user_info(user_info)
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📈 Repository Analytics")
        visualizer.display_language_distribution(language_stats)

        st.subheader("🎯 Recent Activity")
        visualizer.display_activity_timeline(processed_events)

    with col2:
        st.subheader("📊 Quick Stats")
        visualizer.display_quick_stats(user_info, total_stars, total_forks)

        st.subheader("🏆 Top Repositories")
        visualizer.display_top_repos(top_repos)


if __name__ == "__main__":
    main()
