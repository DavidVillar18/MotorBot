# -*- coding: utf-8 -*-
"""
Chatbot 'Motorbot' per ajudar a trobar el cotxe ideal.
@author: David Villar Morales
"""

########## FUNCIONS DEL XATBOT ################################################


def salutacio():
    """Demana el nom a l’usuari, el saluda i retorna el nom."""
    print("Hola, benvingut al Motorbot! El bot que t’ajuda a trobar el teu cotxe ideal!")
    nom = input("Com et dius? ").strip()
    
    # Agafem l’últim nom si l’usuari escriu nom i cognoms
    nom = nom.split(" ")[-1]
    
    print(f"Encantat de coneixe't, {nom}!")
    return nom


def instruccions():
    """Mostra les instruccions bàsiques per utilitzar el xatbot."""
    print("""
Pots fer-me preguntes com:
- Com et dius?
- Quins són els combustibles més rendibles?
- Com sé quin és el cotxe ideal per a mi?

També pots dir-me:
- 'Vull que m'ajudis a trobar el meu cotxe' → per començar la recomanació personalitzada.

I quan vulguis marxar pots dir:
- Adeu
""")


def combustibles():
    """Explica quins són els combustibles més rendibles."""
    print("GLP o gas → És el combustible més barat i rendible.")
    print("Electricitat → Cost per km molt baix, sobretot carregant a casa.")
    print("Dièsel → Rendible si fas molts km i per autopista.")
    print("Gasolina → Menys rendible però cotxes més assequibles.")


def cotxe_ideal():
    """Dona consells generals per triar un cotxe ideal."""
    print("Pensa en l’ús del cotxe, quilòmetres anuals i pressupost.")
    print("Si s’adapta al teu dia a dia i t’agrada conduir-lo, és el teu cotxe ideal.")


def recomanacio_pressupost(pressupost, pref):
    """Genera recomanacions segons pressupost i preferències."""
    if pressupost < 12000:
        return [
            "Amb menys de 12.000€ et recomano cotxes de segona mà:",
            "- Toyota Yaris",
            "- Fiat Panda",
            "- Volkswagen Polo"
        ]

    elif pressupost < 25000:
        msg = ["Amb aquest pressupost pots optar per bons cotxes nous o semi-nous."]
        if "jap" in pref:
            msg.append("Et recomano Honda Civic o Toyota Yaris Hybrid.")
        elif "ital" in pref:
            msg.append("Et recomano Fiat 500 o Alfa Romeo Mito.")
        elif "alem" in pref:
            msg.append("Et recomano Volkswagen Golf o BMW Serie 1.")
        else:
            msg.append("Et recomano Kia Ceed, molt equilibrat.")
        return msg

    elif pressupost < 50000:
        msg = ["Pressupost suficient per cotxes de gamma mitjana-alta."]
        if "jap" in pref:
            msg.append("Et recomano Toyota GR86 o Mazda CX-5.")
        elif "ital" in pref:
            msg.append("Et recomano Alfa Romeo Giulia o Fiat 500X.")
        elif "alem" in pref:
            msg.append("Et recomano BMW Serie 2 o Audi Q3.")
        else:
            msg.append("Et recomano Hyundai Tucson, complet i fiable.")
        return msg

    else:
        return [
            f"Amb {pressupost}€ tens accés a gamma alta:",
            "- Nissan GT-R",
            "- Ferrari Roma",
            "- Porsche 911"
        ]


def recomanacio_personal(nom):
    """Demana dades personals i recomana els millors cotxes."""
    print(f"Perfecte {nom}, comencem la teva recomanació personalitzada!")

    pressupost = int(input("Quin és el teu pressupost (€)? "))
    us = input("Quin ús faràs del cotxe? (Circuit / A-B / Mixt): ").lower()
    pref = input("Quina procedència prefereixes? (Japonesos / Italians / Alemanys): ").lower()

    recom = recomanacio_pressupost(pressupost, pref)

    for r in recom:
        print(r)

    print(f"Gràcies per utilitzar el servei, {nom}!")


########## FUNCIÓ PRINCIPAL ###################################################


def iniciar_chatbot():
    """Funció principal que gestiona tota la conversa del xatbot."""
    nom = salutacio()     # Saludem l’usuari
    instruccions()        # Expliquem com funciona

    while True:
        entrada = input("Tu: ").lower().strip()

        # Gestió d’accions segons l’entrada
        if "com et dius" in entrada or "qui ets" in entrada:
            print("Sóc el Motorbot! El teu assistent per trobar cotxes.")
        
        elif "combustibles" in entrada:
            combustibles()
        
        elif "cotxe ideal" in entrada:
            cotxe_ideal()
        
        elif "ajudis" in entrada or "ajudar" in entrada or ("trobar" in entrada and "cotxe" in entrada):
            recomanacio_personal(nom)
        
        elif "adeu" in entrada:
            print(f"Adeu {nom}, gràcies per utilitzar el Motorbot!")
            break
        
        else:
            print("No he entès el que has dit. Pots repetir-ho o provar amb una altra pregunta.")


########## PUNT D'ENTRADA DEL PROGRAMA ########################################

if __name__ == "__main__":
    iniciar_chatbot()     # El programa comença aquí
