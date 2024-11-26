# pip install requests beautifulsoup4

import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Create necessary directories
os.makedirs('magic', exist_ok=True)
os.makedirs('magic/images', exist_ok=True)

# URL to scrape
url = 'https://sutirthachakraborty.github.io/magic/'

# Get the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and save text content
text_content = soup.get_text(separator='\n', strip=True)
with open('magic/content.txt', 'w', encoding='utf-8') as f:
    f.write(text_content)

# Find and download all images
for img in soup.find_all('img'):
    # Get image source
    img_url = img.get('src')

    # If the image URL is relative, make it absolute
    if img_url and not img_url.startswith(('http://', 'https://')):
        img_url = urllib.parse.urljoin(url, img_url)

    if img_url:
        try:
            # Get image name from URL
            img_name = os.path.basename(urllib.parse.urlparse(img_url).path)
            if not img_name:
                continue

            # Download image
            img_response = requests.get(img_url)

            # Save image
            img_path = os.path.join('magic/images', img_name)
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded: {img_name}")

        except Exception as e:
            print(f"Error downloading {img_url}: {e}")

print("Scraping completed!")
