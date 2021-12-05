import sched
import time
import config
import crawl_worker

s = sched.scheduler(time.time, time.sleep)
worker = crawl_worker.CrawlWorker()
wait_time = int(config.WAIT_TIME)


def do_crawl(sc):
    print("site crawling...")
    worker.run()
    s.enter(wait_time, 1, do_crawl, (sc,))


s.enter(0, 1, do_crawl, (s,))
s.run()
