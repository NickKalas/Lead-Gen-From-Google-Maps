# 🏢 Lead Generator & Live Business Explorer

This app acts like a digital scout, automating the tedious task of collecting local business leads.

When you submit a search query like "Pizza, London" the program handles everything in four quick steps:

    Scrapes: It launches an automated browser to bypass cookie consent popups and scroll through local listings.

    Extracts: It clicks each business card to gather its name, address, phone number, website, and review scores.

    Stores: It instantly saves this information into a local database.db file to prevent data loss.

    Displays: It loads the data onto an interactive Streamlit dashboard for effortless profile browsing.

## Table of contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and initialize the application environment, execute these four simple setup steps:

    Clone: Download the repository source files locally using the git clone command in your terminal.

    Environment: Create and activate an isolated virtual Python environment (venv) to keep dependencies separated.

    Packages: Run pip install -r requirements.txt to automatically download Streamlit, Playwright, and BeautifulSoup.

    Browsers: Run playwright install chromium to provision the automated, standalone browser binaries required for scraping.

Once completed, type streamlit run app.py to boot up your dashboard interface instantly!

## Usage

To operate the pipeline and explore your leads, follow these four simple steps:

      Launch: Boot up the dashboard interface by running streamlit run app.py in your terminal.

      Configure: Enter your target parameters (like "Burgers, Athens") and choose how many leads to collect.

      Extract: Click the tracking action button to spin up the automated background browser and scrape data.

      Explore: Use the interactive dropdown menu to instantly view live, structured company profile cards straight from disk.

## Contributing

* **Open Source:** This project is open for improvement and welcoming to new ideas.
* **Fork & Branch:** To contribute, simply fork the repository, set up a new feature branch, and implement your code updates.
* **Pull Request:** Submit a clear pull request detailing your changes for a quick review and merge.
  
## License
* **MIT License:** This pipeline is distributed completely free under the standard MIT License.
* **Permissions:** You are fully allowed to modify, distribute, copy, or use this software for both personal and commercial automation ventures.
* **Condition:** Just include the original copyright notice in any copies you distribute.
