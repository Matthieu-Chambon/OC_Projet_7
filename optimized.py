import csv
from pprint import pprint
import time


# Programmation dynamique
def get_dynamic_programming(items, weight, step):
    dp = [
        [0 for _ in range(0, weight+step, step)]
        for _ in range(len(items)+1)
    ]  # O(n*w)

    pourcentage = 0
    for i, item in enumerate(items, start=1):  # O(n)

        if round(i*100/len(items)) > pourcentage:  # O(1)
            pourcentage = round(i*100/len(items))
            print(f"Avancement : {pourcentage}%")

        for w in range(step, weight+step, step):  # O(n)
            if item["cost"] <= w:  # O(1)
                dp[i][round(w/step)] = max(
                    dp[i-1][round(w/step)],
                    item["profit"] + dp[i-1][round(w-item["cost"]/step)]
                )  # O(1)
            else:
                dp[i][round(w/step)] = dp[i-1][round(w/step)]  # O(1)
    return dp


def get_optimal_combination(dp, items, w, step):
    optimal_combination = []

    for i in range(1, len(dp)):  # O(n)
        if dp[-i][round(w/step)] != dp[-i-1][round(w/step)]:  # O(1)
            optimal_combination.append(items[-i])  # O(1)
            w -= items[-i]["cost"]  # O(1)
    return optimal_combination


start_time = time.time()

# file_name = "Liste d'actions.csv"
file_name = "Dataset 1.csv"
with open(file_name, mode="r", encoding="utf-8") as file:  # O(1)
    reader = csv.reader(file, delimiter=",")
    data = list(reader)
    data = data[1:]

actions = [  # O(n)
    {
        "name": item[0],
        "cost": int(float(item[1]) * 100),
        "profit": round(float(item[2].strip('%')) * float(item[1]), 4)}
    for item in data
]

for action in actions[:]:  # O(n)
    if action["cost"] <= 0 or action["profit"] <= 0:  # O(1)
        actions.remove(action)  # O(1)

budget = 50000
step = 1

dp = get_dynamic_programming(actions, budget, step)  # O(n)
optimal_combination = get_optimal_combination(dp, actions, budget, step)  # O(n)

print("\nCombination optimale :")
pprint([action["name"] for action in optimal_combination])
print("Coût total :", round(sum(action["cost"] for action in optimal_combination)/100, 2))
print("Profit total :", round(sum(action["profit"] for action in optimal_combination)/100, 2))

end_time = time.time()

print(f"\nTemps d'exécution : {end_time - start_time:.2f} secondes\n")
