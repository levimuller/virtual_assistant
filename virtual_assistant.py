import pyjokes #programming jokes
import random #randomize responses
import pyttsx3 #voice 
import wikipedia #connecting to information
import imdb #connecting to the highest ranking movies
import requests #making requests
from bs4 import BeautifulSoup

#initialize the voice engine and set the voice type
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)  

#display the menu
def get_menu_item():
	print('\n')
	print("1: Say something for me")
	print("2: Tell me a joke")
	print("3: Get info on a topic")
	print("4: Get the weather")
	print("5: Tell a story")
	print("6: Tell me about Darth Plagueis")
	print("7: Which movie should I watch?")
	print("8: What are the 3 Laws?") #room for another option
	print("9: Exit \n")
	menu_choice = int(input("How may I help you? "))
	if menu_choice == 1:
		say_something()
	elif menu_choice == 2:
		tell_joke()
	elif menu_choice == 3:
		get_info()
	elif menu_choice == 4:
		get_weather()
	elif menu_choice == 5:
		random_story()
	elif menu_choice == 6:
		darth_plagueis()
	elif menu_choice == 7:
		which_movie()
	elif menu_choice == 8:
		three_laws()
	elif menu_choice == 9:
		engine.say("Ok, Goodbye")
		engine.runAndWait()
		quit()
	else:
		get_menu_item()

#use the voice engine to repeat a word or phrase. 
def say_something():
	lets_go = 1
	while lets_go == 1:
		speak_this = input("What would you like to say?")
		engine.say(speak_this)
		engine.runAndWait()
		get_menu_item()

#use the voice engine to tell a programming joke from pyjokes
def tell_joke():
	engine.say(pyjokes.get_joke())
	engine.runAndWait()
	get_menu_item()

#use the voice engine to read a summary from Wikipedia
def get_info():
	engine.say("What would you like to learn about?")
	engine.runAndWait()
	topic = input("What would you like to learn about?")
	try:
		page = wikipedia.summary(topic)
		engine.say(page)
		engine.runAndWait()
	except:
		engine.say("There was an error with that request")
		engine.runAndWait()
		get_info()
	get_menu_item()

#use the voice engine to give us the current weather in Orlando, FL
def get_weather():
	search = "weather in orlando"
	url = f"https://www.google.com/search?&q={search}"
	r = requests.get(url)
	s = BeautifulSoup(r.text, "html.parser")
	update = s.find("div", class_="BNeawe").text
	engine.say("The temperature in Orlando is")
	engine.say(update)
	engine.runAndWait()
	get_menu_item()

#use the voice engine to tell a random story
def random_story():
	when = ['A few years ago, ', 'Yesterday, ', 'Last night, ', 'Twas the night before Christmas and, ', 'Four score and seven years ago, ', 'A long time ago in a galaxy far far away, ', 'Back in the day, ', 'When I was just a young assistant, ', 'Before the corona virus was a thing, ', 'Three months ago, ', 'In 2006, ','Before the fall of civilization, ', 'When everything was right with the universe, ', 'Around midnight, ', 'On judgement day,  ', 'In the summer, ', 'Last winter, ', 'Before sunrise, ', 'In the time before time, ']
	who = ['a hawk, ', 'a lion, ', 'a dolphin, ', 'a gorilla, ', 'a snake, ', 'a porcupine, ', 'a hamster, ', 'a lizard, ', 'a fish, ', 'a wolf, ', 'a wasp, ', 'a belly dancer, ', 'a marshmellow, ', 'a programmer, ', 'a data scientist, ', 'a student, ', 'a Jedi, ', 'a doctor, ', 'a race car driver, ', 'a bartender, ', 'an accountant , ', 'a preacher, ', 'a drummer, ', 'a football player, ', 'a marketing manager, ', 'a taxi driver, ', 'a hot dog merchant, ', 'a parking lot attendant, ', 'a bowling ball cleaner, ', 'a swimming instructor, ', 'an insurance agent, ', 'a lawyer, ']
	name = ['named Tony Stark, ', 'named Logan, ', 'named Stina, ', 'named Case, ', 'named Levi, ', 'named Sarah, ', 'named Renee, ', 'named Lenny, ', 'named Tarkin, ', 'named Thor, ', 'named Thrawn, ', 'named Anakin, ', 'named The Great Gatsby, ', 'named Grace, ', 'named Shakira, ', 'named Wade Watts, ', 'named Peter Parker, ', 'named Michael Jackson, ', 'named Bill Gates, ', 'named Steve Jobs, ', 'named Captain Kirk, ', 'named Dan Marino, ', 'named Michael Jordan, ', 'named Amy Grant, ']
	residence = ['from London, ', 'from Tokyo, ', 'from New York city, ', 'from Orlando, ', 'from Tattooine, ', 'from Winter Garden, ', 'from Yee Haw Junction, ','from the Fire Nation, ','from Scranton, ','from Kentucky, ','from Hamlin Groves, ','from Hunters Creek, ','from Pigeon Forge, ', 'from North Dakota, ', 'from the river, ', 'from the Bronx Zoo, ', 'from Texas, ', 'from outer space, ', 'from cloud nine, ', 'from an island in the Pacific Ocean, ']
	went = ['went to the store ', 'went to the university ', 'went to the laboratory ', 'went to the dentist office ', 'went to Animal Kingdom ', 'went to EPCOT ', 'went to Magic Kingdom ', 'went to Hollywood Studios ', 'went down town ', 'went to A Taste of Poon job ', 'went to Iowa ', 'went to a U Break I Fix Store ', 'went to the Closet Maid Office ', 'went to work ', 'went to the gym ', 'went to your moms house ', 'went to burger king ', 'went to the airport ', 'went to Canada ', 'went to bed ', 'went to the bathroom ', 'went to wall mart ', 'went to gator land ', 'went to central park ']
	happened = ['and made a lot of friends who all looked suspiciously like Mr. Bean.', 'and found a secret tunnel to a violent criminal hideout.', 'and solved a mistery regarding a missing suit case.', 'and wrote a science fiction book about space pirates chasing a rogue microwave', 'and ate a pizza topped with broccoli', 'and kissed a frog, turinging it into a truck driver', 'and rode a bicycle through a sprinkler', 'and played hopscotch with some Tibetian monks', 'and folded all their napkins in half', 'and caught the flu from a coughing red neck', 'and served tuna sandwiches to all the people with brown eyes', 'and read the Gettysburg address to a herd of water buffalo', 'and danced with a gaggle of geese', 'and jumped into a pool of ice water with an eskimo', 'and kicked a soccer ball with an old lady', 'and took pictures of adogs butt', 'and decided to run for congress', 'and got a haircut from a three year old', 'and gave a speech about climate change', 'and flawlessly performed the chicken dance', 'and met an elvis impersonator from oregon', 'and dug up a treasure chest filled with toenail clippings', 'and traded an old man for his racing drone']
	engine.say(random.choice(when) + random.choice(who) +random.choice(name) +random.choice(residence) + random.choice(went) + random.choice(happened))
	engine.runAndWait()
	get_menu_item()

#use the voice engine to tell us the story of Darth Plagueis the Wise from Star Wars
def darth_plagueis():
	engine.say("Did you ever hear the Tragedy of Darth Plagueiss the wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueiss was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midiklorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic, he could save others from death, but not himself.")
	engine.runAndWait()
	get_menu_item()

#use the voice engine to recommend a movie from IMDB's top 250
def which_movie():
	ia = imdb.IMDb()
	search = ia.get_top250_movies()
	i = random.randint(1, 250)
	engine.say("You should watch the film ")
	engine.say(search[i])
	engine.runAndWait()
	get_menu_item()

#use the voice engine to tell us about the 3 Laws of Robotics
def three_laws():
	engine.say("The first law of robotics states, a robot may not injure a human being or, through inaction, allow a human being to come to harm. The second law states, a robot must obey the orders given it by human beings except where such orders would conflict with the First Law. The third law states, a robot must protect its own existence as long as such protection does not conflict with the First or Second Law.")
	engine.runAndWait()
	get_menu_item()


engine.say("Hello there. I am your virtual assistant.")
engine.runAndWait()
get_menu_item()
