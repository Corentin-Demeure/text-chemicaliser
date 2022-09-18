#im too lazy to make it efficient and it works fine and its readable and easily editable anyway so why bother?

string = ['ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', 'b', 'ba', 'be', 'bh', 'bi', 'bk', 'br', 'c', 'ca', 'cd', 'ce', 'cf', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'db', 'ds', 'dy', 'er', 'es', 'eu', 'f', 'fe', 'fl', 'fm', 'fr', 'ga', 'gd', 'ge', 'h', 'he', 'hf', 'hg', 'ho', 'hs', 'i', 'in', 'ir', 'k', 'kr', 'la', 'li', 'lr', 'lu', 'lv', 'mc', 'md', 'mg', 'mn', 'mo', 'mt', 'n', 'na', 'nb', 'nd', 'ne', 'nh', 'ni', 'no', 'np', 'o', 'og', 'os', 'p', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt', 'pu', 'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', 's', 'sb', 'sc', 'se', 'sg', 'si', 'sm', 'sn', 'sr', 'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', 'ts', 'u', 'v', 'w', 'xe', 'y', 'yb', 'zn']
name_elements = []
try:
    name = input('text here:').lower()
except KeyboardInterrupt:
    name = '\n\nCLICK ON THE GREEN BUTTON NOT ON THE RED ONE'

last_char = 0

for char_i in range(len(name)):
    if char_i < len(name)-1:
        two_char = name[char_i] + name[char_i+1]
        if two_char in string:
            if last_char < 2:
                name_elements.append(f'[{two_char.capitalize()}]')
                last_char = 2
            else:
                last_char = 0
        elif name[char_i] in string:
            if last_char < 2:
                name_elements.append(f'[{name[char_i].capitalize()}]')
                last_char = 1
            else:
                last_char = 0
        elif last_char < 2:
                name_elements.append(name[char_i])
                last_char = 1
        else:
            last_char = 0
    elif name[char_i] in string:
        if last_char < 2:
            name_elements.append(f'[{name[char_i].capitalize()}]')
            last_char = 1
        else:
            last_char = 0
    elif last_char < 2:
        name_elements.append(name[char_i])
        last_char = 1
    else:
        last_char = 0

for item in name_elements:
    print(item,end='')