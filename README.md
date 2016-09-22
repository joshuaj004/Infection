# Infection - Infection Project for KhanAcademy

This project contains the following items of interest:

1. The User Class
2. Tests for the User Class
3. A visualization tool for the test-run data (or the data of any code produced by the User Class)

## The User Class

The User Class implements the following methods:

1. \__init\__(self, name)

 Instantiate a new instance of the User Class:
 ```python
 charles = User("Charles")
 ```

2. getName(self)

 Returns the name of the specific User.
 ```python
 charles.getName() returns "Charles"
 ```

3. getCoaches(self)

 Returns the name of the User's coach, or an empty list if the User has no coach.
 ```python
 charles.getCoaches() returns "Sarah" or []
 ```

4. getTrainees(self)

 Returns a list of the User's trainees, or an empty list if the User has no trainees.
  ```python
 charles.getTrainees() returns "[April, Joe, Jeff]" or []
 ```

5. \__updateVersion(self, version=1)

  Private method. Changes the Version of the User, without infecting any of the User's trainees or coaches. Returns nothing.
  ```python
  user.__updateVersion(2)
  ```

6. getUsers()

  Static method. Returns a list of all the current instances of the User class, or empty list if there are no Users.
  ```python
  User.getUsers() returns "[Karen, Will, Jack, Wendy]" or []
  ```

7. addCoach(self, coach, auto=False)

  Adds a coach to a given User. Raises an exception if the User has a coach. Automatically associates the User as a trainee of the coach on success. Returns nothing.
  ```python
  charles.addCoach(sarah)
  ```

8. removeCoach(self, coach, auto=False)

  Removes a coach from a given User. Raises an exception if the User is not being coached by the given coach. Automatically disassociates the User from being a trainee of the coach on success. Returns nothing.
  ```python
  charles.removeCoach(sarah)
  ```

9. addTrainee(self, trainee, auto=False)

 Adds a trainee to a given User. Raises an exception if the User is already coaching this trainee. Automatically associates the User as a coach of the trainee on success. Returns nothing.
  ```python
  charles.addTrainee(april)
  ```

10. removeTrainee(self, trainee, auto=False)

 Removes a trainee from a given User. Raises an exception if the User is not coaching the given trainee. Automatically disassociates the User from being a coach of the trainee on success. Returns nothing.
  ```python
  charles.removeTrainee(april)
  ```

11. __createGroupings()

 Private, Static method. Groups the Users by their coaches and trainees. Returns nothing.
 ```python
  User.__createGroupings()
  ```
 
12. groupingsHelper(self)

 Private helper method for __createGroupings().

13. limitedInfection(number, infection=1)

 Static method. Given a number and version, tries to infect that number of Users (with a 20% margin, 80% - 120% of the given number). Guarentees that coaches and trainees will always have the same version. Returns nothing.
 ```python
  User.limitedInfection(58, 3)
  ```

14. fullInfection(self, infection=1)

 Given a User, will infect all coaches and trainees of that user with the given version. Returns nothing.
 ```python
  charles.fullInfection(5)
  ```

15. __listToString(someList)

  Private static helper method for generateJS().

16. generateJS()

 Static method that parses the list of Users into a JavaScript variable that can be intrepreted by the visualizer. Writes out to Visualization/data.js by default. Returns nothing.
  ```python
  User.generateJS()
  ```

17. \__str\__(self):
 Returns a string representation of the User.
  ```python
  print(charles)
  ```
 
 
