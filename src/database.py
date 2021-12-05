import pymongo
import config


class Database(object):

    def __init__(self):
        self.client = pymongo.MongoClient(config.MONGO_CONNECTION_STRING)
        db = self.client["post_database"]
        self.col = db["posts"]

    def save_post(self, post):
        self.col.insert_one(post)

    def save_posts(self, posts):
        for post in posts:
            if self.col.count_documents({'_id': post['_id']}) == 0:
                self.col.insert_one(post)
                print('Save post Title:' + post['Title'])

    def print_post(self):
        for x in self.col.find():
            print(x)
