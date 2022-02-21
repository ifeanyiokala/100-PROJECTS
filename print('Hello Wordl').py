#print('Hello Wordl')
import prettytable
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["PokeMon Name", "Type","Name"]
x.add_row(["Adelaide", 1295,123])
x.add_row(["Brisbane", 5905,123])
x.add_row(["Darwin", 112,123])
x.add_row(["Hobart", 1357,1234])
x.add_row(["Sydney", 2058,1234])
x.add_row(["Melbourne", 1566,678])
x.add_row(["Perth", 5386, 1554769,])

print(x)