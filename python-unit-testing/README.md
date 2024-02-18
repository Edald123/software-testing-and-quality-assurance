# A01422929 Act A6.2
- PEP 8 – Style Guide for Python Code https://peps.python.org/
- Python JSON programming: https://pynative.com/python/json/
- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Flake 8: https://flake8.pycqa.org/en/latest/
- Python Static Analysis Tools: https://luminousmen.com/post/python-static-analysis-tools


## Req 1. 
The program shall be invoked from a
command line. The program shall receive two
files as parameters. The first file will contain
information in a JSON format about a catalogue
of prices of products. The second file will
contain a record for all sales in a company.
## Req 2. 
The program shall compute the total cost
for all sales included in the second JSON archive.
The results shall be print on a screen and on a
file named SalesResults.txt. The total cost
should include all items in the sale considering
the cost for every item in the first file.
The output must be human readable, so make it
easy to read for the user.
## Req 3. 
The program shall include the mechanism
to handle invalid data in the file. Errors should
be displayed in the console and the execution
must continue.
## Req 4. 
The name of the program shall be
computeSales.py
## Req 5. 
The minimum format to invoke the
program shall be as follows:
python computeSales.py priceCatalogue.json
salesRecord.json
## Req 6. 
The program shall manage files having
from hundreds of items to thousands of items.
## Req 7. 
The program should include at the end of
the execution the time elapsed for the
execution and calculus of the data. This number
shall be included in the results file and on the
screen.
## Req 8. 
Be compliant with PEP8.

## Additional Info
Remember to run **pylint** and **flake8** on the code.

To install:
```
pip install pylint
```

To use:
```
pylint compute_sales.py
```

To install flake8:
```
pip install flake8
```

To use:
```
flake8 compute_sales.py
```

## Execute script
To run script:
```
python compute_sales.py priceCatalogue.json salesRecord.json
```