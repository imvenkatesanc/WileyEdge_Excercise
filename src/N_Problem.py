def middle(string):
    length = len(string)
    middle_index = length // 2

    if length % 2 == 1:
        # If the length is odd, return the middle character
        return string[middle_index]
    else:
        # If the length is even, return the two middle characters
        return string[middle_index - 1:middle_index + 1]

# Example usage:
result = middle("middle")
print(result)  # Output: "dd"
