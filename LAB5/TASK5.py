def greet_user(name, gender, message):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Mrs."
    elif gender in ["neutral", "gender-neutral", "non-binary"]:
        title = "Mx."
    else:
        title = ""
    if title:
        return f"{message}, {title} {name}! Welcome."
    else:
        return f"{message}, {name}! Welcome."

if __name__ == "__main__":
    name = input("Enter your name: ")
    gender = input("Enter your gender (male/female/neutral): ")
    message_input = input("Enter a greeting message (e.g., hello, hi, welcome): ")
    message = greet_user(name, gender, message_input)
    print(message)