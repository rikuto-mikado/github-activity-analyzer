import requests
import os
from typing import Dict, List, Optional
from datetime import datetime


class GitHubAPI:
    def __init__(self, token: Optional[str] = None):
        """Initialise the GitHub API client"""
        self.base_url = "https://api.github.com"
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Activity-Analyzer/1.0",
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def get_user_info(self, username: str) -> Dict:
        """Retrieve user information"""
        try:
            url = f"{self.base_url}/users/{username}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user info: {e}")
            return {}

    def get_user_repos(self, username: str, per_page: int = 30) -> List[Dict]:
        """Retrieve the user's list of repositories"""
        try:
            url = f"{self.base_url}/users/{username}/repos"
            params = {"sort": "updated", "per_page": per_page, "type": "all"}
            response = requests.get(
                url, headers=self.headers, params=params, timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []

    def get_user_events(self, username: str, per_page: int = 30) -> List[Dict]:
        """Retrieve the user's recent activity"""
        try:
            url = f"{self.base_url}/users/{username}/events"
            params = {"per_page": per_page}
            response = requests.get(
                url, headers=self.headers, params=params, timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching user events: {e}")
            return []

    def get_rate_limit(self) -> Dict:
        """Verifying API limits"""
        try:
            url = f"{self.base_url}/rate_limit"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching rate limit: {e}")
            return {}

    def test_connection(self) -> bool:
        """API connection test"""
        try:
            rate_limit = self.get_rate_limit()
            return bool(rate_limit)
        except:
            return False
