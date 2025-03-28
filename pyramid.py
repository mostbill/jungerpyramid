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
        text = texts[(i - 1) % len(texts)]
        if i == 1:
            print(spaces + stars + " " + texts[2])  # Top of the pyramid
        elif i == height:
            print(spaces + stars + " " + texts[1])  # Lower left
        elif i == height - 1:
            print(spaces + stars + " " + texts[2])  # Lower right
        else:
            print(spaces + stars)

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the height of the pyramid: "))
        print_pyramid(user_input)
    except ValueError:
        print("Please enter a valid integer.")