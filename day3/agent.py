import re
from tools import calculator, weather, summarizer


def llm_decision(query):

    """
    Simulated LLM reasoning layer.
    In real systems this would call OpenAI / LangChain.
    """

    if "calculate" in query:
        return "calculator"

    elif "weather" in query:
        return "weather"

    elif "summarize" in query:
        return "summarizer"

    else:
        return "unknown"


def agent():

    query = input("Enter your request: ").lower()

    print("\nAnalyzing query using LLM...")

    selected_tool = llm_decision(query)

    print("Selected tool:", selected_tool)


    if selected_tool == "calculator":

        numbers = re.findall(r'\d+', query)

        if len(numbers) >= 2:
            result = calculator(int(numbers[0]), int(numbers[1]))
            print("Result:", result)
        else:
            print("Please provide two numbers")


    elif selected_tool == "weather":

        city = input("Enter city name: ")
        print(weather(city))


    elif selected_tool == "summarizer":

        text = input("Enter text to summarize: ")
        print(summarizer(text))


    else:

        print("LLM could not determine correct tool")


agent()