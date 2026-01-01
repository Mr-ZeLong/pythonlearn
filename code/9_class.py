class Document():
    
    WELCOME_STR = 'Welcome! The context for this book is {}.'
    
    def __init__(self, title, author, context):
        print('init function called')
        self.__title = title
        self.__author = author
        self.__context = context
    
    # 类函数：主要用于创建不同的对象
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context(self):
        return self.__context
    
    def set_context(self, context):
        self.__context = context
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author
    
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

doc = Document("my book", "me", "this is my book")
print(doc.get_title())
print(doc.get_author())
print(doc.get_context())

print(Document.get_welcome("this book"))


# 抽象类（接口）
from abc import ABCMeta, abstractmethod

class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass

class Document(Entity):
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

document = Document()
document.set_title('Harry Potter')
print(document.get_title())
entity = Entity() # 不能实例化抽象类，会报错 TypeError: Can't instantiate abstract class

