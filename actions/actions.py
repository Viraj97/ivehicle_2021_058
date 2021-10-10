
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction



class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "action_choose_car_type"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["car_type"]
    
    def submit(self,
               dispatcher: "CollectingDispatcher",
               tracker: "Tracker",
               domain: "DomainDict",
    ) -> List[Dict]:
        car_type= tracker.get_slot('car_type')
        print(car_type)

        
        dispatcher.utter_message(text=f"You can check out this links to buy your {car_type} vehicle.\n 01. https://ikman.lk/en/ads?query={car_type} \n 02.https://riyasewana.com/search/{car_type}")
        return []
     


