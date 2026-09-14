import urllib.request
from html.parser import HTMLParser


class IMDBParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.films = []
        self.dans_titre = False

    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            self.dans_titre = True

    def handle_endtag(self, tag):
        if tag == "h3":
            self.dans_titre = False

    def handle_data(self, data):
        if self.dans_titre:
            titre = data.strip()

            if titre:
                self.films.append(titre)


def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    parser = IMDBParser()
    parser.feed(html_data)

    return parser.films


def main():
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies = scrap_imdb(html_data)
    >>> for m in movies[:5]: print(m)
    Les évadés
    Le parrain
    The Dark Knight: Le chevalier noir
    Le parrain, 2ème partie
    12 hommes en colère
    >>> for m in movies[-5:]: print(m)
    Aladdin
    La couleur des sentiments
    La Belle et la Bête
    Du rififi chez les hommes
    Danse avec les loups
    """

    url = "https://www.imdb.com/chart/top?ref_=nv_ch_250_4"

    firefox = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) "
        "Gecko/20100101 Firefox/101.0"
    )

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", firefox)

        response = urllib.request.urlopen(req)

        html_data = response.read().decode("utf8")  

    except IOError:
        print("Erreur lors de la récupération de la page IMDb")
        return None

    movies = scrap_imdb(html_data)

    for movie in reversed(movies):
        print(movie)

    return None


if __name__ == "__main__":
    main()