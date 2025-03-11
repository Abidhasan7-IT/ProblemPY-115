# List Duplicates Removal: Write a Python program to remove duplicates from a given list
# while preserving the order of the elements.

def remove_duplicates(input_list):
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result

# Example usage
input_list = [1, 2, 3, 2, 4, 3, 5, 1]
output_list = remove_duplicates(input_list)
print("List after duplicates removal:", output_list)
