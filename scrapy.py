import scrapy
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.yellowpages.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements that contain the article titles
    # You'll need to inspect the website's HTML structure to determine the appropriate selectors
    title_elements = soup.find_all('h2', class_='article-title')

    # Loop through the title elements and print the titles
    for title_element in title_elements:
        print(title_element.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
