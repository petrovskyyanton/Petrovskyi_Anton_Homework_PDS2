class TextProcessor:
    def __init__(self):
        self._punctuation = """!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""

    def __is_punctuation(self, sign):
        return sign in self._punctuation

    def get_clean_string(self, text):
        clean_text = ''
        for sign in text:
            if self.__is_punctuation(sign):
                continue
            clean_text += sign
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print(f'This text is cleaned from signs of punctuations:')
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, text):
        self._text_loader.set_clean_string(text)
        list_of_strings = self._text_loader.clean_string.split(r'\n')
        for i in list_of_strings:
            return i


t = '''First,];<=>? line
Second.{}()[ line:
Third!-*+ line
End- of +#$%&example'''

q = TextProcessor()
r = TextLoader()
g = DataInterface()
print(g.process_texts(t))
