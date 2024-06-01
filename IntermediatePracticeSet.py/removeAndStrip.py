def remove_and_strip(word_list, word_to_remove):
    """
    Remove a given word from a list and strip whitespace from each element.
    
    Parameters:
    word_list (list): The list of words to process.
    word_to_remove (str): The word to remove from the list.
    
    Returns:
    list: A new list with the specified word removed and each element stripped of whitespace.
    """
    return [word.strip() for word in word_list if word.strip() != word_to_remove.strip()]

# Example usage
example_list = [" apple ", " banana ", "  orange ", "apple", "grape"]
word_to_remove = "apple"
result = remove_and_strip(example_list, word_to_remove)
print(result)  # Output: ['banana', 'orange', 'grape']
