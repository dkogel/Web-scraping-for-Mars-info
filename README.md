# Scraping the Web for information about Mars

The purpose of this project was to practice web scraping and storing the scraped data in a noSQL database. Data is collected using Splinter and BeautifulSoup to pull the most up to date information and images from mulitple websites dedicated to the planet Mars, and once collected it is uploaded to a MongoDB database named `mars_info` using Flask. That updated information is then rendered to a website from that database, again using Flask as well as Jinja2 templates. The website itself uses Boostrap for it's styling. 

https://www.google.com/url?sa=i&url=https%3A%2F%2Ftechcrunch.com%2F2019%2F06%2F18%2Fmongodb-gets-a-data-lake-new-security-features-and-more%2F&psig=AOvVaw0Yndav6JXl0nf8mJ4NJtTy&ust=1645583814123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNjZ2MqjkvYCFQAAAAAdAAAAABAD

To try out the website yourself:
(must have MongoDB, Flask, python, and splinter installed)

1. Clone this repository
2. Open MongoDB Compass
3. Create a new database called mars_info
4. Open a Git Bash or Terminal window
5. Type `python app.py` and hit `enter`
6. Copy and paste the URL that is provided in your Git Bash or Terminal window to a web browser address bar (preferrably Chrome)
7. Click on the `Update Data` button to run the web scraping route
8. Observe that new data is populated on the website (all of it is scraped again and updated, but not everything will change as some of the sources don't change frequently)

  
  ---  
  
Daniel Kogel  
dkogel123@gmail.com  
www.linkedin.com/in/daniel-kogel  
