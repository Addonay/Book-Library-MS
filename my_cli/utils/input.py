# utils/input.py

def get_user_input(prompt, required=True):
    """Prompt the user for input and return their response."""
    while True:
        user_input = input(prompt).strip()
        if required and not user_input:
            print("Input is required. Please try again.")
        else:
            return user_input

def get_choice_from_list(prompt, choices):
    """Prompt the user to select an option from a list."""
    while True:
        print(prompt)
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")
        choice_index = input("Select an option (1-{}): ".format(len(choices)))
        try:
            choice_index = int(choice_index)
            if 1 <= choice_index <= len(choices):
                return choices[choice_index - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Other input-related functions as needed
