import re
from tools import calculator, weather, summarizer


def llm_reasoning(query):

    print("\n[LLM]: Understanding user request...")

    if "calculate" in query:
        reasoning = "User wants arithmetic computation"
        tool = "calculator"

    elif "weather" in query:
        reasoning = "User wants weather information"
        tool = "weather"

    elif "summarize" in query:
        reasoning = "User wants text summarization"
        tool = "summarizer"

    else:
        reasoning = "Intent unclear"
        tool = "unknown"


    print("[LLM Reasoning]:", reasoning)

    return tool


def execute_tool(tool, query):

    print("[LLM Decision]: Selected tool →", tool)


    if tool == "calculator":

        numbers = re.findall(r'\d+', query)

        if len(numbers) >= 2:

            return calculator(int(numbers[0]), int(numbers[1]))

        return "Need at least two numbers"


    elif tool == "weather":

        city = input("Enter city name: ")

        return weather(city)


    elif tool == "summarizer":

        text = input("Enter text to summarize: ")

        return summarizer(text)


    return "LLM could not determine tool"


def agent():

    query = input("Enter your request: ").lower()

    selected_tool = llm_reasoning(query)

    result = execute_tool(selected_tool, query)

    print("\n[Agent Response]:", result)


agent()