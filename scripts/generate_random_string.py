import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def write_to_file(content, filename="massive_string.rs"):
    with open(filename, "w") as file:
        file.write('pub const MASSIVE_STRING: &\'static str = "\n')
        for i in range(0, len(content), 79):  # Line width 79 + `\`
            file.write(content[i:i+79] + "\\\n")
        file.write('";')

if __name__ == "__main__":
    desired_length = 50_000
    random_string = generate_random_string(desired_length)
    write_to_file(random_string)
    print(f"Random string created.")
