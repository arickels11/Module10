"""CIS 189 Topic 3 Assignment
Alex Rickels"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_chars.issuperset(lname) and name_chars.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
