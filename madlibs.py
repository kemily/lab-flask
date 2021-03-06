from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    """Save game output to user."""
    yes_answer = request.args.get("yes")
    no_answer = request.args.get("no")

    if no_answer:
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

    return render_template("compliment.html", 
            yes=yes_answer, no=no_answer)    



@app.route('/madlib')
def show_madlib():
    """Save game output to user."""
    isperson = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    animal = request.args.get("animal")

    feeling = request.args.getlist("feeling")


    if feeling:
        feelings = feeling
    else: 
        feelings = []

    return render_template(choice(["madlib1.html","madlib2.html"]), 
            person=isperson, color=color,
            noun=noun, adjective=adjective, animal=animal,
            feelings = feelings) 


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
