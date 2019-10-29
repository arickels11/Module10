"""CIS 189
Alex Rickels
Topic 1 Assignment 1 - driver"""

import class_definitions
# Driver
emp = class_definitions.Employee(lname='Rickels', fname='Alexandra', address='722 18th St', pnumber='867-5309',
                                 salaried=True, salary='$1,000,000', day=15, month=6, year=2015)


emp.set_first_name('Alex')
print(str(emp))
del emp
