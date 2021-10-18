"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Restaurent Manager Solution Basic",
    version = "3.1.0",
    description = "RestoManagerSolution Gestionnaire de Restaurent point de vente et prise en charge de caisse...",
    executables = [Executable("mainWindowMain.py")]
)