# Spec: https://docs.google.com/document/d/1NiKv-MjULOFyyc8f5w8R_EqvuPJ10wJVJgZhtTK9VKc
class User:
    """A simple User class for the infection scenario"""
    def __init__(self, name):#, coaches=[], trainees=[], version=0):
        self.name = name
        self.coaches = []#coaches
        self.trainees = []#trainees
        self.version = 0#version

    def getName(self):
        return self.name

    def getCoaches(self):
        return self.coaches[0]

    def getTrainees(self):
        return self.trainees

    def getVersion(self):
        return self.version

    def updateVersion(self, version=1):
        self.version = version

    def addCoach(self, coach, auto=False):
        if len(self.coaches) > 0:
            raise Exception("You cannot at a coach to a user who already has a coach")
        else:
            self.coaches = [coach]
            if not auto:
                coach.addTrainee(self, True)

    def removeCoach(self, coach, auto=False):
        if len(self.coaches) < 1:
            raise Exception("This user has no coaches")
        elif coach not in self.coaches:
            raise Exception("This user is not coached by this coach")
        else:
            self.coaches = []
            if not auto:
                coach.removeTrainee(self, True)

    def addTrainee(self, trainee, auto=False):
        if trainee in self.trainees:
            raise Exception("This user is already coaching this trainee")
        else:
            self.trainees.append(trainee)
            if not auto:
                trainee.addCoach(self, True)


    def removeTrainee(self, trainee, auto=False):
        if len(self.trainees) < 1:
            raise Exception("This user has no trainess")
        elif trainee not in self.trainees:
            raise Exception("This user is not coaching this trainee")
        else:
            self.trainees.remove(trainee)
            if not auto:
                trainee.removeCoach(self, True)

    def fullInfection(self, infection=1):
        processed = []
        unprocessed = set()
        # add self to unprocessed
        unprocessed.add(self)
        while len(unprocessed) != 0:
            current = unprocessed.pop()
            # Add coach to list
            if current.coaches not in processed:
                c = current.coaches
                if len(c) > 0:
                    unprocessed.add(c[0])
            # Add trainess to infection
            for trainee in current.trainees:
                if trainee not in processed:
                    unprocessed.add(trainee)
            current.updateVersion(infection)
            processed.append(current)



    def __str__(self):
        n = "Name: " + self.name
        c = " Coach: " + ', '.join([x.name for x in self.coaches])
        t = " Trainees: " + ', '.join([x.name for x in self.trainees])
        v = " Version: " + str(self.version)
        return n + c + t + v