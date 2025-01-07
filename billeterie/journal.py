import argparse
from donnees import articles, interviews

class ElementJournal():
    def __init__(self, date, edition, auteur, contenu):
        self.date = date
        self.edition = edition
        self.auteur = auteur
        self.contenu = contenu

class Article(ElementJournal):
    def __init__(self, date, edition, auteur, titre, contenu):
        super().__init__(date, edition, auteur, contenu)
        self.titre = titre

class Interview(ElementJournal):
    def __init__(self, date, edition, auteur, invite, contenu):
        super().__init__(date, edition, auteur, contenu)
        self.invite = invite

class Generateur():
    def __init__(self, date, edition):
        self.date = date
        self.edition = edition

    def importer(self, articles_file, interviews_file):
        elements = []
        with open(articles_file, 'r', encoding='utf-8') as f_articles:
            for line in f_articles:
                article_data = eval(line)
                if article_data["date"] == self.date and (article_data["edition"] == self.edition or article_data["edition"] == "national"):
                    article = Article(
                        article_data["date"],
                        article_data["edition"],
                        article_data["auteur"],
                        article_data["titre"],
                        article_data["contenu"]
                    )
                    elements.append(article)

        with open(interviews_file, 'r', encoding='utf-8') as f_interviews:
            for line in f_interviews:
                interview_data = eval(line)
                if interview_data["date"] == self.date and (interview_data["edition"] == self.edition or interview_data["edition"] == "national"):
                    interview = Interview(
                        interview_data["date"],
                        interview_data["edition"],
                        interview_data["auteur"],
                        interview_data["invite"],
                        interview_data["contenu"]
                    )
                    elements.append(interview)
        return elements

    def afficher(self, elements):
        print(f"==================================")
        print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
        print(f"==================================")
        for element in elements:
            if isinstance(element, Article):
                print(f"Article : {element.titre}")
                print(f"Auteur : {element.auteur}")
                print(f"Contenu : {element.contenu}\n")
            elif isinstance(element, Interview):
                print(f"Interview de {element.invite}")
                print(f"Intervieweur : {element.auteur}")
                print(f"Contenu : {element.contenu}\n")

def main():
    parser = argparse.ArgumentParser(description="Génère le journal du jour selon une date et une région.")
    parser.add_argument("date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=["national", "idf", "paca"])
    args = parser.parse_args()

    try:
        generateur = Generateur(args.date, args.edition)
        elements = generateur.importer("articles.txt", "interviews.txt")
        generateur.afficher(elements)
    except FileNotFoundError:
        print("Erreur : fichiers d'articles ou d'interviews introuvables.")

if __name__ == "__main__":
    main()
