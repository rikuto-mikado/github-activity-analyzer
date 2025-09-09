import streamlit as st
import pandas as pd
import plotly.express as px

def display_user_info(user_info):
    """
    Displays user information metrics (followers, following, etc.) in columns.

    Args:
        user_info (dict): A dictionary containing user information.
    """
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👤 Followers", user_info.get("followers", 0))
    with col2:
        st.metric("👥 Following", user_info.get("following", 0))
    with col3:
        st.metric("📂 Public Repos", user_info.get("public_repos", 0))
    with col4:
        st.metric("📍 Location", user_info.get("location", "N/A"))

def display_language_distribution(languages):
    """
    Displays a pie chart of the user's programming language distribution.

    Args:
        languages (dict): A dictionary of language counts.
    """
    if not languages:
        st.warning("No language data to display.")
        return

    df_lang = pd.DataFrame(list(languages.items()), columns=["Language", "Count"])
    fig = px.pie(
        df_lang,
        values="Count",
        names="Language",
        title="Programming Languages Distribution",
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

def display_activity_timeline(processed_events):
    """
    Displays the user's recent activity timeline.

    Args:
        processed_events (list): A list of formatted event strings.
    """
    if not processed_events:
        st.warning("No recent activity found.")
        return

    st.write("Recent Activities:")
    for event_string in processed_events:
        st.write(event_string)

def display_quick_stats(user_info, total_stars, total_forks):
    """
    Displays quick statistics like total stars, forks, and account creation date.

    Args:
        user_info (dict): Dictionary with user information.
        total_stars (int): Total number of stars.
        total_forks (int): Total number of forks.
    """
    st.metric("⭐ Total Stars", total_stars)
    st.metric("🍴 Total Forks", total_forks)
    
    created_at = user_info.get("created_at")
    st.metric(
        "📅 Account Created",
        created_at[:10] if created_at else "Unknown"
    )

def display_top_repos(top_repos):
    """
    Displays a list of the user's top repositories.

    Args:
        top_repos (list): A list of top repository dictionaries.
    """
    if not top_repos:
        st.info("No repositories to display.")
        return

    for i, repo in enumerate(top_repos):
        name = repo.get("name", "Unknown")
        stars = repo.get("stargazers_count", 0)
        description = repo.get("description", "No description")
        
        # Truncate description if it's too long
        if description and len(description) > 50:
            description = description[:50] + "..."

        st.write(f"{i+1}. {name} ⭐{stars}")
        st.caption(description)
