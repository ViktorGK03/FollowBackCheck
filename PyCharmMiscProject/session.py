import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

print("Welcome to the who is not following me back on Instagram script. \n Login Details Required")

username = input("Username: ")
password = input("Password: ")

L = instaloader.Instaloader()

try:
    L.login(username, password)
# 2FA is required for the session to be approved by Instagram, otherwise gets declined immediately.
except TwoFactorAuthRequiredException:
    print("2FA is required.")
    two_factor_code = input("2FA Code: ")
    L.two_factor_login(two_factor_code)

L.save_session_to_file()

print("Done.")
