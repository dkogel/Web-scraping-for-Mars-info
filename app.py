from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape


#creating and instance of flask
app = Flask(__name__)


#establish mongo connection
mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_info")

#route for rendering
@app.route("/")
def home():

    mars_data = mongo.db.mars_data.find_one()

    return render_template("index.html", mars = mars_data)

#route for scraping
@app.route("/scrape")

def scrape():

    scrape_data = mars_scrape.scrape()

    mongo.db.mars_data.update({}, scrape_data, upsert= True)

    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)