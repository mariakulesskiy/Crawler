import site_parser
import database


class CrawlWorker(object):

    def __init__(self):
        self._database = database.Database()

    def run(self):
        posts = site_parser.get_site_data()
        self._database.save_posts(posts)


