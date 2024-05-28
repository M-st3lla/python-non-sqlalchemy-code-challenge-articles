class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return list({author for author in authors if authors.count(author) > 2})

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
article_2 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")
article_3 = Article(author_2, magazine_2, "Carrara Marble is so 2020")

# Test methods
print(author_1.articles())  
print(author_1.magazines())  
print(author_1.topic_areas())  
print(magazine_1.articles()) 
print(magazine_1.contributors())  
print(magazine_1.article_titles())  
print(magazine_1.contributing_authors()) 
