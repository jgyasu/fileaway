
# Fileaway

A nifty tool to sort your messy folders


## Screenshots

![App Screenshot](https://i.postimg.cc/15j1ZGJJ/image.png)


## Documentation

Fileaway is a fast and lightweight folder sorter. It is written entirely in Python and uses most of the modules that comes pre-installed with it.

It provides the user with two options, that are, to sort the downloads folder or to sort some other folder.

If the user chooses to sort the downloads folder, it automatically detects the path on the operating system and prompts to enter the path manually if it's not located at the default location.

Users can even choose the second option and directly provide the path to any other folder that they want to sort, any path provided passes through some checks to confirm if the destination actually exists on the system and if it doesn't then the user gets a reprompt.

After a path is selected, the program creates several subfolders inside the folder namely Music, Videos, Pictures, Documents, Application and Archives.

It then sorts all the files present in the parent folder into several different groups based on their extensions and moves them in the respective subfolders.


## Installation

Install Fileaway with pip

```bash
  pip install fileaway
```

## Usage

```bash
  fileaway
```
    
## Authors

- [@Jigyasu](https://www.github.com/jgyasu)


## Contributing

I have included support for all the popular file extensions but if you find one missing for you, feel free to contribute.

## Feedback

If you have any feedback or bugs to report, please reach out to me at jigyasu@outlook.in

## License

[MIT](https://choosealicense.com/licenses/mit/)

