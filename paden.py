""""builds paths"""

from pathlib import Path

wdir = Path.cwd()
pad_summary = wdir / "summary/"
file = "VDP_map"
print(pad_summary.is_dir())
pad_sum = wdir / "pad_sum"
sum_map = wdir/"Sum_map"

path_vdp = wdir / file
path_final =  wdir / "VDP_final"
path = wdir / "tmp"

list_of_files_to_clean = [pad_sum,path,sum_map,path_vdp, path_final]

# print(path_vdp)
# print(path_final)

def paden_maker(dirname):
    """"maak dirs"""
    path = Path(wdir / dirname)
    print(f'build:  {path}')
    return path.mkdir(parents=True, exist_ok=True)


def paden_vernietiger(dirname):
    """'verwijdert dirs dit ligt wat gevoeliger:) dan path.rmdir()"""
    pass


# # path = Path(pad_summary_2)
# path.parent.mkdir(parents=True, exist_ok=True)
#
# path.rmdir()
padenlijst = ["VDP_final","summary","tmp","VDP_map","pad_sum","Sum_map"]


for pad in padenlijst:
    paden_maker(pad)

# todo fix het paden verhaal
# todo maak in nieuw projekt.




def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()


for filenaam in list_of_files_to_clean:
    print(f'clean :  {filenaam}')
    cleaner(filenaam)