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

    def addCoach(self, coach):
        if len(self.coaches > 0):
            raise Exception("You cannot at a coach to a user who already has a coach")
        else:
            self.coaches = coach

    def removeCoach(self, coach):
        if len(self.coaches < 1):
            raise Exception("This user has no coaches")
        elif coach not in self.coaches:
            raise Exception("This user is not coached by this coach")
        else:
            self.coaches = []

    def addTrainee(self, trainee):
        if trainee in self.trainees:
            raise Exception("This user is already coaching this trainee")
        else:
            self.trainees.append(trainee)

    def removeTrainee(self, trainee):
        if len(self.trainees < 1):
            raise Exception("This user has no trainess")
        elif trainee not in self.trainees:
            raise Exception("This user is not coaching this trainee")
        else:
            self.trainees.remove(trainee)
