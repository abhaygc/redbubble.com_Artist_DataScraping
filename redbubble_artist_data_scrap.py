import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

#Place the excelsheet containing the URLs of profile to be scraped in the very same folder as the code
#Name the file as urls.xlsx
#Name the column containing the URLs as "RedBubble_Artist_URL"

datasheet = pd.read_excel('urls.xlsx') # Reading the excel file

#Declaring  different lists to store data
RedBubble_Artist_UrlList=[]
RedBubble_Artist_NameList=[]
RedBubble_Artist_DateJoinedList=[]
RedBubble_Artist_ShortBioList=[]
RedBubble_Follower_CountList=[]
RedBubble_Following_CountList=[]
RedBubble_Favorited_CountList=[]
RedBubble_FavoritesReceived_CountList=[]
RedBubble_Artist_Website_LinkList=[]
RedBubble_Artist_Facebook_LinkList=[]
RedBubble_Artist_Twitter_LinkList=[]
RedBubble_Artist_Instagram_LinkList=[]
RedBubble_Artist_Tumblr_LinkList=[]
RedBubble_Artist_Behance_LinkList=[]
RedBubble_Artist_Pinterest_LinkList=[]
RedBubble_Artist_DeviantArt_LinkList=[]
RedBubble_Artist_Dribble_LinkList=[]
RedBubble_Artist_Flickr_LinkList=[]
RedBubble_Artist_GooglePlus_LinkList=[]
RedBubble_Artist_BioList=[]
RedBubble_Portfolio_Feed_PublishedCountList=[]
RedBubble_Portfolio_PublishedCountList=[]
email_in_bioList=[]


for url in datasheet['RedBubble_Artist_URL']:
    page= requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    main=soup.find("div",{'class':'app-entries-artistProfile-components-ProfileInfo-ProfileInfo_profileInfo_2iu-Q'})
    bio_container=soup.find("div",{"class":"profile-bio"})
    count_ul = main.find('ul',{'class':'app-entries-artistProfile-components-ProfileLinks-ProfileLinks_activityLinks_2fp63'})
    social =  main.find('div',{'class':'app-entries-artistProfile-components-ProfileSocial-ProfileSocial_profileSocial_18YjL'})

    RedBubble_Artist_Name=''
    try:
        RedBubble_Artist_Name=main.find("a",{'class':'app-entries-artistProfile-components-ProfileInfo-ProfileInfo_userNameLink_PUWPn'}).text
    except:
        RedBubble_Artist_Name=''

    RedBubble_Artist_DateJoined=''
    try:
        RedBubble_Artist_DateJoined = bio_container.find('li').text.replace("Joined: ","")
    except:
        RedBubble_Artist_DateJoined=''

    RedBubble_Artist_ShortBio=''
    try:
        RedBubble_Artist_ShortBio = main.find('p',{'class':'app-entries-artistProfile-components-ProfileInfo-ProfileInfo_shortBioText_3nXbY'}).text
    except:
        RedBubble_Artist_ShortBio=''

    filled_details = count_ul.find_all('li',{'class':'app-entries-artistProfile-components-ProfileLinks-ProfileLinks_activityLink_2R3rr'})
    words_details=['Shop','Portfolio','followers','following','favorited','favorites received','journals']

    for details in filled_details:
        a=details.find('a')
        txt = a.text
        for word in words_details:
            if word in txt:

                if word == 'Shop':
                    RedBubble_Shop_Link = a['href']
                elif word == 'Portfolio':
                    RedBubble_Portfolio_Link = a['href']
                elif word=='followers':
                    RedBubble_Follower_Count = txt.replace(" "+word,'')
                elif word == 'following':
                    RedBubble_Following_Count=txt.replace(" "+word,'')
                elif word == 'favorited':
                    RedBubble_Favorited_Count=txt.replace(" "+word,'')
                elif word == 'favorites received':
                    RedBubble_FavoritesReceived_Count=txt.replace(" "+word,'')
                else:
                    RedBubble_Journal_Count = txt.replace(" "+word,'')
                break


    RedBubble_Artist_Website_Link = ''
    try:
        RedBubble_Artist_Website_Link = social.find('a',{'title':'Personal site'})['href']
    except:
        RedBubble_Artist_Website_Link = ''

    RedBubble_Artist_Facebook_Link = ''
    try:
        RedBubble_Artist_Facebook_Link = social.find('a',{'title':'Facebook'})['href']
    except:
        RedBubble_Artist_Facebook_Link = ''

    RedBubble_Artist_Twitter_Link = ''
    try:
        RedBubble_Artist_Twitter_Link = social.find('a',{'title':'Twitter'})['href']
    except:
        RedBubble_Artist_Twitter_Link = ''

    RedBubble_Artist_Instagram_Link = ''
    try:
        RedBubble_Artist_Instagram_Link = social.find('a',{'title':'Instagram'})['href']
    except:
        RedBubble_Artist_Instagram_Link = ''

    RedBubble_Artist_Tumblr_Link=''
    try:
        RedBubble_Artist_Tumblr_Link = social.find('a',{'title':'Tumblr'})['href']
    except:
        RedBubble_Artist_Tumblr_Link=''


    RedBubble_Artist_Behance_Link = ''
    try:
        RedBubble_Artist_Behance_Link = social.find('a',{'title':'Behance'})['href']
    except:
        RedBubble_Artist_Behance_Link = ''


    RedBubble_Artist_Pinterest_Link=''
    try:
        RedBubble_Artist_Pinterest_Link= social.find('a',{'title':'Pinterest'})['href']
    except:
        RedBubble_Artist_Pinterest_Link=''

    RedBubble_Artist_DeviantArt_Link=''
    try:
        RedBubble_Artist_DeviantArt_Link=''
    except:
        RedBubble_Artist_DeviantArt_Link=''

    RedBubble_Artist_Dribble_Link=''
    try:
        RedBubble_Artist_Dribble_Link=social.find('a',{'title':'Dribbble'})['href']
    except:
        RedBubble_Artist_Dribble_Link=''

    RedBubble_Artist_Flickr_Link=''
    try:
        RedBubble_Artist_Flickr_Link=''
    except:
        RedBubble_Artist_Flickr_Link=''


    RedBubble_Artist_GooglePlus_Link=''
    try:
        RedBubble_Artist_GooglePlus_Link=''
    except:
        RedBubble_Artist_GooglePlus_Link=''

    RedBubble_Artist_Bio = ''
    try:

        RedBubble_Artist_Bio_list = bio_container.find('span',{'title':'Your Bio'}).find_all('p')
        for i in RedBubble_Artist_Bio_list:
            RedBubble_Artist_Bio = RedBubble_Artist_Bio + " " + i.text
    except:
        RedBubble_Artist_Bio = ''


    email_in_bio=''
    email_in_bio_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', RedBubble_Artist_Bio )

    try:
        email_in_bio=email_in_bio_match.group(0)
    except:
        email_in_bio=''


    purl=RedBubble_Portfolio_Link+"/recent"
    ppage= requests.get(purl)

    psoup = BeautifulSoup(ppage.text,'html.parser')
    feed_container = psoup.find('div',{'class':'portfolio-grid'})

    RedBubble_Portfolio_Feed_PublishedCount = ''
    try:
        RedBubble_Portfolio_Feed_PublishedCount = len(feed_container.find_all('a'))
    except:
        RedBubble_Portfolio_Feed_PublishedCount = ''

    try:
        pagination = psoup.find('div',{'class':'rb-pagination'})
        if pagination is not None:
            chk_pagination = True
        else:
            chk_pagination = False
    except:
        pagination = None
        chk_pagination = False


    RedBubble_Portfolio_PublishedCount =''
    if chk_pagination ==  True:
        try:
            page_explain = pagination.find('span',{'class':'page-explain'}).text
            RedBubble_Portfolio_PublishedCount = page_explain[page_explain.rfind('f')+2:]

        except:
           RedBubble_Portfolio_PublishedCount = RedBubble_Portfolio_Feed_PublishedCount
    else:
        RedBubble_Portfolio_PublishedCount = RedBubble_Portfolio_Feed_PublishedCount

    RedBubble_Artist_UrlList.append(url)
    RedBubble_Artist_NameList.append(RedBubble_Artist_Name)
    RedBubble_Artist_DateJoinedList.append(RedBubble_Artist_DateJoined)
    RedBubble_Artist_ShortBioList.append(RedBubble_Artist_ShortBio)
    RedBubble_Follower_CountList.append(RedBubble_Follower_Count)
    RedBubble_Following_CountList.append(RedBubble_Following_Count)
    RedBubble_Favorited_CountList.append(RedBubble_Favorited_Count)
    RedBubble_FavoritesReceived_CountList.append(RedBubble_FavoritesReceived_Count)
    RedBubble_Artist_Website_LinkList.append(RedBubble_Artist_Website_Link)
    RedBubble_Artist_Facebook_LinkList.append(RedBubble_Artist_Facebook_Link)
    RedBubble_Artist_Twitter_LinkList.append(RedBubble_Artist_Twitter_Link)
    RedBubble_Artist_Instagram_LinkList.append(RedBubble_Artist_Instagram_Link)
    RedBubble_Artist_Tumblr_LinkList.append(RedBubble_Artist_Tumblr_Link)
    RedBubble_Artist_Behance_LinkList.append(RedBubble_Artist_Behance_Link)
    RedBubble_Artist_Pinterest_LinkList.append(RedBubble_Artist_Pinterest_Link)
    RedBubble_Artist_DeviantArt_LinkList.append(RedBubble_Artist_DeviantArt_Link)
    RedBubble_Artist_Dribble_LinkList.append(RedBubble_Artist_Dribble_Link)
    RedBubble_Artist_Flickr_LinkList.append(RedBubble_Artist_Flickr_Link)
    RedBubble_Artist_GooglePlus_LinkList.append(RedBubble_Artist_GooglePlus_Link)
    RedBubble_Artist_BioList.append(RedBubble_Artist_Bio)
    RedBubble_Portfolio_Feed_PublishedCountList.append(RedBubble_Portfolio_Feed_PublishedCount)
    RedBubble_Portfolio_PublishedCountList.append(RedBubble_Portfolio_PublishedCount)
    email_in_bioList.append(email_in_bio)
    #time.sleep(1)




cols=['RedBubble_Artist_UrlList','RedBubble_Artist_NameList','RedBubble_Artist_DateJoinedList','RedBubble_Artist_ShortBioList','RedBubble_Follower_CountList','RedBubble_Following_CountList',
      'RedBubble_Favorited_CountList','RedBubble_FavoritesReceived_CountList','RedBubble_Artist_Website_LinkList','RedBubble_Artist_Facebook_LinkList',
      'RedBubble_Artist_Twitter_LinkList','RedBubble_Artist_Instagram_LinkList','RedBubble_Artist_Tumblr_LinkList','RedBubble_Artist_Behance_LinkList',
      'RedBubble_Artist_Pinterest_LinkList','RedBubble_Artist_DeviantArt_LinkList','RedBubble_Artist_Dribble_LinkList','RedBubble_Artist_Flickr_LinkList',
      'RedBubble_Artist_GooglePlus_LinkList','RedBubble_Artist_BioList','RedBubble_Portfolio_Feed_PublishedCountList','RedBubble_Portfolio_PublishedCountList','email_in_bioList']


data =pd.DataFrame(np.column_stack([RedBubble_Artist_UrlList,RedBubble_Artist_NameList,RedBubble_Artist_DateJoinedList,RedBubble_Artist_ShortBioList,RedBubble_Follower_CountList,RedBubble_Following_CountList,
RedBubble_Favorited_CountList,RedBubble_FavoritesReceived_CountList,RedBubble_Artist_Website_LinkList,RedBubble_Artist_Facebook_LinkList,
RedBubble_Artist_Twitter_LinkList,RedBubble_Artist_Instagram_LinkList,RedBubble_Artist_Tumblr_LinkList,RedBubble_Artist_Behance_LinkList,
RedBubble_Artist_Pinterest_LinkList,RedBubble_Artist_DeviantArt_LinkList,RedBubble_Artist_Dribble_LinkList,RedBubble_Artist_Flickr_LinkList,
RedBubble_Artist_GooglePlus_LinkList,RedBubble_Artist_BioList,RedBubble_Portfolio_Feed_PublishedCountList,RedBubble_Portfolio_PublishedCountList,email_in_bioList]),columns=cols)

data.to_excel('data_scraped.xlsx',header=True,index=False)

print("Data exported to data_scraped.xlsx ")

