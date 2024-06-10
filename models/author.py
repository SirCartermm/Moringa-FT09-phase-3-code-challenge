class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError("Name must be a non-empty string")
        self._name = value 



class Author:
    # ...

    def articles(self):
        # Use SQLAlchemy's ORM to retrieve articles associated with the author
        return db.session.query(Article).join(Author).filter(Article.author_id == self.id).all()

    def magazines(self):
        # Use SQLAlchemy's ORM to retrieve magazines associated with the author
        return db.session.query(Magazine).join(Article).join(Author).filter(Article.author_id == self.id).all()
