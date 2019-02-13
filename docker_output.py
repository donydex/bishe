import _thread as thread
import os
import pandas
import sys
import time


class docker_output():
    def __init__(self):
        self.file_name = "docker_output_{0}.csv".format(sys.argv[1])
        self.end_time = int(sys.argv[2])

    def get_docker_data(self):
        # da = """1547452534
        # CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O             BLOCK I/O           PIDS
        # f8ec85fcf0a6        0.08%               780.2 MiB / 7.783 GiB   9.79%               0 B / 0 B           0 B / 8.19 kB       0
        # bd942a7713c4        0.07%               1.898 GiB / 7.783 GiB   24.38%              0 B / 0 B           52.6 MB / 19.8 MB   0
        # 1d50ee9276a2        0.06%               1.502 GiB / 7.783 GiB   19.30%              0 B / 0 B           217 MB / 34.2 MB    0
        # 180fb2fe4cd4        0.06%               1.564 GiB / 7.783 GiB   20.10%              0 B / 0 B           16 MB / 15.4 MB     0
        # 9207dae4f013        0.62%               232.7 MiB / 7.783 GiB   2.92%               147 MB / 78.3 MB    255 MB / 0 B        0"""
        # return da.split("\n")
        return os.popen("date +%s && docker stats --no-stream").read().split("\n")[:-1]

    def write(self, data):
        df = pandas.DataFrame(data=data)
        df.to_csv(self.file_name, index=False, mode="a", header=False)

    def analisys_docker_Data(self, docker_data):
        count = 0
        line = 0
        arr = []
        time_point = 0
        for data in docker_data:
            count = count + 1
            if count == 1:
                line += 1
                time_point = int(data)
                continue
            if count == 2:
                line += 1
                continue

            datas = data.split("        ")
            text = datas[2]
            while "  " in text:
                text = text.replace("  ", " ")
            arr.append([time_point, datas[0], datas[1][:-1], text.split(" ")[-1][:-1]])
        return arr

    def main(self):
        df = pandas.DataFrame(columns=["time", "docker", "cpu", "mem"])
        df.to_csv(self.file_name, index=False)
        start = int(time.time())
        while int(time.time()) - start < self.end_time:
            data = self.get_docker_data()
            thread.start_new_thread(self.write, (self.analisys_docker_Data(data),))
            time.sleep(0.01)


if __name__ == "__main__":
    docker = docker_output()
    docker.main()
