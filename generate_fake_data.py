import pandas as pd
import numpy as np
from datetime import datetime
import random

# Paramètres
NB_LIGNES = 50_000
ANNEE_DEBUT = 2010
ANNEE_FIN = 2025
REGIONS = [
    "Total", "Port-au-Prince", "Nord", "Sud", "Artibonite", 
    "Ouest", "Grand'Anse", "Nippes", "Centre", "Nord-Est", 
    "Nord-Ouest", "Sud-Est"
]
INDICATEURS = [
    "Population", "PIB (milliards USD)", "Taux de chômage (%)", 
    "Taux d'inflation (%)", "Exportations (millions USD)", 
    "Importations (millions USD)", "Investissement direct étranger (millions USD)",
    "Nombre d'étudiants", "Nombre d'hôpitaux", "Mortalité infantile (pour 1000)",
    "Espérance de vie (années)", "Taux d'alphabétisation (%)",
    "Production agricole (tonnes)", "Émissions de CO2 (kt)"
]

def generer_valeur(indicateur, region, annee):
    """Génère une valeur réaliste selon l'indicateur, la région et l'année."""
    base = 0
    if "Population" in indicateur:
        base = 100000 if region == "Total" else random.randint(50000, 2_000_000)
        # croissance annuelle 2%
        base *= (1 + 0.02 * (annee - ANNEE_DEBUT))
        return int(base)
    elif "PIB" in indicateur:
        base = 20 if region == "Total" else random.uniform(0.5, 5)
        base *= (1 + 0.03 * (annee - ANNEE_DEBUT))
        return round(base, 1)
    elif "chômage" in indicateur:
        base = random.uniform(5, 25)
        return round(base, 1)
    elif "inflation" in indicateur:
        base = random.uniform(3, 20)
        return round(base, 1)
    elif "Exportations" in indicateur:
        base = random.randint(100, 5000)
        base += (annee - ANNEE_DEBUT) * 50
        return int(base)
    elif "Importations" in indicateur:
        base = random.randint(200, 6000)
        base += (annee - ANNEE_DEBUT) * 60
        return int(base)
    elif "investissement" in indicateur.lower():
        base = random.randint(50, 800)
        return int(base)
    elif "étudiants" in indicateur:
        base = random.randint(5000, 300_000)
        return int(base)
    elif "hôpitaux" in indicateur:
        base = random.randint(1, 200)
        return int(base)
    elif "Mortalité" in indicateur:
        base = random.uniform(15, 60)
        # tendance à la baisse
        base -= (annee - ANNEE_DEBUT) * 0.5
        return round(max(5, base), 1)
    elif "Espérance de vie" in indicateur:
        base = random.uniform(55, 70)
        base += (annee - ANNEE_DEBUT) * 0.2
        return round(min(80, base), 1)
    elif "alphabétisation" in indicateur:
        base = random.uniform(40, 90)
        base += (annee - ANNEE_DEBUT) * 0.5
        return round(min(99, base), 1)
    elif "agricole" in indicateur:
        base = random.randint(1000, 50_000)
        return int(base)
    elif "CO2" in indicateur:
        base = random.randint(1000, 15000)
        return int(base)
    else:
        return round(random.uniform(10, 1000), 2)

# Génération du DataFrame
data = []
for _ in range(NB_LIGNES):
    annee = random.randint(ANNEE_DEBUT, ANNEE_FIN)
    region = random.choice(REGIONS)
    indicateur = random.choice(INDICATEURS)
    valeur = generer_valeur(indicateur, region, annee)
    data.append([annee, indicateur, valeur, region])

df = pd.DataFrame(data, columns=["annee", "indicateur", "valeur", "region"])

# Trier pour un affichage plus lisible (optionnel)
df = df.sort_values(["indicateur", "annee", "region"]).reset_index(drop=True)

# Sauvegarde en CSV et Excel
csv_file = "statistiques_generes.csv"
excel_file = "statistiques_generes.xlsx"
df.to_csv(csv_file, index=False, encoding="utf-8")
df.to_excel(excel_file, index=False, engine="openpyxl")

print(f"Fichier généré : {csv_file} ({len(df)} lignes)")
print(f"Fichier généré : {excel_file} ({len(df)} lignes)")
print("\nAperçu des 5 premières lignes :")
print(df.head())

# Petit échantillon de questions possibles pour le chatbot
print("\nExemples de questions que ton chatbot pourra répondre :")
print("- Quelle était la population totale d'Haïti en 2020 ?")
print("- Quel a été le PIB de la région Nord en 2022 ?")
print("- Tendance du taux de chômage à Port-au-Prince entre 2015 et 2025 ?")
print("- Quel indicateur a la plus forte valeur en 2024 ?")
print("- Compare les importations et exportations en 2023.")