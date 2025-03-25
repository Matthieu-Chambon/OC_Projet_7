import csv
from pprint import pprint
import time


def set_combinaisons(actions, current_list, index):
    for i, action in enumerate(actions[index:]):  # O(n)
        new_list = current_list + [action]  # O(1)
        investment = {  # O(n)
            "combination": [action["name"] for action in new_list],
            "cost": sum(action["cost"] for action in new_list),
            "profit": sum((action["cost"]*action["profit"]) for action in new_list)
        }
        combinations.append(investment)  # O(1)
        if index < len(actions) - 1:  # O(1)
            set_combinaisons(actions, new_list, index + i + 1)  # O(2ⁿ)


start_time = time.time()

with open("Liste d'actions.csv", mode="r", encoding="utf-8") as file:  # O(1)
    reader = csv.reader(file, delimiter=",")
    data = list(reader)
    data = data[1:]

actions = [  # O(n)
    {"name": item[0], "cost": int(item[1]), "profit": float(item[2].strip('%')) / 100}
    for item in data
]

combinations = []

set_combinaisons(actions, [], 0)

combinations.sort(key=lambda x: x["profit"], reverse=True)

for combination in combinations:  # O(n)
    if combination["cost"] <= 500:  # O(1)
        print("\nCombinaison optimale :")
        pprint(combination)
        break

end_time = time.time()

print(f"\nTemps d'exécution : {end_time - start_time:.2f} secondes")
