def is_even(number: int):
    return number % 2 == 0


def greatest_even(nums: list):
    current_max = -1

    for number in nums:
        if is_even(number) and number > current_max:
            current_max = number

    return current_max


def main():
    numbers = [22, 23, 44, 751, 224]
    print(f'The greatest even number in the list: {greatest_even(numbers)}')


if __name__ == "__main__":
    main()
