import random

# Expanded list of common words to use for generating usernames
word_list = [
    "tobi", "john", "mary", "jane", "paul", "susan", "alex", "emma", "david", "luke",
    "lisa", "james", "sophia", "olivia", "mia", "liam", "noah", "jack", "lucas", "mason",
    "harry", "charlotte", "victor", "oliver", "emily", "daniel", "ella", "chloe", "george",
    "henry", "scarlett", "aiden", "madison", "chris", "jackson", "hannah", "grace", "leah",
    "ryan", "zoe", "nora", "isaac", "leo", "quinn", "joseph", "elizabeth", "lucy", "lucas",
    "angela", "ariel", "ava", "jake", "kate", "sam", "olga", "victoria", "fiona", "susan",
    "peter", "johnny", "jackie", "annie", "amanda", "robert", "steve", "ella", "michael",
    "max", "jessica", "gabriel", "jose", "rachel", "sandra", "claire", "lily", "lucas",
    "michael", "ronald", "emma", "kevin", "zane", "jason", "william", "oscar", "eric",
    "julius", "emily", "sophie", "dylan", "alexis", "carl", "henry", "andrew", "victor", 
    "harold", "tina", "sean", "catherine", "melissa", "rebecca", "harold", "teresa", "paige",
    "karen", "fay", "johnny", "brian", "ted", "paul", "charles", "scott", "lauren", "annie",
    "julianna", "cheryl", "jenny", "neil", "lindsey", "brittany", "clark", "ariana", "jude",
    "zara", "stephen", "bryan", "olga", "victor", "terry", "vicky", "adam", "brian", "ella",
    "carla", "ashley", "kyle", "edward", "elena", "hugo", "melissa", "austin", "frank",
    "audrey", "maggie", "diana", "isabella", "carter", "leo", "simon", "ruby", "grayson",
    "violet", "chase", "freddie", "miles", "jackson", "lucy", "brooklyn", "olga", "adam",
    "jason", "jameson", "troy", "willow", "shane", "sienna", "lucas", "peter", "roberto",
    "gabriella", "finn", "zoe", "sara", "jake", "will", "matt", "steven", "caroline",
    "leah", "logan", "lucas", "julia", "jude", "penny", "ellen", "jennifer", "fay", "mark",
    "henry", "justin", "hannah", "cole", "elizabeth", "dan", "frankie", "brittany", "ella",
    "rosie", "aubrey", "chloe", "jasmine", "tessa", "melvin", "pearl", "jeffrey", "kelsey",
    "cole", "bryce", "lincoln", "jeremy", "daisy", "hugh", "maggie", "mason", "caleb",
    "milan", "evan", "ethan", "kaitlyn", "vivian", "charlie", "harold"
]

def generate_random_email(existing_emails):
    while True:
        # Generate a random email using the word list and a random number
        username = random.choice(word_list) + str(random.randint(1, 99))
        email = f"{username}@gmail.com"
        
        # Check if the email already exists, if so, generate a new one
        if email not in existing_emails:
            existing_emails.add(email)  # Add email to the set
            return email

def generate_random_password():
    # Prompt the user to input the password
    password = input("Enter the password you want to use for all emails: ")
    return password

def generate_email_count():
    # Prompt the user for the number of emails they want to generate
    while True:
        try:
            count = int(input("Enter the number of emails you want to generate: "))
            if count > 0:
                return count
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Set to store generated emails and avoid duplicates
existing_emails = set()

# Get user input for the password and number of emails
password = generate_random_password()
num_emails = generate_email_count()

with open("emails_passwords.txt", "w") as file:
    for _ in range(num_emails):
        email = generate_random_email(existing_emails)
        file.write(f"{email}|{password}\n")

print(f"✅ {num_emails} unique Gmail emails with your chosen password generated in 'emails_passwords.txt'.")
