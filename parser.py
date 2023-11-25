# parser.py

from selenium import webdriver
import time

# Base URL
base_url = "https://seocho.seocholib.or.kr/KeywordSearchResult/"

# Specify the path to the chromedriver executable (replace with the path on your system)
driver_path = '/path/to/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open the file
with open('korean_test.txt', 'r', encoding='utf-8') as file:
    # Read the file contents
    contents = file.read()
    # Remove spaces and convert the string to a list
    list_chars = [char for char in contents if char.strip()]

# List to store HTML contents
html_contents = []

# For each character in the list
for char in list_chars:
    # Construct the URL
    url = base_url + char
    # Go to the webpage
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)
    # Get the HTML content of the webpage
    html_content = driver.page_source
    # Add the HTML content to the list
    html_contents.append(html_content)

# Close the driver
driver.quit()

# Print the HTML contents
for html in html_contents:
    print(html)
