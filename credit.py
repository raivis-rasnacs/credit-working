"""
Checks type of card
"""
def check_type_of_card(card_number):

    # Gets length of card number
    length = len(card_number)

    # Possible starting numbers
    AMEX_nums = ["34", "37"]
    MASTERCARD_nums = ["51", "52", "53", "54", "55"]
    VISA_nums = ["4"]
    VISA_lengths = [13, 16]

    # Various checks for possible match
    if length == 15 and str(card_number[:2]) in AMEX_nums:
        return "AMEX"
    elif length == 16 and str(card_number[:2]) in MASTERCARD_nums:
        return "MASTERCARD"
    elif length in VISA_lengths and str(card_number[:1]) in VISA_nums:
        return "VISA"
    else:
        return "INVALID"


"""
Sums digits starting from second-to-last
"""
def sum_digits(card_number):
    sum_of_digits = 0
    digits = str()
    for x in range(len(card_number) - 2, -1, -2):
        digits += str(int(card_number[x]) * 2)
    for digit in digits:
        sum_of_digits += int(digit)
    return sum_of_digits


"""
Sums digits starting from the last one
"""
def sum_unmultiplied_digits(card_number):
    sum_of_digits = 0
    unmultiplied_digits = str()
    for x in range(len(card_number) - 1, -1, -2):
        unmultiplied_digits += str(int(card_number[x]))
    for digit in unmultiplied_digits:
        sum_of_digits += int(digit)
    return sum_of_digits


# Asks for input
card_number = input("Card number: ")

# Checksum calculations
total_sum = sum_digits(card_number) + sum_unmultiplied_digits(card_number)

if total_sum % 10 == 0:

    # Checks for type of card
    card_type = check_type_of_card(card_number)

    # Outputs result
    print(card_type)

else:
    print("INVALID")
