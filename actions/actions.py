
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionGreetUser(Action):

#     def name(self) -> Text:
#         return "action_greet_user"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello How can I help you sir!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

ALLOWED_VEHICLE_CON=["used","brand new","new","old","Used Vehicles","Brand New Vehicles"]
ALLOWED_FUEL_TYPES = ["Petrol", "Diesel"]

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
     

## New Actions Added

class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_vehicle_form"

    def validate_vehicle_con(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `vehicle_con` value."""

        if slot_value.lower() not in ALLOWED_VEHICLE_CON:
            dispatcher.utter_message(text=f"We only accept : Used Vehicles/Brand New Vehicles.")
            return {"vehicle_con": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} car ")
        return {"vehicle_con": slot_value}

    def validate_fuel(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `fuel` value."""

        if slot_value not in ALLOWED_FUEL_TYPES:
            dispatcher.utter_message(text=f"I don't recognize fuel type. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"fuel": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} car.")
        return {"fuel": slot_value}
