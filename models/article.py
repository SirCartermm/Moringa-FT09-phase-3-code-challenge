class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def author(self):
        return self.author

    def magazine(self):
        return self.magazine

class Article:
    # ...

    def author(self):
        return self.author

    def magazine(self):
        return self.magazine

