import re

def check_password_strength(password):
    # Initialize variables to track criteria
    length = len(password)
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*()-_+=\[\]{}|;:,.<>?~]", password))

    # Initialize strength score
    strength_score = 0

    # Assess password strength based on criteria
    if length >= 8:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1

    # Provide feedback based on strength score
    if strength_score == 5:
        return "Very Strong"
    elif strength_score >= 3:
        return "Strong"
    elif strength_score >= 2:
        return "Moderate"
    elif strength_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

# Main function to prompt user input and display strength feedback
def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
