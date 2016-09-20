# Spec: https://docs.google.com/document/d/1NiKv-MjULOFyyc8f5w8R_EqvuPJ10wJVJgZhtTK9VKc
class User:
    """A simple User class for the infection scenario"""
    def __init__(self, coaches=[], trainees=[], version=0):
        self.coaches = coaches
        self.trainees = trainees
        self.version = version

    def getCoaches(self):
        return self.coaches

    def getTrainees(self):
        return self.trainees

    def getVersion(self):
        return self.version