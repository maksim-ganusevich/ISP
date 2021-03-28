import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def solve(n):
    return int(((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)) / math.sqrt(5))


def main():
    logger.info(solve(1000))


if __name__ == "__main__":
    main()
