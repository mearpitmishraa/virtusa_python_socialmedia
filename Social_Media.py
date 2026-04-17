#Test Case
posts = [
    "Person1: I hate this platform http://badlink.com",
    "Person2: This is a Good Day",
    "Person3: Such a TOXIC comment visit http://example.com",
    "Person1: I LoVe coding!",
    "Person5: BAD things happen sometimes http://test.com"
]
# list of banned words
ban_word = ["bad", "toxic", "hate"]

# store how many times each user flagged
user_flag = {}

# counters
total_posts = len(posts)
clean = 0
block = 0

# file link
file = open("Links_Found.txt", "w")
print("\n--- clean posts ---\n")

for post in posts:
    words = post.split()

    # get user name
    user = post.split(":")[0]

    # it will add user who is not added in dictionary
    if user not in user_flag:
        user_flag[user] = 0

    flag = False

    # converted post to lowercase 
    lower_post = post.lower()

    # check for ban word
    for bad_word in ban_word:
        if bad_word in lower_post:
            flag = True

            # if match replace it word with ***
            for word in words:
                if word.lower() == bad_word.lower():
                    post = post.replace(word, "***")

    # To Find Link and Save the flie
    for word in words:
        if word.startswith("http"):
            file.write(word + "\n")

    # for counter updating
    if flag:
        block += 1   
        user_flag[user] += 1
    else:
        clean += 1
        
    print(post)
file.close() # close the file

# Print Output 
print("\n--- Report ---")
print("Total Posts Screened:",total_posts)
print("clean:",clean)
print("block:",block)
print("\nUser Flags:")
print(user_flag)