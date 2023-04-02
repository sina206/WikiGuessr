Wikipedia Country Guessing Game

This is a simple Flask application that allows users to play a game where they guess the name of a randomly selected country. The game presents the user with a series of partially obscured sentences from the country's Wikipedia page, and the user has a limited number of guesses to correctly guess the country.

Requirements

To run this application, you will need to have the following installed:

Python 3
Flask
Wikipedia
pycountry
Usage

To run the application, navigate to the directory containing the app.py file and run the command python app.py. The application should start running on http://localhost:5000.

Once the application is running, you can access it by visiting http://localhost:5000 in your web browser.

The application has the following routes:

/: the home page, which provides links to start the game or enter your name
/game: the page where the game is played
/enter_name: the page where the user can enter their name
/category: the page where the user can select a category for the game
/game_over: the page that is displayed when the game is over
/pick_a_player: the page where the user can select a player for the game
Files

This application consists of the following files:

app.py: the Flask application
templates/index.html: the HTML template for the home page
templates/game.html: the HTML template for the game page
templates/enter_name.html: the HTML template for the name entry page
templates/category.html: the HTML template for the category selection page
templates/game_over.html: the HTML template for the game over page
templates/pick_a_player.html: the HTML template for the player selection page
Notes

The game uses the Wikipedia API to fetch content for a randomly selected country, and the pycountry library to generate a list of countries to choose from.
The game presents a series of partially obscured sentences from the country's Wikipedia page, with words matching the country name replaced with asterisks.
The user has a limited number of guesses to correctly guess the country, and receives points for each guess remaining at the end of the game.
The application also includes pages for entering your name, selecting a category for the game, selecting a player for the game, and displaying the game over screen. However, these features are not fully implemented in the current version of the application.
