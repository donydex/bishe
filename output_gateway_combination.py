import _thread as thread
import configparser
import sys
import time


class output_gateway_combination(object):
    def __init__(self):
        config = configparser.ConfigParser()  # 一定要做的
        config.read("config.ini")  # 读取路径
        data = config["service"]
        self.service_list = list(dict(data).values())

    def output_combation(self, arr):

        for i in range(len(arr)):
            print("gateway{0} = http://172.18.8.239:8888/gateway/gateway{0}".format(i + 1))

        for i in range(len(arr)):
            print("String gateway{0}();".format(i + 1))

        for i in range(len(arr)):
            print("@GetMapping(\"/gateway{0}\")\npublic String gateway{0}()\n{1}".format(i + 1, "{"))
            print("\tgatewayService.gateway{0}();\n\treturn \"ok\";\n{1}\n".format(i + 1, "}"))

        for i in range(len(arr)):
            ele = str(arr[i])
            print("@Override\npublic String gateway{0}() {1}".format(i + 1, "{"))
            for j in range(len(ele)):
                if int(ele[j]) == 0:
                    continue
                print("\tservice{0}Client.{1}();".format(int(ele[j]), self.service_list[j + 1]))
            print("\treturn \"ok\";\n}\n")

    def change_ele_to_point(self, ele, point, aim):
        for i in range(len(ele)):
            if ele[i] is point:
                ele[i] = aim
        return ele

    def list_to_str(self, ele):
        string_ = ""
        for i in ele:
            string_ += i
        return string_

    def change_ele(self, ele):
        num = 0
        ele = [i for i in ele]
        for i in ele:
            if i == "0" or "b" in i:
                # print(i)
                continue
            if ele.count(i) > 1:
                ele = self.change_ele_to_point(ele, i, "b{0}".format(num))
                num += 1
            else:
                ele = self.change_ele_to_point(ele, i, "a")
        return self.list_to_str(ele)

    def unique(self, arr):
        history_arr = []
        result = []
        for i in arr:
            change_ele = self.change_ele(i)
            if change_ele not in history_arr:
                history_arr.append(change_ele)
                result.append(i)
        return result

    def get_arr(self):
        self.num = 4
        self.service_count = 5
        output_arr = range(self.service_count)
        for i in range(self.num - 1):
            arr_point = []
            for j in range(self.service_count):
                for k in output_arr:
                    arr_point.append(str(j) + str(k))
            output_arr = arr_point
        result = self.unique(output_arr)
        return result

    def main(self):

        result = self.get_arr()
        result = self.unique(result)
        self.output_combation(result)
        # print(len(result))
        # print(result)


if __name__ == "__main__":
    out = output_gateway_combination()
    out.main()
