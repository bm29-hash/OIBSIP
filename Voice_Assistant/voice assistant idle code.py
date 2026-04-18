
import datetime
import webbrowser


def speak(text):
    print("Assistant:", text)


def take_command():
    return input("You: ").lower()


def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {current_time}")


def tell_date():
    current_date = datetime.date.today()
    speak(f"Today's date is {current_date}")


def search_google():
    speak("Enter what you want to search")
    query = input("Search: ")
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")


def calculate():
    speak("Enter calculation like 5 + 3")
    expression = input("Enter: ")
    try:
        result = eval(expression)
        speak(f"Result is {result}")
    except:
        speak("Invalid calculation")


def run_assistant():
    command = take_command()

    if command == "hello":
        speak("Hello! How can I help you?")

    elif command == "time":
        tell_time()

    elif command == "date":
        tell_date()

    elif command == "search":
        search_google()

    elif command == "calculate":
        calculate()

    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif command == "open google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif command == "exit":
        speak("Goodbye!")
        exit()

    else:
        speak("I don't understand")


if __name__ == "__main__":
    speak("Hello, I am your assistant")

    while True:
        run_assistant()
