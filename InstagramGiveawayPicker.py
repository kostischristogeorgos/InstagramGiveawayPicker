import instaloader
from instaloader import Profile, Post
import random

L = instaloader.Instaloader()

# Getting username and fetching it into the profile variable
username = input("Give me the profile's name")
profile = instaloader.Profile.from_username(L.context, username)

# Gathering the comments from the latest post

for post in profile.get_posts():
    comments = post.get_comments()
    break


usernames = []

# Getting the username from the people who commented and putting it in the list
for comment in comments:
    usernames.append(comment.owner.username)

print("Total comments = ", len(usernames))

# Winner1 is a random username in the usernames list
winner1 = usernames.pop(random.randrange(len(usernames)))

# Getting the other 2 winners as long as they're not the same. If they are, they are drawn again.
while True:
    winner2 = usernames.pop(random.randrange(len(usernames)))
    winner3 = usernames.pop(random.randrange(len(usernames)))
    if (winner1 != winner2) and (winner1 != winner3) and (winner2 != winner3):
        break


print("Winner1 is: " + winner1 + " Winner2 is : ", winner2 + " Winner3 is ", winner3)


# Saving the winners in the winners.txt file
file = open("winners.txt", 'w+')
file.write(winner1 + "\n" + winner2 + "\n" + winner3)

