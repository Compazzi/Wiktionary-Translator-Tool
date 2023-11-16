import argparse

def parse_arguments():
    # ...
    parser = argparse.ArgumentParser(description='This program translates a given word in the terminal by parsing Wiktionary.')
    parser.add_argument('-a', '--all', help='Prints the result of all translations obtained by parsing Wiktionary', action='store_true')
    parser.add_argument('entry', type=str, nargs='?', help='The word to be translated')
    parser.add_argument('-s', '--specific', help='Prints the result obtained by parsing Wiktionary, but only for the specified languages (defined in-program).', action='store_true')
    parser.add_argument('-o', '--one', help='Prints the result obtained by parsing Wiktionary, but only for one chosen language.', action='store_true')
    parser.add_argument('-l', '--language', help='Allows you to view and edit the list of languages to which entries will be translated.', action='store_true')

    return parser.parse_args()
