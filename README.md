# Command Line Diary

This is a command line interface (CLI) application designed to function as a diary, inspired by the futuristic command line apps seen in sci-fi movies. 
The project was initiated by the desire to work with CLI applications and gain experience in building one. 
This is the first CLI application developed by me.

The Command Line Diary allows you to conveniently write and manage your personal diary entries directly from your terminal. It leverages the following technologies:

- **Typer**: A powerful library for building CLI applications with ease.
- **Rich**: A Python library for rich text and beautiful formatting in the terminal.
- **SQLAlchemy**: An Object-Relational Mapping (ORM) library for interacting with databases.


## Installation

To use the Command Line Diary, please follow these steps:

1.Download the diary.py file from the repository shivasharanappaBiradar2645/simple_cli_diary.

2.Install the required dependencies: rich, sqlalchemy, and typer. You can install them using pip by running the following command:
`pip install rich sqlalchemy typer`

3.Once the dependencies are installed, you can run the diary.py file using the following command:
`python diary.py [command]`


##Commands
- **add**   : Provide a console to type your entry and than saves it.
- **all**   : Returns all the saved entries.
- **month** : Returns entries of a particular month.
- **day**   : Returns entry of a particular date.


## License

This project is licensed under the [MIT License](LICENSE).


## Acknowledgments

The development of this project was made possible thanks to the following libraries and resources:

- [Typer](https://github.com/tiangolo/typer)
- [Rich](https://github.com/willmcgugan/rich)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)

Happy diary writing!
