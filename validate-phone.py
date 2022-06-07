import re
from tkinter.messagebox import RETRY

# Does a string contain a phone number?
def has_phone_number(input_string):
    match = re.match(r".*\d{3}\W\d{3}\W\d{4}", input_string)
    return True if match else False 
# .+(\d{3}-\d{3}-\d{4})
# Get a phone number back from a string
def get_phone_number(input_string):
    match = re.match(r".+(\d{3}-\d{3}-\d{4})", input_string)
    if match is None: 
        return None
    else: 
        return match.group(1)



# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    # findall return empty list if nothing is found
    match = re.findall(r"(\d{3}-\d{3}-\d{4})", input_string)
    return match 

# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    match = re.findall(r"(\d{3}-\d{3}-\d{4})", input_string)
    output = []
    for n in match:
        only_digits = re.sub(r"\d", 'X', n, count=6)
        output.append(only_digits)
    output_str = ', '.join(output)
    return output_str

# def hide_phone_numbers(input_string):
#   pattern = r"\d{3}-\d{3}-\d{4}"
#   result = re.sub(pattern, r"XXX-XXX-\1", input_string)
#   return result


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    phone_list = re.split(r"(.*\d{3}.*\d{3}.*\d{4})", input_string)
    split_phone_list = phone_list[1].split(',')
    output = []
    for i in range(len(split_phone_list)):
        only_digits = re.sub(r"\D", '', split_phone_list[i])
        formatted_number = only_digits[0:3] + '-' + only_digits[3:6] + '-' + only_digits[6:len(only_digits)]
        output.append(formatted_number)
    output_str = ', '.join(output)
    return output_str



#    .    - any single character
#   \w    - matches any 'word' character, letters,      numbers, underscores
#    +    - repeat the previous thing, on eor more times
#   [ ]   - like an 'or' expression
#    \d   - digit
#    |    - or
#    $    - at end of string