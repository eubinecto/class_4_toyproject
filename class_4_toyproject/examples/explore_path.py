from pathlib import Path


def main():
    my_path = Path().resolve()
    print(my_path)


if __name__ == '__main__':
    main()