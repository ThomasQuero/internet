# Projet IMDb - scraping des meilleurs films

## Présentation

Ce projet permet de récupérer la liste des films du classement IMDb Top 250 et d'afficher les titres dans l'ordre de lecture HTML.

Le script principal est :

- `python-14-internet-imdb.py`

Le projet utilise l'API HTTP de Python pour télécharger la page HTML d'IMDb, puis un parseur HTML personnalisé pour extraire les titres de films.

## Objectif

L'objectif est de mettre en pratique :

- la récupération d'une page web via `urllib` ;
- l'envoi d'un User-Agent pour simuler un navigateur ;
- l'analyse du HTML avec `HTMLParser` ;
- l'extraction des éléments utiles depuis une page web ;
- la présentation des résultats dans un script simple.

## Structure du projet

```text
internet/
├── README.md
├── IMDb.html
├── main.py
├── python-14-internet-imdb.py
├── pyproject.toml
├── .python-version
├── .gitignore
├── uv.lock
└── .venv/
```

## Fichiers importants

### `python-14-internet-imdb.py`

Ce fichier contient :

- la classe `IMDBParser` héritant de `HTMLParser` ;
- la fonction `scrap_imdb(html_data)` pour extraire les titres ;
- la fonction `main()` qui récupère la page IMDb puis affiche les films.

### `IMDb.html`

C'est une version locale de la page IMDb utilisée pour tester le parseur sans accéder au réseau.

## Fonctionnement

1. La page IMDb est téléchargée via `urllib.request.urlopen`.
2. Une requête HTTP est envoyée avec un `User-Agent` de navigateur.
3. Le HTML est analysé par `HTMLParser`.
4. Lorsqu'un tag `h3` est détecté, le contenu est extrait.
5. Les titres valides sont stockés dans une liste.
6. La liste est affichée dans l'ordre inverse pour correspondre à la logique du classement.

## Exemple de sortie

```text
Les évadés
Le parrain
The Dark Knight: Le chevalier noir
Le parrain, 2ème partie
12 hommes en colère
...
Danse avec les loups
Du rififi chez les hommes
La Belle et la Bête
La couleur des sentiments
Aladdin
```

## Exécution

Pour lancer le script :

```bash
python python-14-internet-imdb.py
```

## Tests

Le script contient des doctests dans la fonction `main()` qui démontrent le fonctionnement attendu du parser sur le fichier `IMDb.html`.

Pour les lancer :

```bash
python -m doctest -v python-14-internet-imdb.py
```

## Remarques

- Ce projet est un exemple simple de scraping web en Python.
- Il ne doit être utilisé qu'à des fins pédagogiques et dans le respect des conditions d'utilisation du site.
- La structure est volontairement légère pour rester facile à lire et à modifier.

## Conclusion

Ce projet illustre comment extraire des informations d'une page web en Python avec des outils de base, sans bibliothèque externe spécialisée.
