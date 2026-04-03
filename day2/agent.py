import re
from tools import calculator, weather, summarizer


def decide_tool(user_input):

    if "calculate" in user_input:
        return "calculator"

    elif "weather" in user_input:
        return "weather"

    elif "summarize" in user_input:
        return "summarizer"

    else:
        return None


def run_agent():

    user_input = input("Enter command: ").lower()

    tool = decide_tool(user_input)


    if tool == "calculator":

        numbers = re.findall(r'\d+', user_input)

        if len(numbers) >= 2:
            result = calculator(int(numbers[0]), int(numbers[1]))
            print("Result:", result)
        else:
            print("Please enter two numbers")


    elif tool == "weather":

        city = input("Enter city name: ")
        print(weather(city))


    elif tool == "summarizer":

        text = input("Enter text to summarize: ")
        print(summarizer(text))


    else:

        print("No matching tool found")


run_agent()