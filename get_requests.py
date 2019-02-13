import _thread as thread
import configparser
import sys
import time
from requests import get


class get_requests(object):
    def __init__(self, api_url, end_time, epoch):
        config = configparser.ConfigParser()  # 一定要做的
        config.read("config.ini")  # 读取路径
        data = config["api"]
        self.api_url = dict(data)[api_url]
        self.end_time = int(end_time)
        self.epoch = int(epoch)

    def get_function(self):
        get(self.api_url)

    def main(self):
        for i in range(self.epoch):
            thread.start_new_thread(self.get_function, ())
        time.sleep(self.end_time)


if __name__ == "__main__":
    get_re = get_requests(sys.argv[1], sys.argv[2], sys.argv[3])
    get_re.main()
