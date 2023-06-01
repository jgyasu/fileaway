import os
import sys
from termcolor import colored
from down_path import down_path
from create_folders import create_folders
from move_files import move_files
from header import header


def main():

    #ASCII art header
    header()

    #choice for the preferred folder
    print(f"{colored('[1]', 'blue')} to sort the Downloads folder")
    print(f"{colored('[2]', 'blue')} to sort some other folder")
    print(f"{colored('[3]', 'blue')} to exit")
    print('\n')

    while True:
        choice = input(colored("Choice: ", 'blue'))
        if choice in ['1', '2', '3']:

            #exits the program
            if choice == '3':
                print('\n')
                sys.exit()

            #sorts the alternate folder
            elif choice == '2':
                print('\n')
                while True:
                    path = input(colored('Path of the folder: ', 'blue'))
                    if os.path.exists(path):
                        #path for the created folders
                        music, videos, pictures, documents, applications, archives, miscellaneous = create_folders(path)
                        move_files(path, music, videos, pictures, documents, applications, archives, miscellaneous)
                        print('\n')
                        break

            #sorts the downloads folder
            else:
                if not down_path():
                    print('Oops! Looks like your Downloads folder is not located at its default location')
                    while True:
                        path = input(colored('Enter your path manually: ', 'blue'))
                        if os.path.exists(path):
                            break
                else:
                    path = down_path()
                    #path for the created folders
                    music, videos, pictures, documents, applications, archives, miscellaneous = create_folders(path)
                    move_files(path, music, videos, pictures, documents, applications, archives, miscellaneous)
                    print('\n')
            break


if __name__ == "__main__":
    main()