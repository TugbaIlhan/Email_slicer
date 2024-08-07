def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domanin : ", domain)
    print("Extension : ", extension)

while True:
    main()    