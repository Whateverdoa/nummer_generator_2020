""""nummer generator 2020"""

import PySimpleGUI as sg
import os
import pandas as pd
import sys
import mes_wikkel as mes_wik
from paden import *
from summary_code import html_sum_form_writer, summary_rol, lege_summary_rollen
from rollen import rest_uitrekenen, rol_num_dikt, df_lege_csv_rol_builder_met_rolnummer



# Very basic window.  Return values as a dictionairy
# todo cleaner
# todo dynamic concatenations:)
# todo multiple vdps


def main():
    sg.change_look_and_feel('Dark')

    layout = [
        # [sg.Text("VDP"), sg.Checkbox('nummers', default=True), sg.Checkbox('beelden')],

        [sg.Text('Nummer generator 2.0', text_color="Yellow")],
        [sg.Text('Ordernummer', size=(15, 1)), sg.InputText(key="order_number")],
        # [sg.Text("Aantal VDP's", size=(15, 1)), sg.InputText('default = 1',key="aantal_vdps")],

        [sg.Text("VDP map voor csv's")],
        [sg.In(key='folder_voor_vdp_map')],[sg.FolderBrowse(target="folder_voor_vdp_map")],


        [sg.Text()],
        [sg.CalendarButton("Datum")],
        [sg.Text()],

        [sg.Text('Totaal aantal', size=(15, 1)), sg.Input(key="totaal_aantal")],
        [sg.Text('Beginnummer', size=(15, 1)), sg.InputText(key="begin_nummer")],

        [sg.Text('Veelvoud', size=(15, 1)), sg.InputText(key="veelvoud")],

        [sg.Text('posities', size=(15, 1)), sg.InputText(key="posities")],
        [sg.Text('voorloop getal', size=(15, 1)), sg.InputText(key="vlg0")],
        [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],
        [sg.Text('Mes', size=(15, 1)), sg.InputText(key='mes')],

        [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(key="Y_waarde")],
        [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],
        [sg.Text('prefix', size=(15, 1)), sg.InputText(key="prefix")],
        [sg.Text('postfix', size=(15, 1)), sg.InputText(key="postfix")],
        [sg.Text('hoogte etiket', size=(15, 1)), sg.InputText(key="hoogte")],
        [sg.Text('opmerkingen', size=(15, 1)), sg.InputText("geen opmerkingen",key="opmerkingen")],


        [sg.Button("Ok"), sg.Cancel()],

        [sg.Text('_' * 80)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        # [sg.Text('Your Folder', size=(15, 1), justification='right'),
        #  sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('Nummer_Generator 2020').Layout(layout)

    while True:
        event, values = window.Read()

        if event in ("Exit", None):
            break

        elif event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            # False in mac OS otherwise it will crash
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            # False in mac OS otherwise it will crash
            window.LoadFromDisk(filename)
            # load(form)

        elif event == "Ok":

            print("ok")

            # print(button, values["order_number"], values["begin_nummer"], values["posities"])

            # datum = values["Datum"]
            # to do datum automtisch maken

            ordernummer = values["order_number"]
            totaal_aantal = int(values["totaal_aantal"])
            begin_nummer = int(values["begin_nummer"])
            veelvoud = int(values["veelvoud"])
            posities = int(values["posities"])
            vlg = int(values["vlg0"])
            aantal_per_rol = int(values["aantal_per_rol"])
            Y_waarde = int(values["Y_waarde"])
            wikkel = int(values["wikkel"])
            hoogte = int(values["hoogte"])
            prefix = values["prefix"]
            postfix = values["postfix"]
            mes = int(values["mes"])
            opmerkingen= values["opmerkingen"]

            naar_folder_pad = Path(values['folder_voor_vdp_map'])
            print(f'naar_folder_pad: {naar_folder_pad}')
            inloop = Y_waarde * 10 - Y_waarde

            # print(datum)

            # use a dict to specify the summeary output or use dict values


            # print(type(int(values["order_number"])))
            # aantallen = int(values[0])
            # print(aantallen)
            # mes_wik.df_csv_rol_builder_met_rolnummer()

            # ___________________________________________________________________________________
            # todo functie invoegen die de folders leegmaakt

            # csvs = [x for x in os.listdir(path_vdp) if x.endswith(".csv")]
            # print(csvs)
            # for file in csvs:
            #     naam = f"{path_vdp}/{file}"  # /VDP_map
            #     # print(naam)
            #     if os.path.exists(naam):
            #         os.remove(naam)
            #     else:
            #         print("empty")

            # csvs = [x for x in os.listdir(path) if x.endswith(".csv")]
            # # print(csvs)
            # for file in csvs:
            #     naam = f"{path}/{file}"  # /tmp
            #     # print(naam)
            #     if os.path.exists(naam):
            #         os.remove(naam)
            #     else:
            #         print("empty")

            # VDP_final = [x for x in os.listdir(path_final) if x.endswith(".csv")]
            # print(VDP_final)
            #
            # for file in VDP_final:
            #     naam = f"{path_final}/{file}"
            #     if os.path.exists(naam):
            #         os.remove(naam)
            #     else:
            #         print("empty")
            # _____________________________

            beginlijst = mes_wik.rol_num_dikt(begin_nummer, vlg, totaal_aantal, aantal_per_rol)
            print(f'beginlijst met rol nummers : {beginlijst}')

            gemaakte_posix_paden = []
            summary_pad_namen_posix=[]
            count = 0
            for key in beginlijst.items():
                rol_nummer = key[0]
                beginnummer = int(key[1])
                filenaam = f'tmp{count:>{0}{6}}.csv'
                padnaam = Path(path.joinpath(filenaam))
                sum_pad_naam = Path(pad_sum.joinpath(filenaam))
                # print(padnaam)
                gemaakte_posix_paden.append(padnaam)
                summary_pad_namen_posix.append(sum_pad_naam)
                mes_wik.df_csv_rol_builder_met_rolnummer(beginnummer, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                                         rol_nummer, veelvoud).to_csv(padnaam, index=0)

                summary_rol(beginnummer, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                                         rol_nummer, veelvoud).to_csv(sum_pad_naam, index=0)
                count += 1
                print(beginnummer, filenaam, padnaam)

            # todo rest functie hier invoegen en extra rollen in tmp zetten (tel) aaltal files in map
            hoeveelheid_rest_rollen = rest_uitrekenen(mes, totaal_aantal, aantal_per_rol)


            if hoeveelheid_rest_rollen != 0:
                print(f'dit is de hoeveelheid_rest_rollen: {hoeveelheid_rest_rollen}')
                aantal_rollen = totaal_aantal//aantal_per_rol

                rest_rollen_dikt = rol_num_dikt(1,vlg, hoeveelheid_rest_rollen,aantal_per_rol,aantal_rollen)
                print(f"dit is de dikt restrollen: {rest_rollen_dikt}")

                rest_gemaakte_posix_paden = []
                rest_summary_pad_namen_posix=[]
                count = aantal_rollen
                for key in rest_rollen_dikt.items():
                    rol_nummer = key[0]
                    beginnummer = int(key[1])
                    filenaam = f'tmp{count:>{0}{6}}.csv'
                    padnaam = Path(path.joinpath(filenaam))

                    sum_pad_naam = Path(pad_sum.joinpath(filenaam))

                    # print(padnaam)
                    rest_gemaakte_posix_paden.append(padnaam)
                    rest_summary_pad_namen_posix.append(sum_pad_naam)


                    df_lege_csv_rol_builder_met_rolnummer(beginnummer, posities, vlg, aantal_per_rol, wikkel, prefix,
                                                             postfix, rol_nummer, veelvoud).to_csv(padnaam, index=0)

                    lege_summary_rollen(beginnummer, posities, vlg, aantal_per_rol, wikkel, prefix,
                                                             postfix, rol_nummer, veelvoud).to_csv(sum_pad_naam, index=0)
                    count += 1

            # voeg rest posix paden toe aan gemaakte posix paden
            if hoeveelheid_rest_rollen != 0:
                new_posix_lijst = gemaakte_posix_paden + rest_gemaakte_posix_paden
                new_summary_lijst = summary_pad_namen_posix + rest_summary_pad_namen_posix
                print(f'nieuwe lijsg ={new_posix_lijst}')

            else:
                new_posix_lijst = gemaakte_posix_paden
                new_summary_lijst = summary_pad_namen_posix



            print(f'posix_paden {gemaakte_posix_paden}')
            print(f'lengte map posix_paden {len(gemaakte_posix_paden)}')


            aantal_rollen = len(beginlijst)
            print(f'aantal rollen {aantal_rollen} + rest rollen: {hoeveelheid_rest_rollen//aantal_per_rol}')
            rest_rollen_toevoegen = hoeveelheid_rest_rollen//aantal_per_rol
            combinaties = (aantal_rollen + rest_rollen_toevoegen) // mes
            print(f'combinaties = {combinaties}')

            csv_files_in_tmp = [x for x in os.listdir(path) if x.endswith(".csv")]

            summary_csv_files_in_tmp = [x for x in os.listdir(pad_sum) if x.endswith(".csv")]

            # print(csv_files_in_tmp)
            sorted_files = sorted(csv_files_in_tmp)
            sorted_sum_files = sorted(summary_csv_files_in_tmp)

            print(f'sortedfiles {sorted_files}')

            combinatie_binnen_mes_posix = []
            combinatie_binnen_mes = []

            summary_combinatie_files = []

            begin = 0
            eind = mes
            for combi in range(combinaties):
                print(begin, eind)

                combinatie_binnen_mes.append(sorted_files[begin:eind])
                combinatie_binnen_mes_posix.append(new_posix_lijst[begin:eind])

                summary_combinatie_files.append(new_summary_lijst[begin:eind])


                begin += mes
                eind += mes

            # kan ik de summary in dezelfde forloop laten meelopen:?
            teller = 0

            for lijst in combinatie_binnen_mes_posix:
                print(f'{mes} == mes')
                print(lijst)
                print(type(mes_wik.lees_per_lijst(lijst, mes)))

                csv_naam = Path(path_vdp.joinpath(f'df_{teller:>{0}{4}}.csv'))
                print(f'csv naam {csv_naam}')

                mes_wik.lees_per_lijst(lijst, mes).to_csv(csv_naam, ";", index=0)

                teller += 1



            teller=0
            for lijst in summary_combinatie_files:
                print(f'{mes} == mes')
                print(lijst)
                print(type(mes_wik.lees_per_lijst(lijst, mes)))

                sum_csv_naam = Path(sum_map.joinpath(f'df_{teller:>{0}{4}}.csv'))
                print(f'sum_csv naam {sum_csv_naam}')

                mes_wik.lees_per_lijst(lijst, mes).to_csv(sum_csv_naam , ";", index=0)

                teller += 1







            df_csv_files_in_tmp = [x for x in os.listdir(path_vdp) if x.endswith(".csv")]
            sum_files_in_sum_map = [x for x in os.listdir(sum_map) if x.endswith(".csv")]

            sorted_df_files = sorted(df_csv_files_in_tmp)
            sorted_sum_df_files = sorted(sum_files_in_sum_map)


            mes_wik.stapel_df_baan(sorted_df_files, ordernummer,path_vdp,path_final)
            mes_wik.stapel_df_baan(sorted_sum_df_files, ordernummer,sum_map,naar_folder_pad,"Summary_")


            vdp_final_files_in_tmp = [vdp for vdp in path_final.glob("*.csv") if vdp.is_file()]

            sorted_csv_final_files = sorted(vdp_final_files_in_tmp)

            mes_wik.wikkel_n_baans_tc(sorted_csv_final_files, Y_waarde, inloop, mes, naar_folder_pad)






            # voorlopige in voor summary

            begin_nummer_lijst = [
                begin for begin in range(begin_nummer, begin_nummer + totaal_aantal - 1, aantal_per_rol)
            ]

            rol_nummer_lijst = [
                f"Rol {num:>{0}{3}}" for num in range(1, len(begin_nummer_lijst) + 1)
            ]

            # print(begin_nummer_lijst)
            begin_eind_nummer_lijst = [
                [begin, begin + aantal_per_rol - 1] for begin in begin_nummer_lijst
            ]
            # print(begin_eind_nummer_lijst)

            belijst = [
                [f"{begin:>{vlg}{posities}};{(begin + aantal_per_rol - 1):>{vlg}{posities}}"]
                for begin in begin_nummer_lijst
            ]

            sumlijst = [
                [
                    f"{prefix}{begin:>{vlg}{posities}}{postfix};{prefix}{(begin + aantal_per_rol - 1):>{vlg}{posities}}{postfix}"
                ]
                for begin in begin_nummer_lijst
            ]

            beg_eind_lijst_df = pd.DataFrame(sumlijst, dtype="str")

            beg_eind_lijst_df.to_csv(f"{naar_folder_pad}/{ordernummer}_sum.csv", index=0)

            keywargs = {
                        "Ordernummer: ": ordernummer,
                        "Aantal VDP's": 1,
                        "Totaal aantal ": str(f'{totaal_aantal:,} etiketten').replace(",", "."),
                        "begin_nummer": f'{begin_nummer:>{0}{posities}}',
                        "eind_nummer": f'{begin_nummer + totaal_aantal - 1:>{0}{posities}}',
                        'Aantal Rollen': f'{aantal_rollen} rol(len) van {aantal_per_rol}',
                        # "Rol_nummers": f'Rol_{begin_rolnummer + 1} t/m Rol_{begin_rolnummer + aantal_rollen}',
                        "Mes ": mes,
                        # 'Mes x combinaties ': f'{mes} van {combinaties} banen',
                        "Wikkel": f'{wikkel + 3} etiketten',

                        'Inloop en uitloop': f'{Y_waarde} x 10 sheets =({inloop})',
                        'De files staan hier': naar_folder_pad,
                        "Opmerkingen": opmerkingen
                        }

            # todo output in html
            html_sum_form_writer(naar_folder_pad,titel=f'summary_{ordernummer}', **keywargs)  # **values voor alle ingegeven values

            #__________rechtstreeks uit projekt lijstbewerkingen


            #
            #
            #
            # mes_wik.stapel_df_baan(opgebroken_lijst, ordernummer)

            # clean all
    window.close()


if __name__ == '__main__':
    main()