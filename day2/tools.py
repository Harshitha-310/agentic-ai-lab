from datetime import datetime


def calculator(expression):

    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except:
        return "Invalid calculation expression"


def weather(city):

    return f"Weather in {city} is sunny (mock API response)"


def summarizer(text):

    summary = text[:60]

    return f"Summary: {summary}..."