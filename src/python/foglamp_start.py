import logging
from foglamp.starter import start

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("foglamp").setLevel(logging.DEBUG)

    start()


if __name__ == "__main__":
    main()
