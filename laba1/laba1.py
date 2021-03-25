import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

def solve(n):
    return round(((1 + math.sqrt(5)) ** n)/2-((1-math.sqrt(5)) ** n)/2)/math.sqrt(5)


def main():
	logger.info(solve(100))

if __name__ == "__main__":
    main()
