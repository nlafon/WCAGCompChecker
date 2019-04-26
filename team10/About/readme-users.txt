To run this project, activate the python virtual environment using the following command in the “Build” directory:
py -3.7 -m pipenv shell
Then navigate to "Build\WCAGCompChecker\wcag_checker" in your terminal and run:
python manage.py runserver
After this, the site can be viewed in your browser at: http://127.0.0.1:8000/home
To use the software, copy the web URL which you wish to check for compliance and enter it in input field of the home page.
Click the “Check WCAG Compliance” button and the checker will scan the site for violations and forward the user to the results page for review.
