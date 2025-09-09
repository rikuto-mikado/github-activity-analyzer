import pandas as pd
from datetime import datetime

def process_language_stats(repos):
    """
    Analyzes repository data to count the usage of each programming language.

    Args:
        repos (list): A list of repository dictionaries from the GitHub API.

    Returns:
        dict: A dictionary where keys are language names and values are their counts.
    """
    languages = {}
    if not repos:
        return languages
    
    for repo in repos:
        lang = repo.get("language")
        if lang and lang != "Unknown":
            languages[lang] = languages.get(lang, 0) + 1
    return languages

def get_total_stats(repos):
    """
    Calculates the total number of stars and forks from a list of repositories.

    Args:
        repos (list): A list of repository dictionaries.

    Returns:
        tuple: A tuple containing the total number of stars and forks.
    """
    if not repos:
        return 0, 0
    
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    total_forks = sum(repo.get("forks_count", 0) for repo in repos)
    return total_stars, total_forks

def process_activity_events(events):
    """
    Processes a list of GitHub events to create a user-friendly activity timeline.

    Args:
        events (list): A list of event dictionaries from the GitHub API.

    Returns:
        list: A list of formatted strings describing each recent activity.
    """
    if not events:
        return []

    processed_events = []
    for event in events[:10]:  # Limit to 10 recent events
        event_type = event.get("type", "Unknown")
        repo_name = event.get("repo", {}).get("name", "Unknown")
        created_at = event.get("created_at", "")

        if created_at:
            try:
                date_obj = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                time_ago = datetime.now(date_obj.tzinfo) - date_obj
                if time_ago.days > 0:
                    time_str = f"{time_ago.days} days ago"
                else:
                    hours_ago = time_ago.seconds // 3600
                    if hours_ago > 0:
                        time_str = f"{hours_ago} hours ago"
                    else:
                        minutes_ago = time_ago.seconds // 60
                        time_str = f"{minutes_ago} minutes ago"

            except ValueError:
                time_str = "Unknown time"
        else:
            time_str = "Unknown time"

        processed_events.append(f"• {event_type} in `{repo_name}` - {time_str}")
    
    return processed_events

def get_top_repos(repos, top_n=5):
    """
    Sorts repositories by stargazers_count and returns the top N.

    Args:
        repos (list): A list of repository dictionaries.
        top_n (int): The number of top repositories to return.

    Returns:
        list: A list of the top N repository dictionaries.
    """
    if not repos:
        return []

    return sorted(
        repos, key=lambda x: x.get("stargazers_count", 0), reverse=True
    )[:top_n]
