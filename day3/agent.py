import re
import os
from tools import calculator, weather, summarizer
from openai import OpenAI


# CONNECT TO GROQ API

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# REAL LLM REASONING USING GROQ

def real_llm_reasoning(query):

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Classify intent as calculator, weather, or summarizer. Return only one word."
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

    except Exception as e:

        print("[LLM Error]: Groq API unavailable")

        return None


# FALLBACK REASONING (SAFE BACKUP)

def fallback_reasoning(query):

    print("[Fallback]: Using simulated reasoning")

    if any(word in query for word in ["calculate", "add", "sum", "+", "what is"]):
        return "calculator"

    elif "weather" in query:
        return "weather"

    elif any(word in query for word in ["summarize", "summary"]):
        return "summarizer"

    return "unknown"


# TOOL SELECTION PIPELINE

def select_tool(query):

    print("\nAttempting LLM reasoning using Groq...")

    tool = real_llm_reasoning(query)

    if tool not in ["calculator", "weather", "summarizer"]:

        tool = fallback_reasoning(query)

    print("[Decision]: Selected tool →", tool)

    return tool


# TOOL EXECUTION

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


# MAIN AGENT LOOP

def agent():

    query = input("Enter your request: ").lower()

    tool = select_tool(query)

    result = execute_tool(tool, query)

    print("\nAgent Response:", result)


agent()