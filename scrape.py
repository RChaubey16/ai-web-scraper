# Selenium allows use to control the web browser and interact with the web page.
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


def scrape_website(website):
    print("Launching chrome browser...")

    # TODO: Use a service like brightData to bypass the captcha's and not get detected as bots.
    chrome_driver_path = "./chromedriver"
    # Chrome options allow us to control the chrome browser in a specific mode like we can ignore images and stuff.
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded....")
        html = driver.page_source
        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if (body_content):
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    # Splitting the DOM content into chunks of maximum length of 6000 characters.
    return [
        dom_content[i:i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
