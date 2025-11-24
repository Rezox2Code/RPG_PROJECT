import tkinter as tk
from tkinter import ttk

# Personnages
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

# Spécialisations
specialisations = [
    "La Cage",
    "La Fusion",
    "Le Bourré",
    "La Sarbacane",
    "La Magie Noire",
    "L'Exorcisme"
]

selected_char = 0

# --- Interface Graphique ---
def update_display():
    """Met à jour l’affichage en fonction du personnage sélectionné"""
    perso_label.config(text=f"Personnage : {personnages[selected_char]}")
    
    details = descriptions[personnages[selected_char]]
    details_text.set(
        f"Compétence : {details['Compétence']}\n"
        f"Buff : {details['Buff']}\n"
        f"Nerf : {details['Nerf']}"
    )

def prev_char():
    """Personnage précédent"""
    global selected_char
    selected_char = (selected_char - 1) % len(personnages)
    update_display()

def next_char():
    """Personnage suivant"""
    global selected_char
    selected_char = (selected_char + 1) % len(personnages)
    update_display()

def validate_selection():
    """Valide et affiche le choix"""
    result_label.config(
        text=f"Tu as choisi : {personnages[selected_char]}\n"
             f"Spécialisation : {spec_var.get()}"
    )

# Création fenêtre
root = tk.Tk()
root.title("Sélecteur de Personnage RPG")
root.geometry("500x400")
root.resizable(False, False)

# Boutons navigation
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

prev_button = tk.Button(frame_top, text="⬅️", width=5, command=prev_char)
prev_button.grid(row=0, column=0)

perso_label = tk.Label(frame_top, text="", font=("Arial", 14))
perso_label.grid(row=0, column=1, padx=20)

next_button = tk.Button(frame_top, text="➡️", width=5, command=next_char)
next_button.grid(row=0, column=2)

# Affichage détails
details_text = tk.StringVar()
details_label = tk.Label(root, textvariable=details_text, font=("Arial", 10), justify="left")
details_label.pack(pady=10)

# Choix de spécialisation
spec_frame = tk.Frame(root)
spec_frame.pack(pady=10)

spec_label = tk.Label(spec_frame, text="Spécialisation :")
spec_label.pack(side="left")

spec_var = tk.StringVar(value=specialisations[0])
spec_dropdown = ttk.Combobox(spec_frame, textvariable=spec_var, values=specialisations, state="readonly")
spec_dropdown.pack(side="left", padx=5)

# Bouton de validation
validate_button = tk.Button(root, text="Valider", command=validate_selection, bg="lightgreen")
validate_button.pack(pady=15)

# Résultat
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Initialisation affichage
update_display()

# Exécution
root.mainloop()
