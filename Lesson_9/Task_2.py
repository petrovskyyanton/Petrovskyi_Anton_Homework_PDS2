class TextProcessor:
    def __init__(self):
        self._punctuation = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

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
    def __init__(self, text_processor, clean_string=''):
        self.__text_processor = text_processor
        self.__clean_string = clean_string

    @property
    def text_processor(self):
        return self.__text_processor

    def set_clean_text(self, text):
        self.clean_string = self.text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        return self.__clean_string
        # f'This text is cleaned from signs of punctuations:\n{self.__clean_string}'

    @clean_string.setter
    def clean_string(self, text):
        self.__clean_string = self.text_processor.get_clean_string(text)


# class DataInterface:
#     def __init__(self, text_processor):
#         self._text_processor = text_processor
#
#     def process_texts(self, list_of_strings):
#         for i in list_of_strings:
#             print(i)


t = input('Text:')
q = TextProcessor()
r = TextLoader(q)
print(q.get_clean_string(t))
print(r.set_clean_text(t))
print(r.set_clean_text(t))
r.clean_string() # str object not callable

