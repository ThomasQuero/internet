import urllib.request

def main():
    print("Hello from internet!")
    u = urllib.request.urlopen('https://www.esiee.fr/')
    print(type(u))
    print(dir(u))



if __name__ == "__main__":
    main()
