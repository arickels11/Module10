"""CIS 189
Alex Rickels
Topic 2 Assignment 1 - Driver"""

import customer_class

customer1 = customer_class.Customer(customer_id=12546, last_name='Peiffer', first_name='Brando',
                                    phone_number='319-310-0651', address='1316 E 10TH ST')
customer2 = customer_class.Customer(customer_id='abx', last_name='Robles', first_name='Antonio', phone_number='515-654-6753', address='657 DRURY LANE')

print(customer1.display())
print(customer2.display())

del customer1
del customer2
