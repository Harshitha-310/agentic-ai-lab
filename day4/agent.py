import re


def extract_numbers(text):

    numbers = list(map(int, re.findall(r'\d+', text)))

    print("Step 1: Extracted numbers:", numbers)

    return numbers


def calculate_average(numbers):

    avg = sum(numbers) / len(numbers)

    print("Step 2: Calculated average:", avg)

    return avg


def summarize_result(avg):

    summary = f"The average value is {avg}"

    print("Step 3: Generated summary:", summary)

    return summary


def planner_agent():

    query = input("Enter your task: ")

    numbers = extract_numbers(query)

    if len(numbers) == 0:
        print("No numbers found.")
        return

    avg = calculate_average(numbers)

    summarize_result(avg)


planner_agent()