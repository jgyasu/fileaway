from termcolor import colored


def header():
    header = """
  _____  _  _                                      
 |  ___|(_)| |  ___   __ _ __      __ __ _  _   _  
 | |_   | || | / _ \ / _` |\ \ /\ / // _` || | | | 
 |  _|  | || ||  __/| (_| | \ V  V /| (_| || |_| | 
 |_|    |_||_| \___| \__,_|  \_/\_/  \__,_| \__, | 
                                            |___/                             
                                                         
A nifty tool to sort your messy folders [MIT License]
            """
    print(colored(header, 'yellow'))
    return 0