# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from rasa_sdk.events import SlotSet


#tipo de actividades que se muestran 
class ActionFiltrarOpciones(Action):
    def name(self) -> Text:
        return "action_filtrar_opciones"

    def run(self, dispatcher, tracker, domain):
        mostrar_todas_str = tracker.get_slot("slot_actividades_all")
        mostrar_todas = mostrar_todas_str == "true"
        varEmocion = tracker.get_slot("slot_tipo_emocion")
        print("mostrar_todas:---",mostrar_todas)
        if mostrar_todas:
            dispatcher.utter_message(response="utter_menu_mostrarAll")
        else:
            if varEmocion == "negativo":
                dispatcher.utter_message(response="utter_menu_list_actividadesN")
            elif varEmocion == "positivo":
                dispatcher.utter_message(response="utter_menu_list_actividadesP")
            elif varEmocion == "neutro":
                dispatcher.utter_message(response="utter_menu_list_actividadesNE")
            else:
                dispatcher.utter_message(text="No se pudo identificar la emoción actual. Por favor, intenta de nuevo.")

        # Resetear el slot después de mostrar las actividades
        return [SlotSet("slot_actividades_all", "false")]
    
# class ActionFiltrarOpciones(Action):
#     def name(self) -> Text:
#         return "action_filtrar_opciones"

#     def run(self, dispatcher, tracker, domain):
#         varEmocion = tracker.get_slot("slot_tipo_emocion")

#         if varEmocion == "negativo":
#             dispatcher.utter_message(response="utter_menu_list_actividadesN")
#         elif varEmocion == "positivo":
#             dispatcher.utter_message(response="utter_menu_list_actividadesP")
#         elif varEmocion == "neutro":
#             dispatcher.utter_message(response="utter_menu_list_actividadesNE")
#         else:
#             dispatcher.utter_message(text="No se pudo identificar la emoción actual. Por favor, intenta de nuevo.")

#         return []
# class ActionFiltrarOpciones(Action):
#     def name(self) -> Text:
#         return "action_filtrar_opciones"

#     def run(self, dispatcher, tracker, domain):
#         varEmocion = tracker.get_slot("slot_tipo_emocion")
#         mostrarTodas = tracker.get_slot("slot_actividades_all")  # slot para mostrar todas las actividades
#         print('MOSTRAR TODAS--',mostrarTodas)
#         # Primero revisamos si el usuario quiere ver todas las actividades
#         if mostrarTodas:
#             dispatcher.utter_message(response="utter_menu_mostrarAll")
#         else:
#             # Filtramos según la emoción
#             if varEmocion == "negativo":
#                 print('EMOCIONES negativas--')
#                 dispatcher.utter_message(response="utter_TEST")
#                 #dispatcher.utter_message(response="utter_menu_list_actividadesN")
#             elif varEmocion == "positivo":
#                 dispatcher.utter_message(response="utter_menu_list_actividadesP")
#             elif varEmocion == "neutro":
#                 dispatcher.utter_message(response="utter_menu_list_actividadesNE")
#             else:
#                 dispatcher.utter_message(text="No se pudo identificar la emoción actual. Por favor, intenta de nuevo.")

#         return [SlotSet("slot_actividades_all", False)]

class ActionEjecutarOpcion(Action):
    def name(self) -> Text:
        return "custom_action_ejecutar_opcion"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Obtener la emoción actual del slot
        varEmocion = tracker.get_slot("slot_tipo_emocion")
        
        # 2. Extraer el número seleccionado (de entidades o botones)
        varNumero = next(tracker.get_latest_entity_values("ent_numActividad"), None)
        print(f"NUMEROO: {varNumero}")
        
        # 3. Mapeo de opciones por emoción
        opciones = {
            "negativo": {
                "1": "utter_detalle_respiracion",
                "2": "utter_detalle_escritura",
                "3": "utter_detalle_audio",
                "4": "utter_detalle_estiramientos"
            },
            "positivo": {
                "1": "utter_detalle_baile",
                "2": "utter_detalle_gratitud",
                "3": "utter_detalle_proyecto",
                "4": "utter_detalle_compartir"
            },
            "neutro": {
                "1": "utter_detalle_meditacion",
                "2": "utter_detalle_organizar",
                "3": "utter_detalle_leer",
                "4": "utter_detalle_hidratacion"
            }
        }

        # 4. Validación y respuesta
        if not varEmocion or not varNumero:
            dispatcher.utter_message(text="No detecté tu selección. Por favor elige una opción válida.")
        elif varEmocion in opciones and varNumero in opciones[varEmocion]:
            dispatcher.utter_message(response=opciones[varEmocion][varNumero])
        else:
            dispatcher.utter_message(text=f"⚠️ La opción {varNumero} no está disponible para emociones {varEmocion}.")

        return []
    
    
#Mostrar todas las actividades 
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionEjecutarCualquiera(Action):
    def name(self) -> Text:
        return "custom_action_ejecutar_cualquiera"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Obtener número seleccionado desde la entidad
        varNumero = next(tracker.get_latest_entity_values("ent_numActividad"), None)
        print(f"[DEBUG] Actividad seleccionada: {varNumero}")

        # 2. Mapeo de las 12 actividades (sin importar emoción)
        actividades = {
            "1": "utter_detalle_respiracion",
            "2": "utter_detalle_escritura",
            "3": "utter_detalle_audio",
            "4": "utter_detalle_estiramientos",
            "5": "utter_detalle_baile",
            "6": "utter_detalle_gratitud",
            "7": "utter_detalle_proyecto",
            "8": "utter_detalle_compartir",
            "9": "utter_detalle_meditacion",
            "10": "utter_detalle_organizar",
            "11": "utter_detalle_leer",
            "12": "utter_detalle_hidratacion"
        }

        # 3. Verificar si el número existe en el diccionario
        if varNumero and varNumero in actividades:
            dispatcher.utter_message(response=actividades[varNumero])
        else:
            dispatcher.utter_message(text="Lo siento, no reconozco esa actividad. Elige un número del 1 al 12.")
        
        # 4. (Opcional) limpiar slot si lo usas
        #return [SlotSet("slot_opcion_actividad", None)]
        return []

## ==============================================
## Flujos NEGACION actividades
## ==============================================

# class ActionEscuchaActiva(Action):
#     def name(self) -> Text:
#         return "action_escucha_activa"

#     def run(self, dispatcher, tracker, domain):
#         # Obtener el último mensaje del usuario
#         user_message = tracker.latest_message.get('text')
        
#         # Análisis básico de emociones (puedes mejorar con NLP después)
#         emotional_words = {
#             'triste': 'negativo', 
#             'ansioso': 'negativo',
#             'feliz': 'positivo',
#             'bien': 'positivo'
#         }
        
#         detected_emotion = 'neutro'
#         for word, emotion in emotional_words.items():
#             if word in user_message.lower():
#                 detected_emotion = emotion
#                 break
        
#         # Guardar en slots para personalizar respuestas
#         return [
#             SlotSet("emocion_detectada", detected_emotion),
#             #SlotSet("ultimo_mensaje", user_message[:50])  # Guardar fragmento
#         ]
   
   
# class ActionManejarAlternativas(Action):
#     def name(self) -> Text:
#         return "action_manejar_alternativas"
    
#     def run(self, dispatcher, tracker, domain):
#         opcion = tracker.get_slot("opcion_alternativas")  # Lee el slot específico
        
#         if opcion == "sentimientos":
#             dispatcher.utter_message(text="sentmimientos select")
#             #dispatcher.utter_message(response="utter_submenu_sentimientos")
#         elif opcion == "recursos":
#             dispatcher.utter_message(text="articulo seleccionado")
#             #dispatcher.utter_message(response="utter_submenu_recursos")
#         else:
#             dispatcher.utter_message(text="Opción no reconocida.")
        
#         return [SlotSet("opcion_alternativas", None)]  # Limpia el slot después de usarlo   



## Seleccion y entrega de recurso      

# class ActionEntregarRecursoSeleccionado(Action):
#     def name(self) -> Text:
#         return "action_entregar_recurso_seleccionado"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         tipo_recurso = tracker.get_slot("tipo_recurso")
        
#         recursos = {
#             "meditacion_recurso": {
#                 "text": "Aquí tienes una meditación guiada de 5 minutos: [enlace]",
#                 "image": "https://ejemplo.com/meditacion.jpg"
#             },
#             "respiración_recurso": {
#                 "text": "Ejercicios de respiración para calmar la ansiedad: [enlace]",
#                 "image": "https://ejemplo.com/respiracion.jpg"
#             },
#             "articulo_recurso": {
#                 "text": "Artículo completo sobre manejo emocional: [enlace]",
#                 "image": "https://ejemplo.com/articulo.jpg"
#             }
#         }
        
#         recurso = recursos.get(tipo_recurso, recursos["meditacion"])
        
#         dispatcher.utter_message(
#             text=recurso["text"],
#             image=recurso["image"]
#         )
        
#         return [SlotSet("tipo_recurso", None)]  # Limpia el slot después de usarlo
    
    

# class ActionEntregarRecurso(Action):
#     def name(self) -> Text:
#         return "action_entregar_recurso"

#     def run(self, dispatcher, tracker, domain):
#         # Obtener tipo de recurso desde el intent
#         resource_type = next(tracker.get_latest_entity_values("tipo_recurso"), "meditacion")
        
#         # Base de datos simple (puedes usar JSON/DB después)
#         resources = {
#             "meditacion": {
#                 "type": "audio",
#                 "url": "https://ejemplo.com/meditacion-5min.mp3",
#                 "text": "Meditación guiada para calmar la mente"
#             },
#             "respiracion": {
#                 "type": "video",
#                 "url": "https://ejemplo.com/respiracion-4-7-8.mp4",
#                 "text": "Técnica 4-7-8 para reducir ansiedad"
#             }
#         }
        
#         # Enviar recurso al usuario
#         resource = resources.get(resource_type, resources["meditacion"])
        
#         if resource["type"] == "audio":
#             dispatcher.utter_message(text=resource["text"])
#             dispatcher.utter_message(attachment=resource["url"])
#         else:
#             dispatcher.utter_message(text=f"Aquí tienes: {resource['text']}")
#             dispatcher.utter_message(image=resource["url"])
        
#         # Registrar estadísticas
#         return [SlotSet("ultimo_recurso", resource_type)]