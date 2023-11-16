import os, sys

from arg_parser import parse_arguments
from wiktionary import get_wiktionary_data
from utils import write_temp, save
from languages import L, modifyLanguagesList

if __name__ == "__main__":
    args = parse_arguments()

    entry = args.entry

    if args.entry == None and not args.language:
        entry = input('Entry: ')

    if args.all == args.one:
        args.specific = True

    if args.language:
        modifyLanguagesList()
        sys.exit()

    language = 'en'  # Not editable for now.
    


    H, C = get_wiktionary_data(language, entry)

    if args.all:
        with open('./wktnTemp.txt', 'w+', newline='') as data:
            write_temp(data, H, C)

            # Moves the read/write cursor to the beginning of the file
            data.seek(0)

            output = ""
            for line in data:
                output += line
            print(output)

        save(output)

        os.remove('./wktnTemp.txt')

    if args.specific:
        with open('./wktnTemp.txt', 'w+', newline='') as data:
            write_temp(data, H, C, L)

            data.seek(0)

            output = ''
            for line in data:
                if all(l.upper() in line for l in line) or any(y in line for y in L):
                    output += line

            print(output)

        save(output)

        os.remove('./wktnTemp.txt')

    if args.one:
        L = []
        selectedLanguage = input('Language: ').capitalize()
        L.append(selectedLanguage)
        
        with open('./wktnTemp.txt', 'w+', newline='') as data:
            write_temp(data, H, C, L)
            data.seek(0)

            output = ''
            for line in data:
                if all(l.upper() in line for l in line) or any(y in line for y in L):
                    output += line

            print(output)

        save(output)

        os.remove('./wktnTemp.txt')