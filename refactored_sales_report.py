"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

melons_by_salesperson = {}

log_file = open("sales-report.txt")  # opens and parses text file
for line in log_file:
    line = line.rstrip()  # strips trailing white space
    entries = line.split("|")  # makes a list by splitting string at each "|"
    salesperson = entries[0]
    # gets salesperson's name from first item in entries list
    melons = int(entries[2])
    # gets number of melons from third item in line in entries list

    if melons_by_salesperson.get(salesperson, 0) == 0:
        melons_by_salesperson[salesperson] = melons
    else:
        melons_by_salesperson[salesperson] += melons

for salesperson, melons in melons_by_salesperson.items():
    print "{} sold {} melons".format(salesperson, melons)

log_file.close()
