import pathlib

def file_rename(*, name=None, count=1, extension_start=None, extension_end=None, rang=[0]):
    p = pathlib.Path(pathlib.Path.cwd() / 'file')
    pn = 1
    for i in p.iterdir():
        if i.is_file():
            old_name = i.name.split('.')
            if not extension_start or old_name[1] == extension_start:
                new_name = ''
                if len(rang) == 2:
                    if rang[0] < rang[1] <= len(old_name[0]):
                        new_name += old_name[0][rang[0]:rang[1]]
                    elif rang[0] < len(old_name[0]):
                        new_name += old_name[0][rang[0]]
                if name:
                    new_name += name
                number_name = str(pn)
                if len(number_name) < count:
                    for _ in range(len(number_name) - count):
                        number_name = '0' + number_name
                new_name += number_name
                pn += 1
                if extension_end:
                    new_name += f'.{extension_end}'
                else:
                    new_name += f'.{old_name[1]}'
                i.rename(pathlib.Path.cwd() / 'file' / new_name)


