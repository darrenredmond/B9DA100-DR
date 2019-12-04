import glob

class SpellChecker(object):
    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        my_file = open(file_name)
        lines = my_file.readlines()
        my_file.close()
        return list(map(lambda x: x.strip().lower(), lines))

    def load_words(self, file_name):
        self.words = self.load_file(file_name)

    def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        return failed_words_in_sentences

    def check_word(self, word):
        return word.strip('.').lower() in self.words

    def check_words(self, sentence, index=0):
        words_to_check = sentence.split(' ')
        caret_position = 0
        failed_words = []
        for word in words_to_check:
            if not self.check_word(word):
                print('Word is misspelt ' + word + ' at line : ' + str(index+1) + ' pos ' + str(caret_position+1))
                failed_words.append({'word':word,'line':index+1,'pos':caret_position+1})
            # update the caret position to be the length of the word plus 1 for the split character.
            caret_position = caret_position + len(word) + 1
        return failed_words

    def check_directory(self, dir_string):
        files = glob.glob(dir_string)
        failed_files = {}
        for file in files:
            failed_files[file] = self.check_document(file)
        return failed_files

if __name__ == '__main__':
    spellChecker = SpellChecker()
    spellChecker.load_words('spell.words')
    print(len(spellChecker.words))
    # now check if the word zygotic is a word
    print(spellChecker.check_word('zygotic'))
    print(spellChecker.check_word('zogotic'))
    print(spellChecker.check_words('zygotic mistasdas elementary'))
    print(spellChecker.check_document('darren.txt'))

    import os
    os.chdir('R:/')
    spellChecker.check_directory('*.txt')
