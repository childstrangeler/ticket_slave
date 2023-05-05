# opretter en dictionary ved navn biograf.
biograf = {
    # opretter en biografsal ved navn "Sal 1".
    "Sal 1": {
        # sætter hvor mange rækker der er i salen.
        "rækker": 5,
        # sætter hvor mange sæder der er i hver række.
        "sæder_pr_række": 10,
        # laver en liste over alle sæder i salen, og sætter dem alle til "false",
        # hvilket i denne sammenhæng betyder at de er ledige.
        "sæder": [10 * [False] for i in range(5)],
        # laver en tom liste over optagede sæder.
        "opt_sæder": [],
        # viser hvilken film der kører i salen.
        "film": "Guardians of the Galaxy Vol. 3"
    },
    "Sal 2": {
        "rækker": 6,
        "sæder_pr_række": 8,
        "sæder": [8 * [False] for i in range(6)],
        "opt_sæder": [],
        "film": "Underverden II"
    },
    "Sal 3": {
        "rækker": 4,
        "sæder_pr_række": 12,
        "sæder": [12 * [False] for i in range(4)],
        "opt_sæder": [],
        "film": "The Fabelmans"
    }
}


def køb_billet(sal_nummer, række, sæde):
    # checker om det valgte sæde er optaget.
    if biograf[sal_nummer]["sæder"][række][sæde]:
        print("Dette sæde er allerede optaget.")
    # hvis sædet ikke er optaget tilføjes sædet til "opt_sæder",
    # og det bliver true i "sæder" 2d-arrayet.
    else:
        biograf[sal_nummer]["sæder"][række][sæde] = True
        biograf[sal_nummer]["opt_sæder"].append((række, sæde))
        # printer en besked om at biletten til det valgte sæde er købt.
        # Da dette er en "f-string" kan man i tuborgklammer indsætte variabelnavne
        # og derved indsætte den værdi variablen holder.
        print(
            f"Du har nu købt billetten til {sal_nummer}, række {række} sæde {sæde}.")


def frie_sæder(sal_nummer):
    # printer en besked der siger hvilken sals sæder vi kigger på.
    print("Ledige sæder i Sal {}: ".format(sal_nummer))
    # går over hver række og sæde i salen.
    for række, sæder in enumerate(biograf[sal_nummer]["sæder"]):
        for sæde, optaget in enumerate(sæder):
            # hvis et sæde ikke er optaget printes dets række- og sæde nummer.
            if not optaget:
                print("Række {}, Sæde {}".format(række, sæde))
    print()

# troede det ville blive relevant at kunne tage fat i denne funktion,
# andre steder i koden, men der var ikke tid til at bruge det til noget.


def vis_film_i_sal(sal_navn):
    # chekker om det valgte "sal_navn" er i biograf variablen.
    if sal_navn in biograf:
        # hvis salen eksisterer findes "film" variablen der passer til.
        film = biograf[sal_navn]["film"]
        # printer den film der kører i den valgte sal.
        print(f"I {sal_navn} vises '{film}'.")


while True:
    # sender en hyggelig besked i starten af hver interaktion.
    print("Velkommen til din nye biograf automat!")
    print("Ledige sale:")
    for biograf_navn in biograf:
        # viser navnet på salene, og hvilke film der vises i de forskellige sale.
        print(biograf_navn + " - " + biograf[biograf_navn]["film"])
    # tager bruger input til at vælge hvilken sal der skal hives fat i.
    biograf_nr = input("Vælg en sal: (skriv venligst et validt tal)")
    biograf_navn = f"Sal {biograf_nr}"
    # undersøger om den sal brugeren har valgt overhovedet eksisterer.
    if biograf_navn not in biograf:
        # hvis den valgte sal ikke eksisterer,
        # printes en errormessage og while-loopet startes forfra.
        print("Den valgte sal eksisterer ikke.")
        print("\n")
        # "continue" er det keyword der springer tilbage til toppen af loopet,
        # uden at eksekvere koden under.
        continue
    # viser de ledige sæder der eksisterer, i den sal brugeren har valgt.
    frie_sæder(biograf_navn)
    # tager bruger input til at vælge hvilken række de vil sidde på.
    række = int(
        input("Hvilken række vil du sidde i? (skriv venligst et validt tal)"))
    # chekker om rækken brugeren har valgt eksisterer i den sal brugeren har valgt.
    if række < 0 or række >= biograf[biograf_navn]["rækker"]:
        # hvis den valgte sal ikke eksisterer,
        # printes en errormessage og while-loopet startes forfra.
        print("Den valgte række eksisterer ikke.")
        print("\n")
        continue
    # tager bruger input til at vælge hvilket sæde de vil sidde på.
    sæde = int(
        input("Hvilket sæde vil du sidde på? (skriv venligst et validt tal)"))
    # chekker om sædet brugeren har valgt eksisterer i den række brugeren har valgt.
    if sæde < 0 or sæde >= biograf[biograf_navn]["sæder_pr_række"]:
        # hvis det valgte sæde ikke eksisterer,
        # printes en errormessage og while-loopet startes forfra.
        print("Det valgte sæde eksisterer ikke.")
        print("\n")
        continue
    # hvis loopet når hertil uden fejl, eksekveres "køb_billet" funktionen.
    køb_billet(biograf_navn, række, sæde)
