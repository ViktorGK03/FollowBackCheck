import instaloader
import time
import random
#from session import username


def human_sleep():
    time.sleep(random.uniform(2,15))
def cooldown():
    time.sleep(random.uniform(70,100))
username = "poko2082025"
L = instaloader.Instaloader()
# The load session is set to a test account. Because of the cases where
# Instagram detects the suspicious activity of scraping, the test account get
# banned or temporary restricted and not my personal one.
# So I'm loading my personal profile details from the test account session.
L.load_session_from_file(username)


profile = instaloader.Profile.from_username(L.context, "viktor.k03")
counter = 0
#max_fetch = 50
followers = set()
print("Fetching followers...")
for follower in profile.get_followers():
    print("Fetching follower...")
    followers.add(follower.username)
    human_sleep()
    counter += 1
    if counter % 50 == 0:
        print("Cooldown")
        cooldown()
#followers = set(f.username for f in profile.get_followers())

with open("followers.txt", "w") as file:
    for user in followers:
        file.write(user + "\n")

time.sleep(65)
following = set()
print("Fetching followees...")
for followee in profile.get_followees():
    print("Fetching followee...")
    following.add(followee.username)
    human_sleep()
    counter += 1
    if counter % 50 == 0:
        print("Cooldown")
        cooldown()
#following = set(f.username for f in profile.get_followees())

with open("following.txt", "w") as file:
    for user in following:
        file.write(user + "\n")

not_following_back = following - followers

with open("not_following_back.txt", "w") as file:
    for user in not_following_back:
        file.write(user + "\n")

print("Done.")