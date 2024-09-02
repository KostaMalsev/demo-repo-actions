import random
import datetime

def main():
    print("Hello, World!")
    random_number = random.randint(0, 8)
    print(f"This is my random number: {random_number}")

    print(f"AI generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()