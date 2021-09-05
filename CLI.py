from find_sentences import FindSentences


class CLI:

    def __init__(self):
        print("Loading the files and preparing the system...")
        self.find_sentence = FindSentences()

    def run(self):
        print("The system is ready. Enter your text:")
        sub_sentence = input()
        try:
            while sub_sentence is not None:
                try:
                    val = self.find_sentence.run(sub_sentence)
                    if val is not None:
                        for i in range(len(val)):
                            print('{}. {}. ({} {})'.format(i + 1, val[i].get_sentence(), val[i].get_path(),
                                                           val[i].get_num_lines()))
                    else:
                        print("could not find any matches")
                        continue
                    print(sub_sentence)
                    print("The system is ready. Enter your text:")
                    temp = input()
                    if temp == '#':
                        print("The system is ready. Enter your text:")
                        sub_sentence = input()
                    else:
                        sub_sentence =" "+temp
                # print("The system is ready. Enter your text:")
                # sub_sentence = input()
                except Exception as e:
                    return "error", e
        except Exception as e:
            return "error", e


cli = CLI()
cli.run()
