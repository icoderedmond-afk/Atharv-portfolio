# collect email from user
#slice email using the @ symbol, save the first part as a user name, the second part will be saved as a domain, with the period being the identifier
def main():
    print("Email Slicer")
    print()

    email_input = input("Put you email.It is never saved: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
while True:
    main()
