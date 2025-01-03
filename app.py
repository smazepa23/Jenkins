def generate_message():
    return "Witaj, świecie!"

def main():
    message = generate_message()
    print(message)
    with open("raport.html", "w") as file:
        file.write(f"<html><body><h1>{message}</h1></body></html>")

if __name__ == "__main__":
    main()

