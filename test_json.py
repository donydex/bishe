import pandas
import numpy
import sys
import os

class calculate_grade_csv(object):
    def __init__(self):
        file_name = sys.argv[1]
        self.docker_file = "docker_output_{0}.csv".format(file_name)
        self.json_file = "json_data_{0}.csv".format(file_name)
        self.grade_file = "grade_data_{0}.csv".format(file_name)
        self.api_name = sys.argv[2]
        
    def calculate_json_grade(self):
        data = pandas.read_csv(self.json_file)
        data = data[data.api == self.api_name]
        print("data.api:{0} api_name:{1}".format(data.api, self.api_name))
        json_grade = numpy.mean(data["duration"])
        return json_grade
        
    def calculate_duration_grade(self):
        data = pandas.read_csv(self.json_file) 
        json_grade = data["duration"][0]
        return json_grade
        
    def main(self):
        print(self.calculate_json_grade())
        print(self.calculate_duration_grade())

if __name__ == "__main__":
    cal = calculate_grade_csv()
    cal.main()
