import pymongo
import mars_scrape

#setup connection to mongo
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

#choose database
db = client.mars_info.mars_data

scrape_data = mars_scrape.scrape()

db.update({},scrape_data, upsert=True)


