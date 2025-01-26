class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters.")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        
        Article.all.append(self)
        author._articles_list.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ValueError("Title is immutable. Cannot change it.")

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid name")
        self._name = name
        self._articles_list = []

    @property
    def name(self):
        return self._name

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def articles(self):
        return self._articles_list

    def magazines(self):
        return list(set([article.magazine for article in self._articles_list]))

    def topic_areas(self):
        if not self._articles_list:
            return None
        return list(set([article.magazine.category for article in self._articles_list]))

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = new_category

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        contributing_authors = [
            author for author in self.contributors()
            if len([a for a in self._articles if a.author == author]) > 2
        ]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
