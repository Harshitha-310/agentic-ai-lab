import re
from tools import calculator, weather, summarizer


def detect_intent(query):

    if "calculate" in query:
        return "calculator"

    elif "weather" in query:
        return "weather"

    elif "summarize" in query:
        return "summarizer"

    return "unknown"


def execute_tool(intent, query):

    print("\n[Agent Decision]: Selected tool →", intent)


    if intent == "calculator":

        expression = query.replace("calculate", "")

        return calculator(expression)


    elif intent == "weather":

        city = input("Enter city name: ")

        return weather(city)


    elif intent == "summarizer":

        text = input("Enter text to summarize: ")

        return summarizer(text)


    else:

        return "No suitable tool found"


def run_agent():

    query = input("Enter your request: ").lower()

    print("\n[Agent]: Processing request...")

    intent = detect_intent(query)

    result = execute_tool(intent, query)

    print("\n[Agent Output]:", result)


run_agent()