import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interface_connexion import Ui_Form  # Importer l'IHM


class ConnexionApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connecter le bouton Valider à une fonction
        self.bouton_valider.clicked.connect(self.valider_formulaire)


    def valider_formulaire(self):
        # Récupérer les valeurs des champs de saisie
        identifiant = self.lineEdit_identifiant.text()
        mot_de_passe = self.lineEdit_motDePasse.text()
        email = self.lineEdit_email.text()


        # Vérifier si les champs sont correctement remplis
        if not identifiant or not mot_de_passe or '@' not in email:
            self.afficher_erreur("Erreur : veuillez remplir correctement tous les champs.")
        else:
            self.afficher_message("Connexion réussie.")


    # Fonction pour afficher une boîte de dialogue d'erreur
    def afficher_erreur(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Utiliser une icône d'erreur
        msg.setWindowTitle("Erreur")
        msg.setText(message)
        msg.exec_()


    # Fonction pour afficher une boîte de dialogue d'information
    def afficher_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  # Utiliser une icône d'information
        msg.setWindowTitle("Information")
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ConnexionApp()
    fenetre.show()
    sys.exit(app.exec_())