## Teenage Pregnancy API
This is the backend for a story map investigating causes for recent trends in US teen pregnancy,
created in the course of the block seminar `Trends and Concepts 2 - 2017/18` at the Hasso-Plattner Institute Potsdam.

### Team 3:
- Martin Gerstmaier
- Philipp Hager
- Sven Lehmann
- Hung Nguyen

## Installation
This is a (flask)[http://flask.pocoo.org/] written in python. It is to be noted that depending on the
server environment, each of the following commands has to be executed using sudo rights.
1. Open the terminal and navigate into the root folder of the project `cd tuk2-teen-pregnancy-api/`
2. Ensure you have [python3 and pip3](https://www.python.org/) installed. Check by running `python3 --version` and `pip3 --version`.
3. Make sure [pipenv](https://github.com/kennethreitz/pipenv) is installed, by running `pip3 install pipenv` and `pipenv --version`. For more information on pipenv lookup ["The Hitchhiker's Guide to Python"](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and ["How to manage your Python projects with Pipenv"](https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv).
4. Create a new virtual environment and install all project dependencies by running `pipenv install --python 3.6`. The argument `--python 3.6` is needed as this project relies upon python 3.6.
5. Make sure that you insert the address and login credentials for the database in the file `/env/config.py`.
6. To enter your virtual environment, run `pipenv shell`.
7. Start the server by running `python3 run.py`.
