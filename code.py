import tkinter as tk
from tkinter import ttk


class Personnage:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Spécialisation:
    def __init__(self, name):
        self.name = name


class RPGSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélecteur de Personnage RPG")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.Personnages = self.load_Personnages()
        self.Specialisations = self.load_Specialisations()
        self.selected_index = 0

        self.details_text = tk.StringVar()
        self.spec_var = tk.StringVar(value=self.Specialisations[0].name)

        self.create_ajouts()
        self.update_display()

    # Chargement des personnages
    def load_Personnages(self):
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
        return [Personnage(name, descriptions[name]) for name in descriptions]

    # Chargement des Specialisations
    def load_Specialisations(self):
        names = [
            "La Cage", "La Fusion", "Le Bourré",
            "La Sarbacane", "La Magie Noire", "L'Exorcisme"
        ]
        return [Spécialisation(name) for name in names]

    # Création de l'interface
    def create_ajouts(self):
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Button(frame_top, text="⬅️", width=5, command=self.prev_char).grid(row=0, column=0)
        self.perso_label = tk.Label(frame_top, text="", font=("Arial", 14))
        self.perso_label.grid(row=0, column=1, padx=20)
        tk.Button(frame_top, text="➡️", width=5, command=self.next_char).grid(row=0, column=2)

        tk.Label(self.root, textvariable=self.details_text, font=("Arial", 10), justify="left").pack(pady=10)

        spec_frame = tk.Frame(self.root)
        spec_frame.pack(pady=10)
        tk.Label(spec_frame, text="Spécialisation :").pack(side="left")
        ttk.Combobox(spec_frame, textvariable=self.spec_var,
                     values=[spec.name for spec in self.Specialisations],
                     state="readonly").pack(side="left", padx=5)

        tk.Button(self.root, text="Valider", command=self.validate_selection, bg="lightgreen").pack(pady=15)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    # Mise à jour du texte affiché
    def update_display(self):
        char = self.Personnages[self.selected_index]
        self.perso_label.config(text=f"Personnage : {char.name}")
        self.details_text.set(
            f"Compétence : {char.description['Compétence']}\n"
            f"Buff : {char.description['Buff']}\n"
            f"Nerf : {char.description['Nerf']}"
        )

    def prev_char(self):
        self.selected_index = (self.selected_index - 1) % len(self.Personnages)
        self.update_display()

    def next_char(self):
        self.selected_index = (self.selected_index + 1) % len(self.Personnages)
        self.update_display()

    def validate_selection(self):
        self.result_label.config(
            text=f"Tu as choisi : {self.Personnages[self.selected_index].name}\n"
                 f"Spécialisation : {self.spec_var.get()}"
        )


# Lancement de l’application
if __name__ == "__main__":
    root = tk.Tk()
    app = RPGSelectorApp(root)
    root.mainloop()
