from termcolor import colored


def header():
    header = """
    ______                             _               
   / ____/___  _________ _____ _____  (_)_______  _____
  / /_  / __ \/ ___/ __ `/ __ `/ __ \/ / ___/ _ \/ ___/
 / __/ / /_/ / /  / /_/ / /_/ / / / / (__  )  __/ /    
/_/    \____/_/   \__, /\__,_/_/ /_/_/____/\___/_/     
                 /____/                                
                                     
A nifty tool to sort your messy folders [MIT License]
            """
    print(colored(header, 'yellow'))
    return 0