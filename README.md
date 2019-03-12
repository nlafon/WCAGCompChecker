# WCAGCompChecker
This is our HCI project to check websites for WCAG compliance. [The guidelines for WCAG can be found here][wcag].

# Purpose
The purpose of this project is to set up a website where a user can enter a URL to check it for the compliance of the Web Content Accessibility Guidelines.

# What is the WCAG?
The Web Content Accessibility Guidelines is a set of guidelines intended to make everything on the internet useable and accessible to all people. If there are people with some disabilities, by these guidelines, all websites are required to make them accomodate them.

# How to use
After a user enters a URL, the WCAGCompChecker will run through that site and check for violations of the WCAG. After thst, the user will be taken to a new page that will tell them which of the guidelines they violated, if any. This project will not show the webpage from the URL itself, but it will only show which things it violated.

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

To use the program go to: **http://127.0.0.1:8000/home** in your browser


[pipenv]: <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>
[wcag]: <https://www.w3.org/WAI/standards-guidelines/wcag/>

