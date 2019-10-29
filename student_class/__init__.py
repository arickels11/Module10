"""CIS 189 Topic 3 Assignment
Alex Rickels"""


class Student:
    """Student class"""
    def __init__(self, lname: object, fname: object, major: object, gpa: object = 0.0) -> object:
        """

        :rtype: object
        """
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
