# function which, when given the same input, returns the same output!
# should not produce any side effects

def double_len(numbers: list):
    return 2*numbers

def main():
    numbers = [1,2,3]
    double_numbers = double_len(numbers)

    print(double_numbers)

if __name__ == "__main__":
    main()