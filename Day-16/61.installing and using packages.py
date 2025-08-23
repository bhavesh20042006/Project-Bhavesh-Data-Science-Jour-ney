from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["pikachu", "squirtle", "charmender"])
table.add_column("type", ["electric", "water", "fire"])
table.align = "l"  # Aligns the columns to the left
print(table)  # This will print the table with the added columns