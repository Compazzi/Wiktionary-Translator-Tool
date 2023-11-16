import os

def write_temp(file, headerList, contentList, L=''):
    i = 0
    length = len(contentList)
    while i < length:
        if i > 0:
            file.writelines('\n\n')
        file.writelines(f'{[i+1]} {headerList[i].upper()}')
        if L:
            noTransMsg = 'There is no translation for the selected language(s) yet.'
            L.append(noTransMsg)
            if not any(lang in contentList[i] for lang in L):
                file.writelines('\n' + noTransMsg)
            else:
                file.writelines(contentList[i])
        else:
            file.writelines(contentList[i])
        i += 1


def save(output):
    save = get_yes_no_input()
    if save:
        dir_path = input("Enter the directory where you want to save the file: ")
        file_name = input("Enter the name of the file: ")
        file_path = os.path.join(os.path.expanduser(dir_path), file_name)
        with open(f'{file_path}.txt', 'w') as f:
            f.write(output)
            

def get_yes_no_input():
    while True:
        user_input = input("\nDo you want to save the output in a Notepad? [Y/N]: \n[N] >>> ").lower()
        if user_input in ('y', 'yes'):
            return True
        elif user_input in ('n', 'no', ''):
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

