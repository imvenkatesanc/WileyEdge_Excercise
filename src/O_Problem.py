def repeat(string, n, delim):
    repeated = [string] * n
    repeated_string = delim.join(repeated)
    return repeated_string

# Example usage:
result = repeat("ho", 3, ", ")
print(result)  # Output: "ho, ho, ho"
