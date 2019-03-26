# Introduction
This is our HCI project to check websites for WCAG compliance. [The guidelines for WCAG can be found here][wcag].

## Purpose
The purpose of this project is to set up a website where a user can enter a URL to check it for the compliance of the Web Content Accessibility Guidelines. Several websites do not follow the guidelines, which makes it difficult for several people with disabilities to use them. 

## What is the WCAG?
The Web Content Accessibility Guidelines is a set of guidelines intended to make everything on the internet useable and accessible to all people. If there are people with some disabilities, by these guidelines, all websites are required to make them accomodate them.

## Solution Overview
After a user enters a URL, the WCAGCompChecker will run through that site and check for violations of the WCAG. After thst, the user will be taken to a new page that will tell them which of the guidelines they violated, if any. This project will not show the webpage from the URL itself, but it will only show which things it violated. It also gives suggestions on how to fix violations, such as providing alternate text.

## References
The main reference for this project is the Web Compliance Accessibilty Guidelines.

# User Description
The site is intended to be usable by all people. A good use for the website would be for big companies so that their website can be used by all people, or professors so that no student feels disadvantaged.

## User/ Market Demographics
All people can use this website. It would be useful for all people to scan different URLs to make sure that people who have accessibilty troubles are also taken care of. Additionally, people who do have disabilities can use the website to check for violations, and then have the makers of the website edit it to accommodate them as well.

## User Personas
This website is intended to be very easy for all types of people to use. They will only need basic knowledge of copy and paste. Everything is very straight forward to make the human-computer interaction as smooth and easy as possible.

## User Environment
The user can use the website as little as one time to check one site, or several times to check different websites. They could even constantly check the same websites to ensure that the site is always in compliance to the guidelines.

## Key User Needs
Ideally, the user should have some knowledge of the WCAG, just so that they know exactly what this compliance checker does. However, even if they do not, the website would still help them get some sort of idea. Our website also links to the WCAG, so users can easily access and become familiar with it.

## Competition
There are some other compliance checkers. However, this one is different because the main goal is to have it show exactly where the given website violated the guidelines, as well as provide suggestions for the constructors of the website on how to fix the violations.

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

# High Priority TODO:
- Make alt txt violation src image attribute URL not relative to site being tested. Or add the image url to the return dict. (jinja can’t render images without complete URL and adding code to the template to do it is a bad idea)
- Fix red rectangle on results page. It's an image with constant size and needs to be more dynamic as the results could be any length.
- Make our own site compliant with WCAG.
- Make results view render pretty.

[pipenv]: <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>
[wcag]: <https://www.w3.org/WAI/standards-guidelines/wcag/>

