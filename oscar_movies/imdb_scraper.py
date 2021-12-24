import requests
from bs4 import BeautifulSoup
import pandas as pd

#scrape data first page
url = "https://www.imdb.com/title/tt2382320/reviews?ref_=tt_urv"
req = requests.get(url)
txt = req.text
soup = BeautifulSoup(txt, features="html.parser")

container = soup.find_all("div", class_="review-container")
ratings = []
dates = []
reviews = []
for tag in container:
    rate = tag.find("span", class_="rating-other-user-rating")
    if rate == None:
        ratings.append('NA')
    else:
        ratings.append(int(rate.find("span").text))
    dates.append(tag.find("span", class_="review-date").text)
    reviews.append(tag.find("div", class_="text show-more__control").text)

#scrape until load more exists
load_more = soup.find("div", class_="load-more-data")
base_url = "https://www.imdb.com/" + load_more["data-ajaxurl"] + "?paginationKey="

while load_more:
    url = base_url + load_more["data-key"]
    req = requests.get(url)
    txt = req.text
    soup = BeautifulSoup(txt, features="html.parser")
    container = soup.find_all("div", class_="review-container")
    for tag in container:
        rate = tag.find("span", class_="rating-other-user-rating")
        if rate == None:
            ratings.append(-1)
        else:
            ratings.append(int(rate.find("span").text))
        dates.append(tag.find("span", class_="review-date").text)
        reviews.append(tag.find("div", class_="text show-more__control").text)
    load_more = soup.find("div", class_="load-more-data")

df = pd.DataFrame({"rating":ratings, "review date":dates, "review content":reviews})
df.to_csv('No_Time_To_die.csv')