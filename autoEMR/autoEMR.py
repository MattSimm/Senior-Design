# Program entry.

import MySQLdb

database = new DbEMR()
controller = new Controller(database)
UI = new UI(controller)
UI.run()

# Viewer:
class UI:
	def __init__(self,controller):
		self.controller = controller
		self.p_info = {}
		self.d_mess = {}
		self.p_id = 0

	def run():
		# Establish the Userinterface, provide buttons, display infor...
		# Feel free to add any variable you need, but please only call method provided by controller.
		# When user click a botton, call controller method to get information you want
		# Currently, modules under controller is not implemented, so it return nothing
		# Assume a return value of controller for UI testing
		# If more information needed, you can assume controller has more method and 
		# assume a return value for that method for testing. Also please tell me what do you need. 


# Controller:
class Controller:
	def __init__(self, database):
		self.database = database
		self.paragraph = []
		self.p_info = {}
		self.d_mess = {}

	def find_p(first_name):
		# Find a already exsisting patient with his first name.
		# Call find_patient method of DbEMR to get back all patients 
		# with same first name, following things are returned:
		# first name, last name, birthday is returned to UI for display
		return database.find_patient(first_name)

	def get_p_from_conversation():
		# Start the speech recognition process and get back a list of string.
		# Each string in the list is a sentence.
		# The list is a track of whole conversation.
		# Call method to parse conversation and get back personal information
		# A dictionary like {'first_name':'Mary','last_name':'Sue'} is returned.
		# Keep it and return it to UI for display.
		paragraph = make_para()
		p_info = pick_p_info(paragraph)
		return p_info

	def confirmed_p(p_id,confirmed_info):
		# Push the changes of that person to database
		# confirmed_info is a dictionay containing things to change or add.
		database.add_patient(p_id,confirmed_info)

	def get_d_from_conversation():
		# Start the speech recognition process and get back a list of string.
		# Each string in the list is a sentence.
		# The list is a track of whole conversation.
		# Call method to parse conversation and get back diagnose information
		# A dictionary like above is returned.
		# Keep it and return it to UI for display.
		# Diagnose message parse is difficult, do this part in second iteration.
		paragraph = make_para()
		d_mess = pick_d_mess(paragraph)
		return d_mess

	def confirmed_d(p_id,confirmed_info):
		# Push the changes of that person to database
		# confirmed_info is a dictionay containing things to change or add.
		database.add_diagnose(p_id,confirmed_info)



# Modules

class DbEMR:
	def __init__(self):
		self.db = MySQLdb.connect("den1.mysql5.gear.host","seniordesign",
								  "00000!","seniordesign")
		self.cursor = db.cursor()

	def find_patient(first_name):

	def add_patient(p_id,confirmed_info):

	def add_diagnose(p_id,confirmed_info):


##Personal Information section###########################
# Parse personal information from whole conversation.
# Para is an array of string, each string is a sentence.
# Return a dictionary like {'first_name':'Mary','last_name':'Sue'}
# Minimum information to return: first name, last name, gender, birthdate
# Maybe design more information to return later.
def pick_p_info(para):


#########################################################


##Diagnose Message section###############################
# Parse diagnose message from whole conversation.
# Para is an array of string, each string is a sentence.
# Working partern is not clear for now, implement in iteration 2
def pick_d_mess(para):


#########################################################

##Speech recognition#####################################
# Construct a paragraph with the sentences it catches
def make_para():

# Catch a sentence and convert it into string.
def convert_sentence():

#########################################################