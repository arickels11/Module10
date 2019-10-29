"""CIS 189
Alex Rickels
Topic 1 Assignment 1 - constructors"""

import datetime


class Employee:

    # Constructor
    def __init__(self, lname, fname, address, pnumber, salaried, salary, day, month, year):

        self.__last_name = lname
        self.__first_name = fname
        self.__address = address
        self.__pnumber = pnumber
        self.__sdate = datetime.datetime(year, month, day)

        if salaried is True:
            self.__salaried = 'Salaried Employee'
            self.__salary = salary + '/year'
        else:
            self.__salaried = 'Hourly Employee'
            self.__salary = salary + '/hour'

    def set_last_name(self, lname):
        self.__last_name = lname

    def set_first_name(self, fname):
        self.__first_name = fname

    def set_address(self, address):
        self.__address = address

    def set_pnumber(self, pnumber):
        self.__pnumber = pnumber

    def set_salaried(self, salaried):
        self.__salaried = salaried

    def set_salary(self, salary):
        self.__salary = salary

    def set_sdate(self, sdate):
        self.__sdate = sdate

    def display(self):
        return str(self.__first_name) + " " + str(self.__last_name) + '\n' + str(self.__address)\
                + '\n' + str(self.__salaried) + ": " + \
                str(self.__salary) + '\n' + "Start Date: " + str(self.__sdate)

    def __str__(self):
        return str(self.__first_name) + " " + str(self.__last_name) + '\n' + str(self.__address)\
                + '\n' + str(self.__salaried) + ": " + \
                str(self.__salary) + '\n' + "Start Date: " + str(self.__sdate)

    def __repr__(self):
        return str(self.__first_name) + " " + str(self.__last_name) + '\n' + str(self.__address)\
                + '\n' + str(self.__salaried) + ": " + \
                str(self.__salary) + '\n' + "Start Date: " + str(self.__sdate)
