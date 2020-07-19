""""summary"""
import pandas as pd
from pathlib import Path

#todo verticale summary zie projekt lijstbewerken invoegen

def html_sum_form_writer(user_designated_file_path,titel="summary", **kwargs):
    """"build a html file for summary purposes with  *kwargv
    search jinja and flask
    css link toevoegen
    """
    for key, value in kwargs.items():
        print(key, value)

    naam_html_file = f'{user_designated_file_path}/{titel}_.html'
    with open(naam_html_file, "w") as f_html:

        #         for key, value in kwargs.items():
        #             print(key, value)

        print("<!DOCTYPE html>\n", file=f_html)
        print('<html lang = "en">\n', file=f_html)
        print("     <head>\n", file=f_html)
        print("<meta charset='UTF-8>'\n", file=f_html)
        print(f"<title>{titel.capitalize()}</title>\n", file=f_html)
        print("     </head>", file=f_html)
        print("         <body>", file=f_html)
        for key, value in kwargs.items():
            print(f' <p><b>{key}</b> : {value}<p/>', file=f_html)

        print("         </body>", file=f_html)
        print(" </html>", file=f_html)


def summary_rol(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix, rolnummer, veelvoud=1):
    rol = [
        (f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "leeg.pdf")
        for getal in range(
            begin_nummer_uit_lijst, (begin_nummer_uit_lijst + aantal_per_rol))
        for i in range(veelvoud)
    ]
    df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol * veelvoud) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    rol_nummer = pd.DataFrame(
        [(".", "rol nummer", f"{rolnummer}") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    begin_nummer = pd.DataFrame(
        [(".", "begin nummer", f"{begin}") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    eind_nummer = pd.DataFrame(
        [(".", "eind nummer", f"{eind}") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([rol_nummer,begin_nummer,eind_nummer])

    return naam


def lege_summary_rollen(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix, rolnummer, veelvoud=1):
    rol_nummer = pd.DataFrame(
        [(".", "leeg", f"blanco {rolnummer}") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    begin_nummer = pd.DataFrame(
        [(".", "leeg", "") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    eind_nummer = pd.DataFrame(
        [(".", "leeg", "") for x in range(1)],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([rol_nummer, begin_nummer, eind_nummer])

    return naam




