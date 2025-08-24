from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher




#ALTERNATIVA 1
class ActionResponderEscuchaActiva(Action):
    def name(self) -> Text:
        return "action_responder_escucha_activa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("ENTRANDO a accion escucha activa-----")
        #varEmocion = tracker.get_slot("slotEmocion")
        varEmocion = "ansioso"

        respuestas = {
            "triste": "Parece que has estado pasando por un momento difícil, y me alegra que quieras hablarlo.",
            "ansioso": "Debe ser agotador sentir esa ansiedad. Estoy aquí para escucharte sin juzgar.",
            "feliz": "¡Me alegra que te sientas así! Cuéntame más, ¿qué ha hecho que tu día sea especial?",
        }

        mensaje = respuestas.get(varEmocion, 
            "Gracias por confiar en mí para hablar de esto. Cuéntame, ¿qué tienes en mente?")
        dispatcher.utter_message(text=mensaje)
        return []



#ALTERNATIVA 2

class ActionManejarAlternativas(Action):
    def name(self) -> Text:
        return "action_manejar_alternativas"
    
    def run(self, dispatcher, tracker, domain):
        varOpcion = tracker.get_slot("slot_tipo_alternativa")  # Lee el slot específico
        print("entrando a la action varOpcion",varOpcion)
        if varOpcion == "sentimientos":
            dispatcher.utter_message(text="sentmimientos select")
            dispatcher.utter_message(response="utter_iniciar_escucha")
            #ActionResponderEscuchaActiva().run(dispatcher, tracker, domain)
            return [
                SlotSet("slot_tipo_alternativa", None),
                SlotSet("slot_contexto", "escucha_activa")  # <- aquí marcamos el contexto
            ]
        elif varOpcion == "recursos":
            print("seleccionaste recursos------")
            #dispatcher.utter_message(text="articulo seleccionado")
            dispatcher.utter_message(response="utter_menu_list_recurso")
            dispatcher.utter_message(response="utter_menu_button_recurso") #payload
            return [SlotSet("slot_tipo_alternativa", None),
                    SlotSet("slot_contexto", None)]
        elif varOpcion == "despedida":
            dispatcher.utter_message(response="utter_despedida_final")
            return [SlotSet("slot_tipo_alternativa", None),
                    SlotSet("slot_contexto", None)]    
        else:
            dispatcher.utter_message(text="Opción no reconocida.")
            return [SlotSet("slot_tipo_alternativa", None),
                    SlotSet("slot_contexto", None)]
        
  


## Seleccion y entrega de recurso      

class ActionEntregaRecursoSel(Action):
    def name(self) -> Text:
        return "action_entrega_recurso_sel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        varTipoRecurso = tracker.get_slot("slot_tipo_recurso")
        print("varTipoRecurso: ",varTipoRecurso)
        
        recursos = {
            "meditacion": {
                "text": "Aquí tienes una meditación guiada de 5 minutos: [enlace]",
                "image": "https://ejemplo.com/meditacion.jpg"
            },
            "respiracion": {
                "text": "Ejercicios de respiración para calmar la ansiedad: [enlace]",
                "image": "https://ejemplo.com/respiracion.jpg"
            },
            "articulo": {
                "text": "Artículo completo sobre manejo emocional: [enlace]",
                "image": "https://ejemplo.com/articulo.jpg"
            }
        }
        
        recurso = recursos.get(varTipoRecurso)

        if not recurso:
            dispatcher.utter_message(text="Lo siento, no tengo ese recurso disponible ahora.")
            return []
             
        dispatcher.utter_message(
            text=recurso["text"],
            image=recurso["image"]
        )
        return [SlotSet("slot_tipo_recurso", None)]












