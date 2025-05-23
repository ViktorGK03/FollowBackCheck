I wanted to see the people that are not following me back on instagram, so i can unfollow them using the python library instaloader.
The idea was to have a way of logging in with my creds of a test account and scrape the data of my personal account like followers and the people i am following, then deduct one out of the other and see the people that are not following me back.
I ran into a bunch of problems with the Instagram 'security checks' you could say. When scraping the followers and etc. I would get flagged really fast. So i tried adding sleep() of 1 or 2 seconds at a time after each follower, still got caught fast.
Then the best result I got was by adding a random time of sleep in an interval. But eventually still got caught.
My current best results are 230 - 250 followers being scraped until getting flagged, So i could definetely do this in a bunch of batches like maybe 50 at a time, but that will just take too much time if you count the sleep after every follower which can be between (2, 15)
and the cooldown i tried every 50 followers of (70, 100). Then another cooldown of 65 seconds once done with followers and starting my following.

In conclusion, Instagram security checks beat me.
The program does work with smaller accounts that have in total less than ~200 followers and following in total.

In the end just pasting the script into the website console works much better, and almost instantly. IG i will soon try making this whole thing with a WebView + Script injection combo.
