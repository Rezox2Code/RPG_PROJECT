import os

class Utils:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")


class personnage:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Specialisation:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self):
        self.personnages = self.load_personnages()
        self.Specialisations = self.load_Specialisations()
        self.selected_char_index = 0
        self.selected_spec = None

    def load_personnages(self):
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

        return [personnage(name, descriptions[name]) for name in descriptions]

    def load_Specialisations(self):
        specs = [
            "La Cage", "La Fusion", "Le Bourré",
            "La Sarbacane", "La Magie Noire", "L'Exorcisme"
        ]
        return [Specialisation(name) for name in specs]

    def display_personnage(self):
        Utils.clear()
        print("=== Sélection du personnage ===")
        print("Utilise Q (←) et D (→) puis Entrée pour valider\n")

        for i, char in enumerate(self.personnages):
            display = f"[{char.name}]" if i == self.selected_char_index else char.name
            print(display, end="  ")

        print("\n\nDétails :")
        for key, value in self.personnages[self.selected_char_index].description.items():
            print(f"{key} : {value}")

    def select_personnage(self):
        while True:
            self.display_personnage()
            key = input("\n(q/d pour naviguer, Entrée pour choisir) : ").lower()

            if key == "q":
                self.selected_char_index = (self.selected_char_index - 1) % len(self.personnages)
            elif key == "d":
                self.selected_char_index = (self.selected_char_index + 1) % len(self.personnages)
            elif key == "":
                break

    def display_Specialisation(self):
        Utils.clear()
        print("=== Sélection de spécialisation ===")
        print("Tape le numéro de la spécialisation puis Entrée :\n")

        for i, spec in enumerate(self.Specialisations):
            print(f"{i + 1}) {spec.name}")

    def select_Specialisation(self):
        while True:
            self.display_Specialisation()
            choice = input("\nChoix : ")

            if choice.isdigit() and 1 <= int(choice) <= len(self.Specialisations):
                self.selected_spec = self.Specialisations[int(choice) - 1]
                break

    def start_game(self):
        Utils.clear()
        chosen_char = self.personnages[self.selected_char_index]
        print(" Tu as choisi :")
        print(f"Personnage : {chosen_char.name}")
        print(f"Spécialisation : {self.selected_spec.name}")
        print("\nTu peux maintenant lancer ton RPG !")


# LANCEMENT DU PROGRAMME
if __name__ == "__main__":
    game = Game()
    game.select_personnage()
    game.select_Specialisation()
    game.start_game()
