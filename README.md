# 🏢 Lead Generator & Live Business Explorer

A modern, automated pipeline engineered to extract local business leads directly from Google Maps and explore them via an interactive, live dashboard web application.

Built natively in Python using Playwright for programmatic browser automation, BeautifulSoup4 for structured content analysis, SQLite for asynchronous local data warehousing, and Streamlit for real-time visualization.
🚀 Key Features

    Asynchronous Browser Automation: Employs Playwright to emulate human interaction, handle cookies/consent dialog overlays automatically, and sequentially navigate local data feeds.

    Anti-Bot Telemetry Mitigation: Utilizes jitter-randomized event timelines to bypass automation pattern signatures safely.

    Robust DOM Extractors: Leverages advanced, fallback-supported multi-lingual XPath expressions to reliably pull entity names, structural addresses, digital contact nodes, review volumetric tallies, and mean rating averages.

    State Isolation Engine: Isolated threaded database connections prevent race-condition write conflicts inside SQLite during asynchronous extraction runs.

    Live Metrics Explorer Dashboard: Features a Streamlit interface tracking active lead pipelines directly from disk, with elegant fallback layout modes if extraction queues are empty.

🛠️ System Architecture

The pipeline is split into three core modules optimized for separation of concerns:

├── app.py          # Frontend Layout Logic (Streamlit Dashboard & Inputs)
├── main.py         # Automation Engine (Playwright Scraper & DOM Parsing)
├── database.py     # Local Data Warehouse (SQLite Initializer & Writer)
└── requirements.txt # Explicit Package Dependency Map

📦 Prerequisites & Installation
1. Clone the Project Assets
Bash

git clone [https://github.com/yourusername/lead-generator.git](https://github.com/yourusername/lead-generator.git)
cd lead-generator

2. Establish a Virtual Environment & Synchronize Dependencies
Bash

# Create environment
python -m venv lead_gen

# Activate environment (Windows)
.lead_genScriptsactivate

# Activate environment (Mac/Linux)
source lead_gen/bin/activate

# Install explicit distribution packages
pip install -r requirements.txt

3. Provision the Playwright Browser Binaries

Playwright requires its standalone browser binaries to run securely. Download them to your environment with a single terminal instruction:
Bash

playwright install chromium

🖥️ Usage Guide

To boot up the complete environment including the database routing engine, run the primary Streamlit application entry point:
Bash

streamlit run app.py

How It Works:

    Configure Target Parameter Profiles: Enter your localized search context query (e.g., Pizza, Katerini or Burgers, Washington) and set your target lead collection quotas directly inside the web interface.

    Execute the Scraper: Click the "Click me to start scraping!!!" button. This automatically initializes a safe background worker instance via main.py.

    Explore the Leads Warehouse: The dashboard automatically invalidates older state caches, pulls the live rows from database.db, and updates the interactive interactive lookup layout profiles on the fly.

🗄️ Database Schema Details

Data is stored persistently in an optimized SQLite layout matrix (users table):
Column Name	Type	Key Constraint	Description
id	INTEGER	PRIMARY KEY AUTOINCREMENT	Unique Identifier Node
name	TEXT	NOT NULL UNIQUE	Unique Business Trading Title
adress	TEXT	NOT NULL	Physical Geographic Location String
phone_number	TEXT		Telephony Route Contact Value
reviews	TEXT	NOT NULL	Aggregated Review Count Node
average	TEXT	NOT NULL	Arithmetic Scoring Mean Value
website	TEXT	NOT NULL	Core Web Resource Anchor Target
🛡️ License

Distributed under the MIT License. See LICENSE for more structural detail parameters.
