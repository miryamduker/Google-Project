class DataObject:

    def __init__(self, path, line, sentence):
        self.path = path
        self.num_line = line
        self.sentence = sentence

    def get_path(self):
        return self.path

    def get_num_lines(self):
        return self.num_line

    def get_sentence(self):
        return self.sentence

    def get_id(self):
        return self.id

    def __eq__(self, other):
        if self.path == other.path and self.num_line == other.num_line and self.sentence == other.sentence:
            return True
        return False

    def get_sentence(self):
        return self.sentence
