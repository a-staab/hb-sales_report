"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# Recommended refactor: store parallel lists as a dictionary whose key-value
# pairs take the form 'salesperson: melons_sold'

salespeople = []  # creates an empty list
melons_sold = []  # creates another empty list

f = open("sales-report.txt")  # opens and parses text file
for line in f:
    line = line.rstrip()  # strips trailing white space
    entries = line.split("|")  # makes a list by splitting string at each "|"
    salesperson = entries[0]
    # gets salesperson's name from first item in entries list
    melons = int(entries[2])
    # gets number of melons from third item in line in entries list

    # Checks the salespeople list created at beginning
    # if the salesperson's name isn't in it, it adds it to that list and adds
    # the number of melons they sold to the melons_sold list created at the
    # beginning too.  If the salesperson's name is already in the list, it
    # adds the number of melons indicated in the line to the number at the same
    # index in melons_sold as the index for the salesperson in the salespeople
    # list (parallel lists).

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints how many melons each salesperson sold by counting up to the total
# number of salespeople and using the count as the index to grab the
# salesperson and the number of melons they sold from the parallel lists
for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
