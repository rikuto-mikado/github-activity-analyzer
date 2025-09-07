import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application Configuration Class"""

    # GitHub API Configuration
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    GITHUB_API_BASE_URL = "https://api.github.com"

    # Streamlit Configuration
    APP_TITLE = "GitHub Activity Analyzer"
    APP_DESCRIPTION = "Analyze and visualize your GitHub activity"

    # General
    DEFAULT_PER_PAGE = 30
    MAX_REPOS = 100
    CACHE_TTL = 300

    # UI
    THEME_CONFIG = {
        "primaryColor": "#FF6B6B",
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#262730",
    }

    @classmethod
    def validate_config(cls) -> bool:
        """Verify the validity of the settings"""
        if not cls.GITHUB_TOKEN:
            print("Warning: GITHUB_TOKEN is not set. Some features may be limited.")
            return False
        return True

    @classmethod
    def get_github_token(cls) -> str:
        """Obtaining a GitHub token"""
        return cls.GITHUB_TOKEN or ""
