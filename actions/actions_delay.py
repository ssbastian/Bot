import asyncio
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List

# Función helper para enviar mensajes con delay
async def utter_with_delay(dispatcher, text, delay=1.0, buttons=None):
    """Envía un mensaje con delay opcional"""
    if buttons:
        dispatcher.utter_message(text=text, buttons=buttons)
    else:
        dispatcher.utter_message(text=text)
    
    await asyncio.sleep(delay)

# Acciones de delay para usar en stories/rules
class ActionDelayPequeno(Action):
    def name(self) -> Text:
        return "action_delay_pequeno"

    async def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        await asyncio.sleep(1.2)
        return []

class ActionDelayMedio(Action):
    def name(self) -> Text:
        return "action_delay_medio"

    async def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        await asyncio.sleep(2.0)
        return []

class ActionDelayGrande(Action):
    def name(self) -> Text:
        return "action_delay_grande"

    async def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        await asyncio.sleep(3.0)
        return []

# Acciones que usan la función helper para flujos complejos
class ActionPreguntarComfortConDelay(Action):
    def name(self) -> Text:
        return "action_preguntar_comfort_con_delay"

    async def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        await utter_with_delay(
            dispatcher, 
            "Para poder ayudarte mejor, ¿cómo describirías tu comfort en situaciones sociales hoy?",
            delay=1.5
        )