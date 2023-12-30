# Part 1
def part1(data):
    total = 0
    # For each line in data
    for line in data:
        # Get list of all digits in the line
        digits = [int(character) for character in line if character.isdigit()]
        # Add first digit times 10 plus the last digit for each line
        total += (digits[0] * 10) + digits[-1]
    return total

# Part 2
def part2(data):
    # List of words to map to their integer counterparts
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_data = []
    # For each line in data
    for line in data:
        new_line = []
        # Go through each character
        for i in range(len(line)):
            # For each word in mappings, check if the line starts with it
            mapped_digit = "".join([str(index) for index, word in enumerate(mappings, 1) if line[i:].startswith(word)])
            # If the word was found, add the mapped digit, else add the original character
            new_line.append(mapped_digit if mapped_digit else line[i])
        new_data.append(new_line)
    # Use the part1 function to calculate the total for new_data
    return part1(new_data)
        
# Open and read the data file
with open('day1_input.txt') as file:
    data = file.readlines()

# Print the results of both functions
print(part1(data))
print(part2(data))
