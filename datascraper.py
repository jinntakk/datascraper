from bs4 import BeautifulSoup
import requests

#getting url page, requesting http from the page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

#finding, organizing, cleaning data headers
table = soup.find_all('table')[1]
table_header = table.find_all('th')
table_header_cleaned = [header.text.strip() for header in table_header]

#importing pandas dataframe and telling it each column is
#table_header_cleaned which is a list of column headers
import pandas as pd
dataframe = pd.DataFrame(columns = table_header_cleaned)

#finding column rows, labeling individual rows, cleaning them up
table_row = table.find_all('tr')
for row in table_row[1:]:
    row_data = row.find_all('td')
    table_row_cleaned = [data.text.strip() for data in row_data]
    #setting length of dataframe to how many rows are being scraped
    length = len(dataframe)
    #inputting scraped data into their respective row automagically
    dataframe.loc[length] = table_row_cleaned

#exporting to a csv file(excel)
dataframe.to_csv(r'C:\Users\MEMEMEMEME2\Documents\datascraper\Companies.csv', index = False)



