
def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import time
    from webdriver_manager.chrome import  ChromeDriverManager
    import pandas as pd

    ## get mars news

    #set up splinter
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    
    
    # NASA Mars News
    nasa_url = "https://redplanetscience.com/"
    browser.visit(nasa_url)
    time.sleep(1)
    html= browser.html
    soup= bs(html, "html.parser")
    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()

    
    # JPL Mars Space Images - Featured Image
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    time.sleep(1)
    html = browser.html
    soup= bs(html, "html.parser")
    relative_img_url = soup.findAll('img')[1]['src']
    featured_img_url = f'{jpl_url}{relative_img_url}'
    browser.quit()         

   


    
    ## get mars facts   

    # set up splinter
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
        
        
    facts_url= 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)
    time.sleep(1)
    tables= pd.read_html(facts_url)
    tables_df= tables[0]
    browser.quit() 
    tables_df

    #clean and convert mars info table to HTML
   
    tables_df_final= tables_df.iloc[1: , 0:2]
    html_table= tables_df_final.to_html(index=False, header=False)


    ##astrogeology/hemispheres information scrape

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    base_url= 'https://marshemispheres.com/'
    cerberus_url = 'https://marshemispheres.com/cerberus.html'
    schiaparelli_url = 'https://marshemispheres.com/schiaparelli.html'
    syrtis_url ='https://marshemispheres.com/syrtis.html'
    valles_url = 'https://marshemispheres.com/valles.html'


    #cerberus
    browser.visit(cerberus_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    cerberus_img = soup.find('img', class_= 'wide-image')['src']
    cerberus_title = soup.find('h2', class_= 'title').get_text()
    cerberus_img_url= f'{base_url}{cerberus_img}'




    #schiaparelli
    browser.visit(schiaparelli_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    schiaparelli_img = soup.find('img', class_='wide-image')['src']
    schiaparelli_title = soup.find('h2', class_= 'title').get_text()
    schiaparelli_img_url = f'{base_url}{schiaparelli_img}'

    # syrtis
    browser.visit(syrtis_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    syrtis_img = soup.find('img', class_='wide-image')['src']
    syrtis_title = soup.find('h2', class_= 'title').get_text()
    syrtis_img_url = f'{base_url}{syrtis_img}'


    # valles
    browser.visit(valles_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    valles_img = soup.find('img', class_='wide-image')['src']
    valles_title = soup.find('h2', class_= 'title').get_text()
    valles_img_url = f'{base_url}{valles_img}'

    browser.quit()


    hemisphere_image_urls = {}

    hemisphere_image_urls["cerberus"] = {"title":cerberus_title,"img_url":cerberus_img_url}
    hemisphere_image_urls["schiaparelli"] = {"title":schiaparelli_title,"img_url":schiaparelli_img_url}
    hemisphere_image_urls["syrtis"] = {"title":syrtis_title,"img_url":syrtis_img_url}
    hemisphere_image_urls["valles"] = {"title":valles_title,"img_url":valles_img_url}

    return {"nasa_mars_news" : {"news_title": news_title, "news_summary": news_p},
            "jpl_featured_img" : featured_img_url,"mars_facts_table" : html_table, 
            "hemisphere_img_urls": hemisphere_image_urls}
    


















