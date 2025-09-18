# GitHub Activity Analyzer

This project is a web application to analyze and visualize GitHub user activity. It fetches data from the GitHub API and displays it in an interactive dashboard.

## Demo

https://github-activity-analyzer-e34l.onrender.com/

## Features

*   Fetches user activity data from GitHub.
*   Visualizes activity data using interactive charts.
*   Provides a dashboard to view the analysis.

## Requirements

*   Python 3.8+
*   A GitHub account and a Personal Access Token (PAT).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/github-activity-analyzer.git
    cd github-activity-analyzer
    ```

2.  Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a `.env` file by copying the example file:
    ```bash
    cp .env.example .env
    ```

2.  Open the `.env` file and add your GitHub Personal Access Token:
    ```
    GITHUB_TOKEN="your_github_pat"
    ```

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Then open your web browser and go to `http://localhost:8501`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Plans

I'm considering developing the next version with Django or Flask.
