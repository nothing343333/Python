user_input = input("enter the message you want to filter out as a spam or not a spam\n")


if user_input in user_input:
    spam_words = ["Buy now", "Click this", "Subscribe this"]
    spam_count = sum(user_input.count(word) for word in spam_words)
    print("Spam count: ", spam_count)
    if spam_count > 0:
        print("Spam\n")
