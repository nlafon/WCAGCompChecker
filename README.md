# WCAGCompChecker
This is our HCI project to check websites for WCAG compliance. [The guidelines for WCAG can be found here][wcag].
# How to run
This project was developed in Python 3.7.2. All the dependencies can easily be installed using [pipenv][pipenv]. After installing pipenv, install the dependencies and activate the shell using:
```sh
python -m pipenv install
python -m pipenv shell
```

To run this project, navigate to "\WCAGCompChecker\wcag_checker" and run:
```sh
python manage.py runserver
```


[pipenv]: <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>
[wcag]: <https://www.w3.org/WAI/standards-guidelines/wcag/>