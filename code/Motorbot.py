print("Hola, benvingut a Motorbot! Un Bot de conversa preparat per trobar el teu cotxe ideal!")
nom = input("Com et dius? ")
nom = nom. split(" ")
nom = nom[-1]
print("Hola, " + nom + "! Encantat de coneixer-te.")

print("Pots fer-me preguntes com 'Com et dius?', 'Quins son els combustibles mes rendibles?', 'Com se quin es el cotxe ideal per a mi?' o 'Adeu' per finalitzar la conversa.")
print("També pots dir-me 'vull que m'ajudis a trobar el meu cotxe' per començar la recomanació personalitzada.")

while True:
    entrada = input("Tu: ").lower().strip()

    if "com et dius" in entrada or "qui ets" in entrada:
        print("Em dic Motorbot! Et puc ajudar a trobar el teu proper vehicle ideal.")

    elif "combustibles mes rendibles" in entrada or "combustibles més rendibles" in entrada:
        print("GLP o gas: És el combustible més barat i rendible per a la majoria de conductors.")
        print("Electricitat: Té el cost per quilòmetre més baix, sobretot si carregues a casa.")
        print("Dièsel: Només surt a compte si fas molts quilòmetres, sobretot per autopista.")
        print("Gasolina: És el menys rendible, però els cotxes solen ser més barats de comprar.")

    elif "cotxe ideal" in entrada or "quin cotxe" in entrada:
        print("Per saber quin cotxe és per a tu, pensa en l’ús que en faràs, els quilòmetres anuals i el teu pressupost.")
        print("Si t’agrada conduir-lo i s’adapta al teu dia a dia, segurament és el teu cotxe ideal.")

    elif "vull que m'ajudis a trobar el meu cotxe" in entrada or "vui que m'ajudis a trobar el meu cotxe" in entrada or "ajudar-me a trobar un cotxe" in entrada:
        print("Perfecte! Comencem la cerca del teu cotxe ideal, " + nom + ".")


        pressupost = input("Quin es el teu pressupost (€)? ")
        us = input("Quin us li donaries al cotxe (circuit / per anar del punt A al B / una mica de cada)? ").lower()
        pref = input("Que prefereixes: cotxes Japonesos qeu son conegusta per la seva fiabilitat, cotxes Italians que son coneguts pel seu disseny o Alemanys coneguts pel se gran rendiment y esportivitat? ").lower()

        p = int(pressupost)

        if p < 12000:
            print("Amb un pressupost de", p, "euros et recomano mirar cotxes de segona ma.")
            print("Per exemple:")
            print("- Toyota Yaris o Honda Jazz (japonesos)")
            print("- Fiat Panda o Punto (italians)")
            print("- Volkswagen Polo o Opel Corsa (alemanys)")

        elif p < 25000:
            print("Amb un pressupost mitja-baix pots trobar bons cotxes nous o de segona mà.")
            if "jap" in pref:
                if "circuit" in us:
                    print("Et recomano el Mazda MX-5, petit i molt divertit de conduir.")
                elif "punt" in us:
                    print("Et recomano el Toyota Yaris Hybrid, molt eficient per ciutat.")
                else:
                    print("Et recomano el Honda Civic, equilibrat, fiable y amb capaccitats de millora asequibles.")
            elif "ital" in pref:
                if "circuit" in us:
                    print("Et recomano l'Alfa Romeo Mito, amb estil i caràcter.")
                elif "punt" in us:
                    print("Et recomano el Fiat 500, petit i pràctic per ciutat.")
                else:
                    print("Et recomano el Fiat Tipo, un cotxe senzill i còmode.")
            elif "alem" in pref:
                if "circuit" in us:
                    print("Et recomano el Volkswagen Polo GTI, esportiu pero equilibrat en el seu rendiment.")
                elif "punt" in us:
                    print("Et recomano el Volkswagen Golf, molt equilibrat amb una gran capacitat de modificació.")
                else:
                    print("Et recomano el BMW serie 1, pràctic i ben fet. Que amb unes petites modificacions pot ser un gran cotxe")
            else:
                print("Et recomano un Kia Ceed, bon rendiment i preu raonable.")

        elif p < 50000:
            print("Amb aquest pressupost pots trobar cotxes de gama mitjana-alta.")
            if "jap" in pref:
                if "circuit" in us:
                    print("Et recomano el Toyota GR86, esportiu i fiable.")
                elif "punt" in us:
                    print("Et recomano el Lexus UX 250h, còmode i eficient.")
                else:
                    print("Et recomano el Mazda CX-5, perfecte per tot tipus d'us.")
            elif "ital" in pref:
                if "circuit" in us:
                    print("Et recomano l'Alfa Romeo Giulia, molt bonic i potent.")
                elif "punt" in us:
                    print("Et recomano el Fiat 500X, bon SUV petit per ciutat i carrers estrets.")
                else:
                    print("Et recomano l'Alfa Romeo Tonale, modern i polivalent, ideal per a molts publics.")
            elif "alem" in pref:
                if "circuit" in us:
                    print("Et recomano el BMW Serie 2, bastant esportiu i ben fet.")
                elif "punt" in us:
                    print("Et recomano el Volkswagen Passat, còmode i segur, ideal per a tota la familia.")
                else:
                    print("Et recomano el Audi Q3, tecnologic i espaiós per dins.")
            else:
                print("Et recomano un Hyundai Tucson, molt complet i fiable.")

        else:
            print("Amb un pressupost de", p, "euros pots permetre't cotxes d'alta gamma.")
            if "circuit" in us:
                print("- Nissan GT-R (japones)")
                print("- Ferrari Roma (italia)")
                print("- Porsche 911 Turbo S (alemany)")
            elif "punt" in us:
                print("- Lexus ES 300h (japones)")
                print("- Maserati Ghibli (italia)")
                print("- Mercedes Classe E (alemany)")
            else:
                print("- Toyota Supra (japones)")
                print("- Alfa Romeo Stelvio (italia)")
                print("- BMW X5 (alemany)")

        print("Gracies per parlar amb mi,", nom)

    elif "adeu" in entrada:
        print("Adeu", nom, ". Espero haver-te ajudat. Que tinguis un bon dia.")
        break

    else:
        print("Ho sento, no entenc aquesta pregunta. Prova amb una altra.")
