# A01422929 Act A6.2
- Unit Test Python Framework: https://docs.python.org/3/library/unittest.html
- PEP 8 – Style Guide for Python Code https://peps.python.org/
- Python JSON programming: https://pynative.com/python/json/
- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Flake 8: https://flake8.pycqa.org/en/latest/
- Python Static Analysis Tools: https://luminousmen.com/post/python-static-analysis-tools


## Req 1. 
Implement a set of classes in Python that
implements two abstractions:
1. Hotel
2. Reservation
3. Customers
## Req 2. 
Implement a set of methods to handle the
next persistent behaviors (stored in files):
1. Hotels
    - Create Hotel
    - Delete Hotel
    - Display Hotel information
    - Modify Hotel Information
    - Reserve a Room
    - Cancel a Reservation
2. Customer
    - Create Customer
    - Delete a Customer
    - Display Customer Information
    - Modify Customer Information
3. Reservation
    - Create a Reservation (Customer,
    Hotel)
    - Cancel a Reservation
    - You are free to decide the attributes within each class that enable the required behavior.
## Req 3. 
Implement unit test cases to exercise the
methods in each class. Use the unittest module in
Python.
## Req 4. 
The code coverage for all unittests should
accumulate at least 85% of line coverage.
## Req 5. 
The program shall include the mechanism
to handle invalid data in the file. Errors should be
displayed in the console and the execution must
continue.
## Req 6. 
Be compliant with PEP8.
## Req 7. 
The source code must show no warnings
using Fleak and PyLint.

## Additional Info
Remember to run **pylint** and **flake8** on the code.

To install:
```
pip install pylint
```

To use:
```
pylint abstractions.py
```

To install flake8:
```
pip install flake8
```

To use:
```
flake8 abstractions.py
```

To install coverage:
```
pip install coverage
```

To use:
```
coverage run -m unittest tests.py
coverage report
```

## Execute script
