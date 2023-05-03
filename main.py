biograf = {
    "Sal 1": {
        "rækker": 5,
        "sæder_pr_række": 10,
        "sæder": [[False] * 10 for _ in range(5)],
        "opt_sæder": [],
        "film": "Guardians of the Galaxy Vol. 3"
    },
    "Sal 2": {
        "rækker": 6,
        "sæder_pr_række": 8,
        "sæder": [[False] * 8 for _ in range(6)],
        "opt_sæder": [],
        "film": "Underverden II"
    },
    "Sal 3": {
        "rækker": 4,
        "sæder_pr_række": 12,
        "sæder": [[False] * 12 for _ in range(4)],
        "opt_sæder": [],
        "film": "The Fabelmans"
    }
}


def buy_ticket(sal_nummer, række, sæde):
    if biograf[sal_nummer]["sæder"][række][sæde]:
        print("Dette sæde er allerede optaget.")
    else:
        biograf[sal_nummer]["sæder"][række][sæde] = True
        biograf[sal_nummer]["opt_sæder"].append((række, sæde))
        print(
            f"Du har nu købt billetten til {sal_nummer} i række {række} sæde {sæde}.")


def vis_ledige_sæder(sal_nummer):
    print("Ledige sæder i Sal {}: ".format(sal_nummer))
    for række, sæder in enumerate(biograf[sal_nummer]["sæder"]):
        for sæde, optaget in enumerate(sæder):
            if not optaget:
                print("Række {}, Sæde {}".format(række, sæde))
    print()


def vis_film_i_sal(sal_navn):
    if sal_navn in biograf:
        film = biograf[sal_navn]["film"]
        print(f"I {sal_navn} vises '{film}'.")
    else:
        print("Den valgte sal eksisterer ikke.")


while True:
    print("Velkommen til din nye biograf automat!")
    print("Ledige sale:")
    for biograf_navn in biograf:
        print(biograf_navn + " - " + biograf[biograf_navn]["film"])
    biograf_nr = input("Vælg en sal: ")
    biograf_navn = f"Sal {biograf_nr}"
    if biograf_navn not in biograf:
        print("Den valgte sal eksisterer ikke.")
        print("\n ")
        continue
    vis_ledige_sæder(biograf_navn)
    række = int(input("Hvilken række vil du sidde i? "))
    if række < 0 or række >= biograf[biograf_navn]["rækker"]:
        print("Den valgte række eksisterer ikke.")
        print("\n ")
        continue
    sæde = int(input("Hvilket sæde vil du sidde på? "))
    if sæde < 0 or sæde >= biograf[biograf_navn]["sæder_pr_række"]:
        print("Det valgte sæde eksisterer ikke.")
        print("\n ")
        continue
    buy_ticket(biograf_navn, række, sæde)
