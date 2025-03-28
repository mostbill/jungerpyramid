def print_pyramid(height):
    """
    Prints a pyramid of the given height using asterisks (*).
    :param height: The height of the pyramid
    At the end of each pyramid row, the following texts are displayed:
    1) assertive behaviors
    2) attained values and ideas
    3) alter-ego needs
    """
    if height <= 0:
        print("Height must be a positive integer.")
        return

    # List of texts to display at the end of each row
    texts = ["assertive behaviors", "attained values and ideas", "alter-ego needs"]
    texts = texts[::-1]  # Reverse the order to match the desired sequence

    for i in range(1, height + 1):
        # Print spaces for alignment
        spaces = ' ' * (height - i)
        # Print asterisks for the pyramid
        stars = '*' * (2 * i - 1)
        # Select the appropriate text based on the row index
        buffer = ' ' * (len(texts[1]) + 1)  # Buffer space for text alignment
        if i == 1:
            print(buffer + spaces + stars + " " + texts[2])  # Top of the pyramid
        elif i == height:
            print(texts[1] + ' ' + spaces + stars + ' ' + texts[0]) # Bottom of the pyramid
        else:
            print(buffer + spaces + '*' + ' ' * (2 * i - 3) + '*')

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the height of the pyramid: "))
        print_pyramid(user_input)
    except ValueError:
        print("Please enter a valid integer.")