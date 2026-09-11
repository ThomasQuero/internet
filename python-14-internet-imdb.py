# Vos imports ici..

class IMDBParser(HTMLParser):
    # Votre classe ici
    def __init__(self):
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    # Votre code ici...
    l = []
    return l
    
        
def main():
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies =  scrap_imdb(html_data)
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
    # Votre code ici...
    
    url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
    try:
        html_data = ""
    except IOError:
        pass
    
    movies =  scrap_imdb(html_data)
    
    # print reversed list of movies
    
    return None

if __name__ == '__main__':
    main()