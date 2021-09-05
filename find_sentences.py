import difflib
import string
from _ast import operator

from read_data import ReadData
import re


class FindSentences:
    def __init__(self):
        self.r_data = ReadData()
        self.word_data = self.r_data.read_data('2021-archive')
        self.had_mistake = False

    def get_sentences_by_word(self, word):
        words_data = self.word_data  .get(word)
        if words_data is None:
            self.had_mistake = True
            temp = self.known_words(self.find_errors(word))
            closet_word = self.calculate_score(temp, word)
            words_data = self.word_data.get(closet_word)
            return words_data, closet_word
        return words_data, word

    def ignore_extra_chars(self, sentence):
        sentence = " ".join(sentence.split())
        sentence = re.sub(r'[^\w\s]', '', sentence)
        return sentence

    def run(self, sentence):
        try:
            sentence = self.ignore_extra_chars(sentence)
            return_data = []
            relevant_sentences = []
            relevant_sentences = self.get_sentences_by_word(sentence.split()[0])[0]
            my_string = self.get_sentences_by_word(sentence.split()[0])[1]
            for i in range(1, len(sentence.split())):  # iterating on words to detect corrections
                words_data, current_sentence = self.get_sentences_by_word(sentence.split()[i])[0], \
                                               self.get_sentences_by_word(sentence.split()[i])[1]
                try:
                    result = list(filter(lambda x: (x in words_data and my_string in x.get_sentence()), relevant_sentences))
                except Exception as e:
                    print("error", e)
                relevant_sentences = result
                my_string += " " + current_sentence
            return relevant_sentences[:5]
        except Exception as e:
            print( "error", e)
            return
            pass

    def find_errors(self, word):
        alphabet_string = string.ascii_lowercase
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in alphabet_string]
        inserts = [L + c + R for L, R in splits for c in alphabet_string]

        return set(deletes + transposes + replaces + inserts)

    def known_words(self, words):
        return set(w for w in words if w in self.word_data.keys())

    def calculate_score(self, word_set, input_word):
        word = ""
        score = 0
        closests = {}
        for value in word_set:
            s = difflib.SequenceMatcher(None, input_word, value, autojunk=False)
            for tag, i1, i2, j1, j2 in s.get_opcodes():
                if tag == 'replace':
                    if i1 > 4:
                        score = len(input_word) * 2 - 1
                    else:
                        score = len(input_word) * 2 - 5 - i1
                if tag == 'delete' or tag == "insert":
                    if i1 > 4:
                        score = len(input_word) * 2 - 2
                    else:
                        score = len(input_word) * 2 - 10 - i1 * 2

            closests[score] = value
            score = 0
        max_score = max(closests.keys())
        return closests[max_score]
