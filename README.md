MacEwan Hackathon Project
MaCS Hackathon 2022 BugBot

README
BugBot is a general multi purpose discord bot used to call commands to do many different things. Commands include memes, minigames, and a personality quiz.

BugBot was written in python, using a combination of different modules.

List of commands:
/hangman - A command used to start a quick game of hangman. The user is allowed no more than 7 incorrect guesses and they try to guess a word imported from a list of words that contains 848 words. Each wrong guess adds a body part to the gallows. Correct and incorrect guesses are both displayed for the user to see.
/nhlscores - A command used to get the most up to date NHL scores in terms of the website used from the internet and posts the scores for that day.
/quiz - A command that brings up a personality based quiz using a point system that will assign the individual a role at the end of the test
/madlib - Command that prompts the user to enter various words; displays a story once all inputs have been taken. If at any time in the middle of entering inputs, the user can quit by simply entering ‘quit’ rather than what is currently being prompted for.
/sus - Displays a crewmate shaped emoji from the hit game Among Us.
/lenny - Displays a lenny face.
/happy - Displays a text-based happy face
/hap - Displays a text-based happier face.
/shrug - Displays a shrug
/watching - Displays a text based emoji of a face peeking around the corner of a wall.
/look - Displays combination of emojis, showing a face.
/studying - Displays a student studying in peak performance
/cs - Displays a gif of a monkey attacthed to an oxygen tank.
/cope - Displays a gif of a frog, crying, and attached to an oxygen tank.
/over - Displays a gif of kermit falling off a building
/ok - Displays a gif of a cat with tears in its eyes.
/bonk - Displays a gif of a dog hitting another dog over the head with a wooden bat.



List of defined functions:
export_csv():
Converts table from html code to a list of its values then converts to csv file.
    csv file header: 
    ,Date,Visitor,G,Home,G.1,Unnamed: 5,Att.,LOG,Notes
    csv file line 1: 
    0,2022-10-07,San Jose Sharks,1.0,Nashville Predators,4.0,,16648.0,2:43,"at
    (Prague, CZ)"

load_scores(file):
   Takes a file as a parameter, reads csv file line for line and stores
    the date as a key and value a list of information of the game:
    first team name, first team score, second team name, second team score
    If there are no updated scores and the fields are empty for the scores 
    it stops storing information.
    Returns scores as a dictionary.
    ex. '2022-10-11': ['Vegas Golden Knights', '4', 
                                'Los Angeles Kings', '3', 
                                'Tampa Bay Lightning', '1', 
                                'New York Rangers', '3']

get_current_date():
   Gets current date with datetime.now(), formats it and returns it as a 
    string.
    ex. '2022-10-11'

get_recent_scores(scores):
   Takes scores dictionary as follows:
    dictionary : '2022-10-11': ['Vegas Golden Knights', '4', 
                                             'Los Angeles Kings', '3', 
                                             'Tampa Bay Lightning', '1', 
                                             'New York Rangers', '3']
    and converts the dictionary to a list and gets the last key in the
    dictionary (the most up to date score date). Uses this last key and gets the
    list of scores (value) with that date (key) and returns it as a list.

get_word(words):
   Takes a list of words as a parameter and randomly returns one word from 
    that list.

possible_gallows():
   Returns a tuple of all possible gallows.

SETUP
Insert the token provided  

CONTACT
Start here

NOTICE
Start here


