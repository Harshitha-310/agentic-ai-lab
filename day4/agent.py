import re


def extract_numbers(text):

    numbers = list(map(int, re.findall(r'\d+', text)))

    print("Step 1: Extracted numbers:", numbers)

    return numbers


def calculate_average(numbers):

    avg = sum(numbers) / len(numbers)

    print("Step 2: Calculated average:", avg)

    return avg


def calculate_sum(numbers):

    total = sum(numbers)

    print("Step 2: Calculated sum:", total)

    return total


def count_numbers(numbers):

    count = len(numbers)

    print("Step 2: Counted numbers:", count)

    return count


def summarize_result(result):

    summary = f"The result of the operation is {result}"

    print("Step 3: Generated summary:", summary)

    return summary


def planner(query):

    print("\nPlanning task...\n")

    numbers = extract_numbers(query)

    if len(numbers) == 0:
        print("No numbers found.")
        return


    if "average" in query:

        result = calculate_average(numbers)


    elif "sum" in query:

        result = calculate_sum(numbers)


    elif "count" in query:

        result = count_numbers(numbers)


    else:

        print("Could not determine operation.")
        return


    summarize_result(result)


def planner_agent():

    query = input("Enter your task: ").lower()

    planner(query)


planner_agent()