from prettytable import PrettyTable

table = PrettyTable()
# Way 1:
# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirle", "Water"])
# table.add_row(["Charmander", "Fire"])

# Way 2:

table.add_column("Pokemon", ["Pikachu", "Squirle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = 'l'
print(table)