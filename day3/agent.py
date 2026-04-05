import re
from tools import calculator, weather, summarizer
from openai import OpenAI

client = OpenAI()


def real_llm_reasoning(query):

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Classify intent as calculator, weather, or summarizer"
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )

        intent = response.choices[0].message.content.strip().lower()

        print("[LLM Reasoning]:", intent)

        return intent

    except:

        print("[LLM Error]: API unavailable")

        return None


def fallback_reasoning(query):

    print("[Fallback]: Using simulated reasoning")

    if any(word in query for word in ["calculate", "add", "sum", "+", "what is"]):
        return "calculator"

    elif "weather" in query:
        return "weather"

    elif any(word in query for word in ["summarize", "summary"]):
        return "summarizer"

    return "unknown"


def select_tool(query):

    print("\nAttempting real LLM reasoning...")

    tool = real_llm_reasoning(query)

    if tool not in ["calculator", "weather", "summarizer"]:

        tool = fallback_reasoning(query)

    print("[Decision]: Selected tool →", tool)

    return tool


def execute_tool(tool, query):

    if tool == "calculator":

        numbers = re.findall(r'\d+', query)

        if len(numbers) >= 2:
            return calculator(int(numbers[0]), int(numbers[1]))

        return "Need two numbers"


    elif tool == "weather":

        city = input("Enter city name: ")
        return weather(city)


    elif tool == "summarizer":

        text = input("Enter text to summarize: ")
        return summarizer(text)


    return "Tool not identified"


def agent():

    query = input("Enter your request: ").lower()

    tool = select_tool(query)

    result = execute_tool(tool, query)

    print("\nAgent Response:", result)


agent()