"""Petit exemple de requête HTTP en Python.

Ce script ouvre une page web publique et vérifie que la connexion fonctionne.
Il sert de démonstration simple de l'usage de `urllib.request.urlopen`.
"""

import urllib.request


def main() -> None:
    """Effectue une requête HTTP vers le site ESIEE et affiche un message.

    La fonction ouvre une page web et vérifie que la réponse est bien reçue.
    """
    print("Hello from internet!")
    u = urllib.request.urlopen("https://www.esiee.fr/")
    # print(type(u))
    # print(dir(u))


if __name__ == "__main__":
    main()
