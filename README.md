Introduction-
This project is a basic Python programme that checks social media posts for inappropriate content. It helps in identifying harmful words, cleaning them, and keeping track of flagged users.

Working Mechanism-
The program goes through each post one by one and converts it into lowercase to ensure case-insensitive checking. It compares the post with a list of banned words like bad, toxic, and hate.
If any such word is found, it replaces it with *** and marks the post as flagged.
It also checks for links (words starting with "http") and saves them into a file named Links_Found.txt.

Important Code Explanation-
A list of posts is used as input data.
A dictionary (user_flag) is used to store how many times each user has flagged.
The program uses loops to go through posts and banned words.
String methods like .lower() help in case-insensitive comparison.
File handling (open, write) is used to store extracted links.

Logic Used-
Convert post to lowercase → compare with banned words
If match found → replace word with ***
If post contains link → save it in file
Update counters for clean and flagged posts
Track user-wise flags using dictionary

Output-
Displays all posts (cleaned if needed)
Shows total posts, clean posts, and flagged posts
Prints how many times each user was flagged
Saves all extracted links in Links_Found.txt
