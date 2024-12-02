# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
def remove_and_strip(lst, word):
    new_list = [item.strip() for item in lst if item.strip() != word]
    return new_list

if __name__ == "__main__":
    my_list = [" hello ", "world  ", " python ", "  hello", "coding "]
    word_to_remove = "hello"
    result = remove_and_strip(my_list, word_to_remove)
    print(f"Original list: {my_list}")
    print(f"After removing '{word_to_remove}' and stripping: {result}")
