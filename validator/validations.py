#  check if text conatains special characters only
def check_only_special_character(text):

    validation = False

    # Declaring variable for special characters
    special_char = 0

    for i in range(0, len(text)):

        # is alphabet or not.
        if (text[i].isalpha()):
            continue

        # is a number or not.
        elif (text[i].isdigit()):
            continue

        else:
            special_char += 1

    if len(text) == special_char:
        validation = True

    return validation

# check if its a number


def check_is_numeric(text):

    return str(text).isnumeric()

# check if the text is blank


def check_if_blank(text):

    validation = False

    if len(text) == 0 or text == '' or not text:

        validation = True

    return validation

# check if the text is valid by calling all the validation functions


def validate_text(text):

    is_valid_text = False

    # check if text is not blank
    if not check_if_blank(text):

        # check if text is not only special characters
        if not check_only_special_character(text):

            # cehck if text is not only numbers
            if not check_is_numeric(text):

                is_valid_text = True

            else:

                is_valid_text = False

        else:

            is_valid_text = False

    else:

        is_valid_text = False

    return is_valid_text

# check if a text input has multiple lines


def check_for_multine(text):

    multiline_validation = False

    if len(text.splitlines()) > 2:

        multiline_validation = True

    else:

        multiline_validation = False

    return multiline_validation
