# PRODIGY_CS_03
# Description:
This Python script, check_password_strength.py, is designed to assess the strength of a password input by the user. The strength of the password is evaluated based on several criteria including length, presence of uppercase and lowercase letters, digits, and special characters.

# Functionality:
The script employs regular expressions to check for the presence of uppercase letters, lowercase letters, digits, and special characters in the password.
It assigns a strength score based on the fulfillment of various criteria, such as minimum length and presence of different character types.
The strength score is then used to categorize the password into one of the following categories: Very Weak, Weak, Moderate, Strong, or Very Strong.
The categorization is based on a scale ranging from 0 (very weak) to 5 (very strong).

# Criteria for Password Strength:
- Minimum length of 8 characters.
- Presence of at least one uppercase letter.
- Presence of at least one lowercase letter.
- Presence of at least one digit.
- Presence of at least one special character from the following: !@#$%^&*()-_+=[]{}|;:,.<>?~
# Dependencies:
The script utilizes the re module, which is a standard Python library for working with regular expressions. Therefore, there are no additional dependencies required to run the script.
