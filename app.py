import random  # Importing the random module
import datetime  # Importing the datetime module

def main():
    # Print a greeting to the user.
    print("Hello, World!"
    
    # Generate a random number between 0 and 7 (inclusive).
    random_number = random.randint(0, 7
    
    # Print the generated random number
    print(f"This is my random number: {random_number}")
    
    # Print the current date and time
    print(f"AI generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("Succeeded running this app"

# Check if this script is being run directly (and not being imported)
if __name__ == "__main__":
    main()
