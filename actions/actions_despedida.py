from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
import time


TIEMPO_ENCUESTA = 86400

class ActionDeactivateFeedback(Action):
    def name(self) -> Text:
        return "action_deactivate_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        # Obtener valores de los slots
        var_mejora = tracker.get_slot("slot_mejora")
        var_satisfaccion = tracker.get_slot("slot_satisfaccion")
        var_recomendacion = tracker.get_slot("slot_recomendacion")

        # print(f"Valor del slot 'mejora': {var_mejora}")
        # print(f"Valor del slot 'satisfaccion': {var_satisfaccion}")
        # print(f"Valor del slot 'recomendacion': {var_recomendacion}")
        
        # Guardar timestamp actual y marcar feedback como no pendiente
        tiempo_actual = time.time()
        print("valor del slot ANTES",tracker.get_slot("slot_ultima_encuesta"))
        result = [
            SlotSet("slot_feedback_pendiente", False),
            SlotSet("slot_ultima_encuesta", tiempo_actual)
        ]
        
        print(f"🎯 RETURNING: {result}")
        return [result]


class ActionVerificarFeedback(Action):
    def name(self) -> Text:
        return "action_verificar_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        # print(tracker.get_slot("slot_recomendacion"))
        # print(tracker.get_slot("slot_ultima_encuesta"))
        print("ACTION VERIFICAARFEEDBACK",tracker.get_slot("slot_ultima_encuesta"))
        
        slot_ultima_encuesta = tracker.get_slot("slot_ultima_encuesta") or 0
        ahora = time.time()

        if ahora - slot_ultima_encuesta > TIEMPO_ENCUESTA:
            # Es momento de ofrecer feedback
            return [SlotSet("slot_feedback_pendiente", True)]
        else:
            # Aún no ofrecer feedback
            print("AUN no ofrecer feeback-------- - - - - -")
            return [SlotSet("slot_feedback_pendiente", False)]


