import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Nécessite pillow (pip install pillow)


class Character:
    def __init__(self, name, description, image_path):
        self.name = name
        self.description = description
        self.image_path = image_path


class RPGSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélecteur de Personnage RPG")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.characters = self.load_characters()
        self.specializations = ["La Cage", "La Fusion", "Le Bourré", "La Sarbacane", "La Magie Noire", "L'Exorcisme"]
        self.selected_index = 0

        self.details_text = tk.StringVar()
        self.spec_var = tk.StringVar(value=self.specializations[0])
        self.image_label = None
        self.create_widgets()
        self.update_display()

    def load_characters(self):
        descriptions = {
            "Fleuriste": {"Compétence": "Bouquet explosif (dégâts continus)", "Buff": "Parfum apaisant", "Nerf": "Allergies"},
            "Le Pape": {"Compétence": "Anathème", "Buff": "Bénédiction", "Nerf": "Dogme rigide"},
            "CM": {"Compétence": "Bad Buzz", "Buff": "Post Viral", "Nerf": "Burn-out"},
            "Cuisinier": {"Compétence": "Marmite de destruction", "Buff": "Plat revigorant", "Nerf": "Surcuisson"},
            "Agent Sécurité": {"Compétence": "Contrôle musclé", "Buff": "Armure anti-émeute", "Nerf": "Procédure admin"},
            "Huissier": {"Compétence": "Saisie immédiate", "Buff": "Avis de passage", "Nerf": "Papiers manquants"},
            "Procureur": {"Compétence": "Réquisitoire final", "Buff": "Pièce à Conviction", "Nerf": "Objection !"},
            "Dragon": {"Compétence": "Souffle incendiaire", "Buff": "Écailles Titan", "Nerf": "Cupidité"},
        }

        return [
            Character(name, descriptions[name], f"images/{name}.png")
            for name in descriptions
        ]

    def create_widgets(self):
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Button(frame_top, text="⬅️", width=5, command=self.prev_char).grid(row=0, column=0)
        self.perso_label = tk.Label(frame_top, text="", font=("Arial", 14))
        self.perso_label.grid(row=0, column=1, padx=20)
        tk.Button(frame_top, text="➡️", width=5, command=self.next_char).grid(row=0, column=2)

        tk.Label(self.root, textvariable=self.details_text, font=("Arial", 10), justify="left").pack(pady=10)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        spec_frame = tk.Frame(self.root)
        spec_frame.pack(pady=10)
        tk.Label(spec_frame, text="Spécialisation :").pack(side="left")
        ttk.Combobox(spec_frame, textvariable=self.spec_var, values=self.specializations, state="readonly").pack(side="left", padx=5)

        tk.Button(self.root, text="Valider", command=self.validate_selection, bg="lightgreen").pack(pady=15)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def update_display(self):
        char = self.characters[self.selected_index]
        self.perso_label.config(text=f"Personnage : {char.name}")
        self.details_text.set(
            f"Compétence : {char.description['Compétence']}\n"
            f"Buff : {char.description['Buff']}\n"
            f"Nerf : {char.description['Nerf']}"
        )
        try:
            img = Image.open(char.image_path)
            img = img.resize((200, 200))  # Taille image
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
        except:
            self.image_label.config(text="Aucune image trouvée")

    def prev_char(self):
        self.selected_index = (self.selected_index - 1) % len(self.characters)
        self.update_display()

    def next_char(self):
        self.selected_index = (self.selected_index + 1) % len(self.characters)
        self.update_display()

    def validate_selection(self):
        self.result_label.config(
            text=f"Tu as choisi : {self.characters[self.selected_index].name}\n"
                 f"Spécialisation : {self.spec_var.get()}"
        )


# Lancement
if __name__ == "__main__":
    root = tk.Tk()
    app = RPGSelectorApp(root)
    root.mainloop()
