class TextProcessor:
    def __init__(self):
        self._punctuation = '.,!?;:*'

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
    def __init__(self, __text_processor, __clean_string):
        self.__text_processor = __text_processor
        a = input("Text")
        __text_processor = TextProcessor(a)
    def set_clean_text(self):
        clean_string = self.__text_processor.get_clean_string()
        return clean_string

    @property
    def clean_string(self):
        return clean_string



