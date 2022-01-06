# Are Best Picture award winning movies considered the best among the public?

## Table of contents
* [Project Description] (#project-description)
* [Libraries and packages] (#libraries-and-packages)
* [Method] (#method)
* [Sources] (#sources)

<a name="project-description"></a>
## Project Descritpion
With this project, we are trying to find if there are any difference between the Oscar jury and the public opinion about the best movie of the year. We will compare the Best Picture award winning movies and the best rated movies on IMDB to see if there is any discrepancy and run a sentiment analysis and use data visualization to gain insights about the reasons for this difference.

<a name="libraries-and-packages"></a>
## Libraries and packages
In order to run the code for this project, you will need to run the following command to install the necessary packages:
'''
python -m pip install -U pip
python -m pip install -U pandas beautifoulsoup4 requests matplotlib numpy nltk scikit-learn joblib spacy textblob seaborn wordcloud
'''

<a name="method"></a>
## Method
For this project, we have used the code in this way:
1. run imdb_scraper.py for every Best Picture award winning movies to get the ratings and the reviews from the users;
2. divide the above scraped databases in after award movies and before award movies;
3. use the Kaggle database and extract the award winning movies information;
4. run a sentiment analysis on the reviews;
5. visualize the findings and write report.

<a name="sources"></a>
## Sources
* Stefano L. (2020, January). IMDb movies extensive dataset, Version 2, Retrieved December 4, 2021 from https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb+movies. csv
* IMDB movies websites:
https://www.imdb.com/title/tt0099348/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0102926/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0105695/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0108052/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0109830/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0112573/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0116209/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0120338/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0138097/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0169547/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0172495/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0268978/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0299658/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0167260/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0405159/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0375679/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0407887/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0477348/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt1010048/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt0887912/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt1504320/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt1655442/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt1024648/reviews/?ref_=tt_ql_urv
https://www.imdb.com/title/tt2024544/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt2562232/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt1895587/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt4975722/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt5580390/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt6966692/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt6751668/reviews/?ref_=tt_ql_urv 
https://www.imdb.com/title/tt9770150/reviews/?ref_=tt_ql_urv
