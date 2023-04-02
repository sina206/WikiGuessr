import wikipedia
import random
import pycountry
import re
from flask import Flask, render_template, request

app = Flask(__name__)

# list of random countries
countries = []
for country in pycountry.countries:
    if hasattr(country, "official_name"):
        if any(not c.isalnum() for c in country.name):
            countries.append(country.name)

# choose a random country
randomCountry = random.choice(countries)
page = wikipedia.page(randomCountry)
title = page.title
sentences = page.content.split(". ")
givenSentences = []
guesses = 5
points = 0

def play_game():
    print(randomCountry)
    global guesses, points, givenSentences
    answer = request.form.get("answer")
    if answer:
        if answer.lower() == title.lower():
            points += guesses*2
            result = ("You guessed correctly! The answer is indeed " + title)
        else:
            random_sentence = random.choice(sentences)
            # Replace matching words with asterisks
            for word in re.findall(r'\w+', title):
                if word.lower() in random_sentence.lower():
                    random_sentence = random_sentence.replace(word, "*" * len(word))
            givenSentences.append(random_sentence)
            result = ("Incorrect! Try again with another sentence:")
            guesses -= 1
            if guesses == 0:
                result = ("Sorry, you're out of guesses! The answer was: " + title)
    else:
        result = ("")
    if guesses == 0:
        result = ("Sorry, you're out of guesses! The answer was: " + title)
    return (title, givenSentences, result, points, guesses)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    global title, givenSentences, sentences, randomCountry, guesses, points
    if request.method == 'GET':
        # add this block to show a random sentence when the page is first loaded
        #if not givenSentences:
        random_sentence = random.choice(sentences)
        givenSentences.append(random_sentence)
        return render_template('game.html', title=title, givenSentences=givenSentences, result="", points=points, guesses=guesses)
    elif request.method == 'POST':
        title, givenSentences, result, points, guesses = play_game()
        if guesses == 0:
            # Choose a new random country when the game is over
            randomCountry = random.choice(countries)
            page = wikipedia.page(randomCountry)
            title = page.title
            sentences = page.content.split(". ")
            givenSentences = []
            random_sentence = random.choice(sentences)
            for word in re.findall(r'\w+', title):
                if word.lower() in random_sentence.lower():
                    random_sentence = random_sentence.replace(word, "*" * len(word))
            givenSentences.append(random_sentence)

            guesses = 5
            points = 0

            render_template('game.html', title=title, givenSentences=givenSentences, result=result, points=points, guesses=guesses)
            return render_template("game_over.html")



        elif (result == ("You guessed correctly! The answer is indeed " + title)):
            print("yes")
            randomCountry = random.choice(countries)
            page = wikipedia.page(randomCountry)
            title = page.title
            sentences = page.content.split(". ")
            givenSentences = []
            random_sentence = random.choice(sentences)
            for word in re.findall(r'\w+', title):
                if word.lower() in random_sentence.lower():
                    random_sentence = random_sentence.replace(word, "*" * len(word))
            givenSentences.append(random_sentence)

            points += (guesses)
            guesses = 5
        return render_template('game.html', title=title, givenSentences=givenSentences, result=result, points=points, guesses=guesses)


@app.route('/enter_name')
def enter_name():
    return render_template('enter_name.html')


@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/game_over')
def game_over():
    return render_template('game_over.html')

@app.route('/pick_a_player')
def pick_a_player():
    return render_template('pick_a_player.html')




if __name__ == '__main__':
    app.run(debug=True)
