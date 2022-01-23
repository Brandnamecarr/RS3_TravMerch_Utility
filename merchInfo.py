import requests
from bs4 import BeautifulSoup

# class definition for merchGetter

class merchGetter():
    
    # constructor only takes URL as argument because that's all you need to scrape for the Merchant data.

    def __init__(self, url):
        self.url = url

    # main method for scraping table data from the url passed in. 

    def getTableData(self):
        # requests the data from the url & loads page's content.
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # intializing two empty lists, 1 to hold all the extracted data, the other to hold the data the program is looking for.
        tempHref = []
        extractedTitles = []

        # outer for loop finds all instances of the table class: wikitable align-center-1 align-center-4 based on Runewiki's HTML structure.
        for item in soup.find_all(attrs={'class':'wikitable align-center-1 align-center-4'}):

            # innter for loop finds all the <a href> tags within each of the classes identified above.
            for link in item.find_all('a'):

                #href = the title of the link identified by the for loop that finds the <a href> tag.
                href= link.get('title')

                #href object is added to the tempHref list.
                tempHref.append(href)
        

        # to extract the data needed from this list, get the 3:7 indices and place them in the extractedTitles list.
        for i in range(3,7):
            extractedTitles.append(tempHref[i])
        
        # clearing the temp list.
        tempHref.clear()

        # returning the relevant data.
        return extractedTitles
    
    # this method returns the extracted Runedate data from the table on the website.
    def getRunedate(self):
        # request the data from the url passed in.
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        tempHref = []

        for item in soup.find_all(attrs={'class':'wikitable align-center-1 align-center-4'}):

            for link in item.find_all('a'):

                href = link.get('title')

                tempHref.append(href)
        return tempHref[0:3]
        
    # this method takes in the data returned by getRunedate(), and reformats/cleans it to be more presentable for the user. 
    def cleanData(self, _list):
        # using split() to split the first element into a new list.
        x = _list[0].split(" ")
        
        # adding the elements from the initial list to list x, then clearing the other list.
        x.append(_list[1])

        _list.clear()

        # swapping the first 2 elements in the list to maintain American date/time structure.
        x[0], x[1] = x[1], x[0]

        # return new list
        return x

       