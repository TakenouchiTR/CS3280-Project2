import sys
import utils

def main():
    result = utils.get_links("https://www.westga.edu")
    for line in result:
        print(line)

if __name__ == "__main__":
    main()