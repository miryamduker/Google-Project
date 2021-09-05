import os
from data_object import DataObject


class ReadData:
    def __init__(self):
        self.data = dict()

    def ignore(self, sentence):
        return " ".join(sentence.split())

    def read_data(self, current_path):
        for subdir, dirs, files in os.walk(current_path):
            for filename in files:
                filepath = subdir + os.sep + filename
                if filepath.endswith(".txt"):
                    with open(filepath, encoding="utf8") as file:
                        my_counter = 0
                        for line in file:
                            line = line[:-1]
                            data = DataObject(os.path.split(filepath)[1].replace(".txt", ""), my_counter, line)
                            for word in line.split():
                                if word in self.data.keys() and self.data[word] is not None:
                                    self.data[word].append(data)
                                else:
                                    self.data[word] = [data]
                            my_counter += 1
        return self.data