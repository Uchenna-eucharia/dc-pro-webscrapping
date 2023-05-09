import requests
from bs4 import BeautifulSoup 
import json
import pandas as pd

baseurl = "https://www.planitplus.net"

headers = {
      'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

r = requests.get("https://www.planitplus.net/CareerAreas/")

soup =  BeautifulSoup(r.content, 'lxml')

profession = soup.find_all('div', class_='career-area' )


professions = []

for item in profession: 
    for link in item.find_all('a', href=True):
        professions.append(baseurl + link['href'])


# testlink = 'https://www.planitplus.net/CareerAreas/View/1'
for link in professions:
    r = requests.get(link,headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')

    career = soup.find('div',class_='col-3-4').text.strip()
   
    try:
         job =  soup.find('div', class_='job-block-menu third-top').text.strip()
    except:
        job = 'no job'
    occupation = {
        'career': career,
        'job' : job
    }
    professions.append(occupation)
    print('saving:' , occupation['job'])
    

df = pd.Dataframe(professions)
print(df.head(27))

with open('occupationps.json', 'w', encoding='latin-1') as f:
    json.dump(professions, f, indent=8, ensure_ascii=False)
print("Created Json File")

# req = requests.get(URL).text

# soup = BeautifulSoup(req, 'lxml')


# print(soup)
# career = soup.find('a')
# print(career)
# profession = soup.find('a', class_='career-areas-btn')
# professions = profession.text
# print(profession)





# .ui-accordion-content-active .third-top a

# with open('planit.html', 'r' ) as html_file:
#     soup = soup = BeautifulSoup(html_file, 'lxml')  

# category = soup.find('a', class_='career-areas-btn')
# # print(category)

# headline = category.text
# print(headline)
   

