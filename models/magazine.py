import dbm
from sqlite3 import dbapi2

from database.setup import Article, Author


class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError("Category must be a non-empty string")
        self._category = value 


class Magazine:
    # ...

    def articles(self):
        # Use SQLAlchemy's ORM to retrieve articles associated with the magazine
        return dbm.session.query(Article).join(Magazine).filter(Article.magazine_id == self.id).all()

    def contributors(self):
        # Use SQLAlchemy's ORM to retrieve authors associated with the magazine
        return dbapi2.session.query(Author).join(Article).join(Magazine).filter(Article.magazine_id == self.id).all()

    def article_titles(self):
        # Use SQLAlchemy's ORM to retrieve article titles associated with the magazine
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Use SQLAlchemy's ORM to retrieve authors who have written more than 2 articles for the magazine
        authors = {}
        for article in self.articles():
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]