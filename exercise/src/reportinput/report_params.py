from typing import List


def gen_params(a, b) -> List[str]:
    try:
        # Check if inputs are empty or None
        if not a or not b:
            raise ValueError("Input strings cannot be empty or None.")

        # Check if inputs are strings
        if not (isinstance(a, str) and isinstance(b, str)):
            raise TypeError("Inputs must be strings.")

        # Convert input strings to lowercase and split by whitespace or comma
        a_lower_set = [elem.strip().lower() for elem in a.replace(',', ' ').split()]
        b_lower_set = [elem.strip().lower() for elem in b.replace(',', ' ').split()]

        # Find intersection of sets to get common elements
        common_elements = set(a_lower_set) & set(b_lower_set)

        # Find sorted intersection of sets to get common elements
        sorted_common_elements = sorted(common_elements)

        # Convert set to list and return
        return list(sorted_common_elements)

    except TypeError as te:
        raise te
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"An unexpected error occurred in gen_params(): {e}")


def main():
    try:
        # Get input for two string inputs
        a_input = input("Enter the first string input: ")
        b_input = input("Enter the second string input: ")

        # Call the function to find common elements
        result = gen_params(a_input, b_input)

        # Print the common elements found
        print("Common elements:", result)

    except TypeError as te:
        print(f"An error occurred: {te}")
    except ValueError as ve:
        print(f"An error occurred: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
