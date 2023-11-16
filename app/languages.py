import pickle, os

actualPath = os.path.dirname(os.path.abspath(__file__))
projectPath = os.path.dirname(actualPath)
filePath = os.path.join(projectPath, 'data', 'languagesList.pkl')

try:
    with open(filePath, 'rb') as file:
        L = pickle.load(file)
except FileNotFoundError:
    L = ['German','Greek', 'Portuguese']

def modifyLanguagesList():
    global L
    while True:
        option = input('Choose an option (0. Display list; 1. Add; 2. Remove): ')
        if option == '0':
            print('\n', L, '\n')
        if option == '1':
            language = input('\nEnter the language (in English): ').capitalize()
            L.append(language)
            L = sorted(L)
            with open(filePath, 'wb') as file:
                pickle.dump(L, file)
        if option == '2':
            index = input('\nIndex of the to be removed (starting at 0): ')
            del L[int(index)]
            with open(filePath, 'wb') as file:
                pickle.dump(L, file)
        if option == '':
            break
