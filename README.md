# 🚀 Projet 7 - Résolvez des problèmes en utilisant des algorithmes en Python

## 📝 Description  
Ce projet repose sur le **problème du sac à dos** et vise à optimiser un portefeuille d'investissement en sélectionnant les actions les plus rentables sous une contrainte budgétaire de **500 euros**.  

Deux algorithmes ont été développés pour résoudre ce problème :  
🔹 **Brute-force (`bruteforce.py`)** : teste toutes les combinaisons possibles.  
🔹 **Programmation dynamique (`optimized.py`)** : améliore l'efficacité de la recherche de la meilleure combinaison.  


## 📂 Fichiers du projet  
📄 `bruteforce.py` → Algorithme naïf explorant toutes les combinaisons possibles.  
⚡ `optimized.py` → Algorithme optimisé basé sur la **programmation dynamique**.  

## 🏗️ Explication des Algorithmes  

### 💪 Méthode Brute-Force (`bruteforce.py`)  
L'algorithme **brute-force** teste **toutes les combinaisons possibles** d'actions et sélectionne la plus rentable dans la limite de 500 €.  

#### 🔧 Fonctionnement :  
1️⃣ Génère **toutes les combinaisons possibles** d'actions.  
2️⃣ Calcule le **coût total** et le **profit** pour chaque combinaison.  
3️⃣ Filtre les combinaisons dépassant le budget de 500 €.  
4️⃣ Sélectionne la **meilleure combinaison**.  

✅ **Avantages** : Trouve toujours la solution optimale.  
❌ **Inconvénients** : **Extrêmement lent** pour de grands ensembles de données (Complexité **O(2ⁿ)**).  

### ⚡ Méthode Optimisée (`optimized.py`)  
L'algorithme utilise la **programmation dynamique** pour améliorer **l'efficacité** du calcul. Il évite de recalculer les mêmes sous-problèmes et réduit le temps d'exécution.  

#### 🔧 Fonctionnement :  
1️⃣ Crée une **tableau de programmation dynamique** pour stocker les meilleurs choix d'actions possibles.  
2️⃣ Remplit progressivement le tableau en décidant **action par action** si elle doit être incluse ou non.  
3️⃣ Identifie la **meilleure combinaison d'actions** en fonction du budget.  

✅ **Avantages** : Beaucoup plus rapide (Complexité **O(n × W)**).  
❌ **Inconvénients** : Consomme plus de mémoire que brute-force.  

## 📥 Installation et exécution  

1️⃣ **Cloner le projet**  

```sh
cd "Chemin\complet\vers\le\dossier\du\projet"
git clone https://github.com/Matthieu-Chambon/OC_Projet_7
cd OC_Projet_7
```

2️⃣ Exécutez l'un des scripts :  

💪 **Brute-force** :  
```sh
python bruteforce.py
```
⚡ **Optimisé (programmation dynamique)** :  
```sh
python optimized.py
```

## ⏳ Performances  

| Algorithme          | Complexité  | Temps d'exécution  | Adapté pour ? |
|---------------------|------------|-------------------|--------------|
| 💪 **Brute-force**  | **O(2ⁿ)**   | Très lent 🚫      | Petit dataset |
| ⚡ **Optimisé**     | **O(n × W)** | Rapide 🚀         | Grand dataset |