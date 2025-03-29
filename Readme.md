# AI Web Scraper

A powerful web scraping tool that combines web automation with AI to intelligently extract and parse information from websites. This tool uses Streamlit for the interface, Selenium for web scraping, and LangChain with Ollama for intelligent content parsing.

## Project Description

The AI Web Scraper is designed to:
- Scrape websites using automated browser control
- Clean and process HTML content
- Use AI to intelligently parse and extract specific information
- Provide a user-friendly interface for easy interaction

## Tools & Technologies Used

- **Python** - Primary programming language
- **Streamlit** - Web interface and application framework
- **Selenium** - Web automation and scraping
- **BeautifulSoup4** - HTML parsing and cleaning
- **LangChain** - AI integration framework
- **Ollama** - Local AI model for content parsing
- **ChromeDriver** - Browser automation driver

## Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-webscraper
```

2. Create and activate a virtual environment:
```bash
python -m venv ai_scrape
source ai_scrape/bin/activate  # On Windows, use: ai_scrape\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install ChromeDriver:
   - Download ChromeDriver compatible with your Chrome browser version
   - Place the `chromedriver` executable in the project root directory

5. Install and run Ollama:
   - Follow instructions at [Ollama's official website](https://ollama.ai/)
   - Pull the required model:
```bash
ollama pull llama3

ollama run llama3
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Enter a website URL in the input field
3. Click "Scrape Site" to fetch the content
4. Enter your parsing requirements in the description field
5. Click "Parse Content" to extract specific information

## Video Demo

[Coming Soon] A video demonstration of the AI Web Scraper in action will be added here.

## Notes

- Make sure to comply with websites' robots.txt and terms of service
- Some websites may block automated access
- For production use, consider using proxy services or API endpoints when available
