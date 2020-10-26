from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from emailClassFile import emailClass

citiesFilePath = r"E:\zOther\Upgrad AI ML\Programs\34. Chatbot Case Study\Rasa_Chatbot_CaseStudy\cities.txt"

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		#dispatcher.utter_message("Inside the restaurant search")
		
		config={ "user_key":"e556cab022363342ab67be69f38554f7"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"

		dispatcher.utter_message("-----"+response)
		return [SlotSet('emailContent',response)]
		
def check_if_string_in_file(string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    cityNames = open(citiesFilePath, "r")
	# Read all lines in the file one by one
    for line in cityNames:
        line = line.lower()
        string_to_search = string_to_search.lower()
		# For each line, check if line contains the string
        if string_to_search in line:
            return True
    return False

# Check if the detected location belong to Tier1 or Tier2 dataset
class CheckLocation(Action):
    def name(self):
        return 'act_checkLocation'

    def run(self, dispatcher, tracker, domain):              
        loc = tracker.get_slot('location')
        #dispatcher.utter_message("Check Location Message..!!!")
        check = check_if_string_in_file(loc)
        if check:
            return [SlotSet('slt_checkOp',True)]
        else:
            return [SlotSet('slt_checkOp',False)]

# Class to detect location after utter_ask_location
class detectLocation(Action):
	def name(self):
		return 'act_detectLocation'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('detectLocation')
		check_loc = tracker.get_slot('confirmLocation')

		if len(loc) >= 3 and check_loc == "loc_Yes":
			return [SlotSet('location',loc)]
		else:
			return [SlotSet('confirmLocation',check_loc)]
			#dispatcher.utter_message("Please restart the session, thank you..!!!")

class sendEmail(Action):
	def name(self):
		return 'act_sendEmail'

	def run(self, dispatcher, tracker, domain):
		mail_content = tracker.get_slot('emailContent')
		receiverAddress = "kalpesh94552@gmail.com"

		em = emailClass()
		em.sendEmailFun(mail_content,receiverAddress)
		dispatcher.utter_message("Mail Sent..!!!")

		return [SlotSet('emailContent',mail_content)]