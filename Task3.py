import requests
from bs4 import BeautifulSoup

# URL of the static web page
url = 'https://www.flipkart.com/'

# Send a GET request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract and print text
    print("Text Content:")
    text_content = soup.get_text()
    print(text_content[:1000])  # Print the first 1000 characters of the text content

    # Extract and print all links
    print("\nLinks:")
    links = soup.find_all('a')
    for idx, link in enumerate(links):
        href = link.get('href')
        text = link.get_text()
        print(f'Link {idx + 1}: Text: {text}, URL: {href}')

    # Extract and print all images
    print("\nImages:")
    images = soup.find_all('img')
    for idx, img in enumerate(images):
        src = img.get('src')
        alt = img.get('alt', 'No alt text')
        print(f'Image {idx + 1}: Source: {src}, Alt text: {alt}')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
