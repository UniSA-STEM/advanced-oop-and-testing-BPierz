
class Entry:

    def __init__(self, date: str, issue: str, details: str, severity: int, treatment: str):
        self.__date = date
        self.__issue = issue
        self.__details = details

        if severity < 0 or severity > 3:
            raise ValueError

        self.__severity = severity
        self.__treatment = treatment

    def str_severity(self):
        if self.__severity == 0:
            return "Negligible"
        if self.__severity == 1:
            return "Mild"
        if self.__severity == 2:
            return ("Moderate")
        if self.__severity == 3:
            return ("Severe")

    @property
    def date(self):
        return self.__date
    @property
    def issue(self):
        return self.__issue
    @property
    def details(self):
        return self.__details
    @property
    def severity(self):
        return self.__severity
    @property
    def treatment(self):
        return self.__treatment


    def __str__(self):
        return (f"Date: {self.__date}\n"
         f"Issue: {self.__issue}\n"
         f"Details: {self.__details}\n"
         f"Severity: {self.str_severity()}\n"
         f"Treatment: {self.__treatment}")

    def __repr__(self):
        return (f"Date: {self.__date} | Issue: {self.__issue} | Severity: {self.str_severity()}\n")

