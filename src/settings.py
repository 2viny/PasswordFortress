# Color of the background of the entire app
BG_APP = "#545454"  # "#121212"

# Color and font of the text
FG = "#e9e9e9"
STD_FONT = "Arial"
STD_SIZE_FONT = 12

# Color of the hints in entrys
HINT_FG = "#c2c0c0"

# Settings of the strength bar
BAR_BG = "#c2c0c0"
BAR_COLOR = "#2596be"

# BG of non flat buttons
BUTTONS_BG = "#154c79"

# Login Frame settings
# Header text and font
LOGIN_HEADER_TEXT = "Welcome to PasswordFortress!"
LOGIN_HEADER_FONT = (STD_FONT, STD_SIZE_FONT+2, "bold")

# Text and font of the widgets
LOGIN_GUIDE_TEXT = "Log Into PasswordFortress"
LOGIN_USERNAME_HINT = "Enter Your Username"
LOGIN_PASSWORD_HINT = "Enter Your Password"
LOGIN_WIDGETS_FONT = (STD_FONT, STD_SIZE_FONT)
LOGIN_LOG_IN_TEXT = "Log In"

# Text and text color for a invalid login
INVALID_LOGIN = "This Login is Invalid."
INVALID_LOGIN_FG = "#ff0000"

# Text and text color for warning suspension and suspended accounts
TIMEOUT_LOGIN = "Account Suspended For:"
TIMEOUT_LOGIN_FG = "#ff0000"

START_TIMEOUT_WARNING = "Account Will be Suspended in"
END_TIMEOUT_WARNING = "Tries..."
TIMEOUT_WARNING_FG = "#fcf917"

SUSPENDED_LOGIN = "Account Suspended"
SUSPENDED_LOGIN_FG = "#ff0000"

TRIES_TO_TIMEOUT = 5

# Text and text color for a invalid login
VALID_LOGIN = "Login in..."
VALID_LOGIN_FG = "#28ab00"

# Settings of the register button
LOGIN_REGISTER_TEXT = "Register"
LOGIN_REGISTER_FONT = (STD_FONT, STD_SIZE_FONT-2, "underline")
LOGIN_REGISTER_FG = "#063970"

# Register Frame settings
# Header text and font
REGISTER_HEADER_TEXT = "Sing Up to PasswordFortress!"
REGISTER_HEADER_FONT = (STD_FONT, STD_SIZE_FONT+2, "bold")

# Text and font of the widgets
REGISTER_GUIDE_TEXT = "It's quick and secure."
REGISTER_NICKNAME_HINT = "Enter a Nickname"
REGISTER_USERNAME_HINT = "Enter a Username"
REGISTER_PASSWORD_HINT = "Enter a Password"
REGISTER_CONFIRM_PASSWORD_HINT = "Confirm the Password"
REGISTER_WIDGETS_FONT = (STD_FONT, STD_SIZE_FONT)
REGISTER_SING_UP_TEXT = "Sing Up"


# Setting of the password strength display
REGISTER_STRENGTH_TEXT = "Strength:"
REGISTER_STRENGTH_FONT = (STD_FONT, STD_SIZE_FONT-4)


# Settings of the back button
REGISTER_BACK_TEXT = "Back"
REGISTER_BACK_FONT = (STD_FONT, STD_SIZE_FONT-2, "underline")
REGISTER_BACK_FG = "#063970"

REGISTER_SUCCESS_FG = "#28ab00"
REGISTER_ERROR_FG = "#ff0000"

# Register Frame settings
# Header font
PROFILE_HEADER_FONT = (STD_FONT, STD_SIZE_FONT+8, "bold")

PROFILE_WIDGETS_FONT = (STD_FONT, STD_SIZE_FONT)

PROFILE_NEW_PLATAFORM_HINT = "Enter the Plataform"
PROFILE_NEW_LOGIN_HINT = "Enter the Login"
PROFILE_NEW_PASSWORD_HINT = "Enter the Password"

# Text of the cancel and confirm buttons in the popup's
CONFIRM_TEXT = "Confirm"
CANCEL_TEXT = "Cancel"

# Text of the widgets for changing password
CHANGING_HEADER_PASSWORD = "Type your new and old password to change it"

CHANGING_GUIDE_TEXT = "Fill the Boxes:"
CHANGING_GUIDE_FONT = (STD_FONT, STD_SIZE_FONT-2)
ON_CHANGING_ERROR = "#ff0000"
ON_CHANGING_SUCESS = "#28ab00"

OLD_PASSWORD_HINT = "Enter Your Current Password"
NEW_PASSWORD_HINT = "Enter a new Password"
CONFIRM_PASSWORD_HINT = "Confirm the Password"

# Hints that should be hidden when the user is typing in their boxes
HINTS_HIDE_BOX = [LOGIN_PASSWORD_HINT, REGISTER_PASSWORD_HINT, REGISTER_CONFIRM_PASSWORD_HINT,
                  OLD_PASSWORD_HINT, NEW_PASSWORD_HINT, CONFIRM_PASSWORD_HINT]