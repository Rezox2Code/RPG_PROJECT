import os

# touts les personnages
personnages = [
    "Fleuriste", "Le Pape", "CM", "Cuisinier",
    "Agent Sécurité", "Huissier", "Procureur", "Dragon"
]

descriptions = {
    "Fleuriste": {
        "Compétence": "Bouquet explosif (dégâts continus)",
        "Buff": "Parfum apaisant (soin équipe, 3 tours)",
        "Nerf": "Allergies (-10% précision)"
    },
    "Le Pape": {
        "Compétence": "Anathème (gros dégâts)",
        "Buff": "Bénédiction (+attaque & défense)",
        "Nerf": "Dogme rigide (inutilisable <20% PV)"
    },
    "CM": {
        "Compétence": "Bad Buzz (provocation + debuff)",
        "Buff": "Post Viral (boost aléatoire)",
        "Nerf": "Burn-out (-15% vitesse <50% PV)"
    },
    "Cuisinier": {
        "Compétence": "Marmite de destruction (zone)",
        "Buff": "Plat revigorant (+PV max)",
        "Nerf": "Surcuisson (risque auto-brûlure)"
    },
    "Agent Sécurité": {
        "Compétence": "Contrôle musclé (stun 1 tour)",
        "Buff": "Armure anti-émeute (tank)",
        "Nerf": "Procédure admin (perd un tour)"
    },
    "Huissier": {
        "Compétence": "Saisie immédiate (retire buff + dégâts)",
        "Buff": "Avis de passage (+défense/précision)",
        "Nerf": "Papiers manquants (20% échec)"
    },
    "Procureur": {
        "Compétence": "Réquisitoire final (gros dégâts)",
        "Buff": "Pièce à Conviction (+attaque si debuff)",
        "Nerf": "Objection ! (-20% attaque si allié K.O)"
    },
    "Dragon": {
        "Compétence": "Souffle incendiaire (énorme zone)",
        "Buff": "Écailles Titan (-dégâts)",
        "Nerf": "Cupidité (perd un tour si objet rare)"
    },
}

# toutes les spécialisation
specialisations = [
    "La Cage",
    "La Fusion",
    "Le Bourré",
    "La Sarbacane",
    "La Magie Noire",
    "L'Exorcisme"
]

selected_char = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_character():
    clear()
    print("=== Sélection du personnage ===")
    print("Utilise Q (←) et D (→) puis Entrée pour valider\n")

    for i, char in enumerate(personnages):
        print(f"[{char}]" if i == selected_char else char, end="  ")

    print("\n\nDétails :")
    for k, v in descriptions[personnages[selected_char]].items():
        print(f"{k} : {v}")

def display_specialization():
    clear()
    print("=== Sélection de spécialisation ===")
    print("Tape le numéro de la spécialisation puis Entrée :\n")
    
    for i, spec in enumerate(specialisations):
        print(f"{i+1}) {spec}")

# Méthode pour séléctionner les personnages
while True:
    display_character()
    key = input("\n(q/d pour naviguer, Entrée pour choisir) : ").lower()

    if key == "q":
        selected_char = (selected_char - 1) % len(personnages)
    elif key == "d":
        selected_char = (selected_char + 1) % len(personnages)
    elif key == "":
        break

# Méthode pour séléctionner les spécilisations
while True:
    display_specialization()
    choice = input("\n👉 Choix : ")

    if choice.isdigit() and 1 <= int(choice) <= len(specialisations):
        selected_spec = specialisations[int(choice)-1]
        break

# Print de tout les informations
clear()
print("🎯 Tu as choisi :")
print(f"Personnage : {personnages[selected_char]}")
print(f"Spécialisation : {selected_spec}")
print("\nTu peux maintenant lancer ton RPG !")
