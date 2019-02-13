import pandas
import numpy
import sys


class calculate_grade_csv(object):
    def __init__(self):
        file_name = sys.argv[1]
        self.docker_file = "docker_output_{0}.csv".format(file_name)
        self.json_file = "json_data_{0}.csv".format(file_name)
        self.api_name = sys.argv[2]

    def calculate_docker_grade(self):
        data = pandas.read_csv(self.docker_file)
        cpu_grade = numpy.mean(data["cpu"])
        memory_grade = numpy.mean(data["mem"])
        return cpu_grade + memory_grade

    def calculate_json_grade(self):
        data = pandas.read_csv(self.json_file)
        data = data[data.api == self.api_name]
        json_grade = numpy.mean(data["duration"])
        return json_grade

    def main(self):
        print(self.calculate_docker_grade())
        print(self.calculate_json_grade())
        return self.calculate_docker_grade(), self.calculate_json_grade()


if __name__ == "__main__":
    cal = calculate_grade_csv()
    cal.main()
