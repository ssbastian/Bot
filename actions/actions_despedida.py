from typing import Dict, Text, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


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
        
        # Marcar feedback como completado (no pendiente y ya respondido)
        result = [
            SlotSet("slot_feedback_pendiente", False),
            SlotSet("slot_encuesta_completada", True)  # Nuevo slot para control permanente
        ]
        
        print(f"🎯 Encuesta completada. RETURNING: {result}")
        return result


class ActionVerificarFeedback(Action):
    def name(self) -> Text:
        return "action_verificar_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        # Verificar si la encuesta ya fue completada
        encuesta_completada = tracker.get_slot("slot_encuesta_completada")
        
        if encuesta_completada:
            # La encuesta ya fue respondida, no ofrecer de nuevo
            print("Encuesta ya completada anteriormente - No ofrecer feedback")
            return [SlotSet("slot_feedback_pendiente", False)]
        else:
            # Es la primera vez, ofrecer feedback
            print("Ofrecer encuesta por primera vez")
            return [SlotSet("slot_feedback_pendiente", True)]


class ActionResetEncuesta(Action):
    """Acción opcional para resetear la encuesta si es necesario"""
    def name(self) -> Text:
        return "action_reset_encuesta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        # Resetear el estado de la encuesta
        return [
            SlotSet("slot_encuesta_completada", False),
            SlotSet("slot_feedback_pendiente", False),
            SlotSet("slot_mejora", None),
            SlotSet("slot_satisfaccion", None),
            SlotSet("slot_recomendacion", None)
        ]













































# from typing import Dict, Text, Any, List
# from rasa_sdk import Tracker, Action
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction
# import time


# TIEMPO_ENCUESTA = 8

# class ActionDeactivateFeedback(Action):
#     def name(self) -> Text:
#         return "action_deactivate_feedback"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
#         # Obtener valores de los slots
#         var_mejora = tracker.get_slot("slot_mejora")
#         var_satisfaccion = tracker.get_slot("slot_satisfaccion")
#         var_recomendacion = tracker.get_slot("slot_recomendacion")

#         # print(f"Valor del slot 'mejora': {var_mejora}")
#         # print(f"Valor del slot 'satisfaccion': {var_satisfaccion}")
#         # print(f"Valor del slot 'recomendacion': {var_recomendacion}")
        
#         # Guardar timestamp actual y marcar feedback como no pendiente
#         tiempo_actual = time.time()
#         print("valor del slot ANTES",tracker.get_slot("slot_ultima_encuesta"))
#         result = [
#             SlotSet("slot_feedback_pendiente", False),
#             SlotSet("slot_ultima_encuesta", tiempo_actual)
#         ]
        
#         print(f"🎯 RETURNING: {result}")
#         return result


# class ActionVerificarFeedback(Action):
#     def name(self) -> Text:
#         return "action_verificar_feedback"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

#         # print(tracker.get_slot("slot_recomendacion"))
#         # print(tracker.get_slot("slot_ultima_encuesta"))
#         print("ACTION VERIFICAARFEEDBACK",tracker.get_slot("slot_ultima_encuesta"))
        
#         slot_ultima_encuesta = tracker.get_slot("slot_ultima_encuesta") or 0
#         ahora = time.time()

#         if ahora - slot_ultima_encuesta > TIEMPO_ENCUESTA:
#             # Es momento de ofrecer feedback
#             return [SlotSet("slot_feedback_pendiente", True)]
#         else:
#             # Aún no ofrecer feedback
#             print("AUN no ofrecer feeback-------- - - - - -")
#             return [SlotSet("slot_feedback_pendiente", False)]


