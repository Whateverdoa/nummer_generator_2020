import pandas as pd
import os
from paden import *


def lijstmaker(begin_nummer, totaal, aantal_per_rol):
    begin_nummer_lijst = [
        begin for begin in range(begin_nummer, begin_nummer + totaal - 1, aantal_per_rol)
    ]
    return begin_nummer_lijst


def rol_nummer_lijst(lijst):
    rol_nummers = [f'Rol {num:>{0}{3}}' for num in range(1, len(lijst) + 1)]
    return rol_nummers


def kol_naam_lijst_builder(mes=1):
    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'lees_per_lijst_file_{count:>{0}{4}}'
        print(naam)
        naam = pd.read_csv(posix_pad_naar_file, dtype="str")
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes)
    print(f'kolomnamen = {kolomnamen}')
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]
    # print(lijst_over_axis_1)

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1

    # naam = pd.read_csv(csv)  # naam = pd.read_csv(f'{pad}/{csv}')
    # concatlist.append(naam)

    # lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    # return lijst_over_axis_1


def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ";"
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"Kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)

    namen = list_to_string(kollomnaamlijst)

    return namen




def df_csv_rol_builder_met_rolnummer(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                     rolnummer, veelvoud=1):
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

    twee_extra = pd.DataFrame(
        [(f"{prefix}{x:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(2)],
        columns=["num", "omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [(f"{prefix}{x:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(wikkel)],
        columns=["num", "omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", f"{rolnummer} {begin} t/m {eind}", "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def losse_csv_rollen_builder(posities,
                             vlg,
                             aantal_per_rol,
                             wikkel,
                             begin_nummer_lijst,
                             prefix,
                             postfix,
                             lijst_rolnummer):
    builder = [
        df_csv_rol_builder_met_rolnummer(begin, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                         lijst_rolnummer).to_csv(
            f"{path}/tmp{begin:>{0}{6}}.csv", index=0
        )
        for begin in begin_nummer_lijst
    ]
    # return len(builder)


def rol_num_dikt(begin, vlg, totaal, aantal_per_rol):
    """"maak twee lijsten nummers en rolnummers voeg samen tot dikt"""
    rollen_metbegin_nummers = {}

    beginnummers = [f'{begin:>{0}{vlg}}' for begin in range(begin, begin + totaal, aantal_per_rol)]

    # beginnummers
    aantal_rollen = len(beginnummers)
    getallenvoorrol = len(str(aantal_rollen))

    # rolnummers
    rolnummers = [f'Rol {rolnummer:>{0}{getallenvoorrol}}' for rolnummer in range(1, aantal_rollen + 1)]
    rollen_metbegin_nummers = {rolnummers[i]: beginnummers[i] for i in range(aantal_rollen)}
    # rollen_metbegin_nummers
    return rollen_metbegin_nummers







def stapel_df_baan(lijstin, ordernummer):
    stapel_df = []
    for index in range(len(lijstin)):
        print(lijstin[index])
        to_append_df = pd.read_csv(
            f"{path_vdp}/{lijstin[index]}", ";", dtype="str"
        )  #
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";", index=0)


def stapel_df_baan_met_df_lijst(lijst_van_dataframes, ordernummer):
    pd.concat(lijst_van_dataframes, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";")


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes, user_designated_file_path = path_final):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".;;stans.pdf;" * mes)
    inlooplijst = inlooplijst[:-1] + "\n"  # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = user_designated_file_path / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])

# print(VDP_final)
