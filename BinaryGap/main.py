from solution import solution


def main():
    with open('test-input.txt', 'r') as file:
        for line in file:
            N = int(line.strip())
            longest_gap = solution(N)
            print(f"N = {N}, Longest Binary Gap = {longest_gap}")


if __name__ == "__main__":
    main()
