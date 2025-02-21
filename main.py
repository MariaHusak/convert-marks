def calculate_marks(mark) -> int:
    grade_ranges = {
        range(90, 101): "A",
        range(81, 90): "B",
        range(71, 81): "C",
        range(61, 71): "D",
        range(51, 61): "E",
        range(0, 51): "F",
    }

    for grade_range, grade in grade_ranges.items():
        if mark in grade_range:
            return grade
    return "Invalid mark"


def main():
    try:
        mark = int(input("Enter your mark: "))
        print(f"Your grade is {calculate_marks(mark)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()