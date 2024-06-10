class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter