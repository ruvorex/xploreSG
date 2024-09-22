from datetime import datetime, time, date
from time import time

class Enquiry:
    def __init__(self, name, email, purpose, query):
        self.name = name
        self.email = email
        self.purpose = purpose
        self.query = query
        self.day = datetime.today()
        self.solveddate = None
        self.status = 'Not resolved'
        self.id = time() * 9000

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setPurpose(self, purpose):
        self.purpose = purpose

    def setQuery(self, query):
        self.query = query

    def setStatus(self, status):
        if status != 'Not resolved':
            self.solveddate = datetime.date.today()
            self.status = 'Resolved'

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPurpose(self):
        return self.purpose

    def getStatus(self):
        return self.status

    def getId(self):
        return self.id