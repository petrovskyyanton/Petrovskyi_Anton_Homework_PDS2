import string


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def get_clean_string(self):
        for i in string.punctuation:
            if i in self.text:
                self.text = self.text.replace(i, '')
        return self.text

    def __is_punctuation(self):
        for i in self.text:
            if i in string.punctuation:
                return True
            else:
                return False


class TextLoader:
    def __init__(self, __text_processor, __clean_string):
        self.__text_processor = __text_processor
        a = input("Text")
        __text_processor = TextProcessor(a)
    def set_clean_text(self):
        __clean_string = f'{self.__text_processor.get_clean_string()}'

    @property
    def __clean_string(self):
        return __clean_string



