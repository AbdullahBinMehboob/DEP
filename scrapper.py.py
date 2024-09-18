import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the website: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='card-body')

    data = []

    for article in articles:
        title_tag = article.find('h2')
        if title_tag is not None:  
            title = title_tag.get_text().strip()
            link_tag = article.find('a')
            if link_tag and 'href' in link_tag.attrs:  
                link = link_tag['href']
                data.append([title, f"https://realpython.com{link}"])

    for item in data:
        print(f"Title: {item[0]}")
        print(f"Link: {item[1]}\n")
    
    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])
        writer.writerows(data)
    print(f"Data successfully saved to {filename}")

if __name__ == "__main__":
    url = "https://realpython.com/tutorials/" 
    scraped_data = scrape_website(url)
    if scraped_data:
        save_to_csv(scraped_data, 'realpython_tutorials.csv')
