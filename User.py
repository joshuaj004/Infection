# Spec: https://docs.google.com/document/d/1NiKv-MjULOFyyc8f5w8R_EqvuPJ10wJVJgZhtTK9VKc
class User:
    users = []
    groups = []

    """A simple User class for the infection scenario"""
    def __init__(self, name):
        self.name = name
        self.coaches = []
        self.trainees = []
        self.version = 0
        User.users.append(self)

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

    @staticmethod
    def getUsers():
        return User.users

    def addCoach(self, coach, auto=False):
        if len(self.coaches) > 0:
            raise Exception("You cannot add a coach to a user who already has a coach")
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
            raise Exception("This user has no trainees")
        elif trainee not in self.trainees:
            raise Exception("This user is not coaching this trainee")
        else:
            self.trainees.remove(trainee)
            if not auto:
                trainee.removeCoach(self, True)

    def fullInfection(self, infection=1):
        infectees = self.groupings_helper()
        for infectee in infectees:
            infectee.updateVersion(infection)


    @staticmethod
    def create_groupings():
        users = User.users[:]
        groupings = []
        while len(users) > 0:
            base = users[0]
            base_groupings = base.groupings_helper()
            groupings.append(base_groupings)
            for x in base_groupings:
                if x in users:
                    users.remove(x)
        User.groups = groupings


    def groupings_helper(self):
        processed = []
        unprocessed = set()
        unprocessed.add(self)
        while len(unprocessed) != 0:
            current = unprocessed.pop()
            if current.coaches not in processed:
                c = current.coaches
                if len(c) > 0:
                    unprocessed.add(c[0])
            for trainee in current.trainees:
                if trainee not in processed:
                    unprocessed.add(trainee)
            processed.append(current)
        return set(processed)

    @staticmethod
    def limited_infection(number, infection=1):
        # This will use a 20% margin for the term close in
        # "infect close to a given number of users"
        low = int(number * 0.8)
        # Plus 1 because python int rounds to the lower int
        hi = int(number * 1.2 + 1)
        User.create_groupings()
        users = sorted(User.groups[:], key=len, reverse=True)
        usersLength = len(users)
        current_val = 0
        index = 0
        infection_list = []
        while current_val < hi and (index + 1) < usersLength:
            new_len = current_val + len(users[index])
            if current_val > number and abs(current_val - number) < abs(new_len - number):
                break
            elif new_len < hi:
                infection_list.extend(users[index])
                current_val += len(users[index])
            index += 1
        for user in infection_list:
            if user.version != infection:
                user.updateVersion(infection)

    @staticmethod
    def generateJS():
        baseStr = "var users = [\n"
        for x in range(len(User.users)):
            user = User.users[x]
            userName = "\"name\": \"{0}\", ".format(user.name)
            userCoaches = "\"coaches\": {0}, ".format(User.listToString(user.coaches))
            userTrainees = "\"trainees\": {0}, ".format(User.listToString(user.trainees))
            userVersion = "\"version\": {0}".format(user.version)
            tempStr = "    {" + userName + userCoaches + userTrainees + userVersion + "}"#"{\"name\": {0}, \"coaches\": {1}, \"trainees\" {2}, \"version\": {3} }".format(user.name, User.listToString(user.coaches), User.listToString(user.trainees), user.version)
            if x != (len(User.users) - 1):
                tempStr += ','
            baseStr += tempStr + "\n"
        baseStr += '];'
        f = open("Visualization/data.js", 'w')
        print(baseStr, file=f)

    @staticmethod
    def listToString(someList):
        if someList == []:
            return []
        else:
            tempList = []
            for name in someList:
                tempList.append(str(name.name))
            return tempList

    def __str__(self):
        n = "Name: " + self.name
        c = " Coach: " + ', '.join([x.name for x in self.coaches])
        t = " Trainees: " + ', '.join([x.name for x in self.trainees])
        v = " Version: " + str(self.version)
        return n + c + t + v