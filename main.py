def main():
    message = "Witaj, świecie!"
    print(message)
    with open("raport.html", "w") as file:
        file.write(f"<html><body><h1>{message}</h1></body></html>")

if __name__ == "__main__":
    main()
