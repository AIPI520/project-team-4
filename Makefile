.PHONY: install run

# Target to install dependencies
install:
	@pip install -r requirements.txt

# Target to run the main.py script
run:
	python3 src/main.py

# Default target
all: install run
