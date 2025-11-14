
class Issue:
    def __init__(self, author, date, summary, description):
        self.__date = date
        self.__summary = summary
        self.__author = author
        self.__description = description

    def __str__(self):
        return (f"--- Issue Report ---\n"
                f"Summary: {self.__summary}\n"
                f"Date: {self.__date}\n"
                f"Author: {self.__author}\n"
                f"Description: {self.__description}\n"
                f"--------------------")