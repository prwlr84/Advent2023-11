from main import expand_grid


def test_adjust_list():
    # Define the test input and expected output
    test_input = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#....."
    ]
    expected_output = [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#......."
    ]

    # Convert string input to list of lists
    test_input_list = [list(line) for line in test_input]

    # Run the adjust_list function
    actual_output_list = expand_grid(test_input_list)

    # Convert list of lists back to list of strings for comparison
    actual_output = [''.join(sublist) for sublist in actual_output_list]

    # Assert equality
    assert actual_output == expected_output, f"Test failed: Expected {expected_output}, but got {actual_output}"

    print("Test passed successfully!")


if __name__ == '__main__':
    test_adjust_list()
