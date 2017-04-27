import csv


def leermunicipiosine():
    with open('../datos/17codmun.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row)


def transformarnombremunicipio(nombre):
    return nombre


def main():
    print(transformarnombremunicipio("Socuéllamos"))

if __name__ == "__main__":
    main()
