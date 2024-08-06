run:
	@echo "Which part do you want to run? (1, 2, or both)"
	@read part; \
	if [ "$$part" = "1" ]; then \
		ruby day3.rb input.txt 1; \
	elif [ "$$part" = "2" ]; then \
		ruby day3.rb input.txt 2; \
	elif [ "$$part" = "both" ]; then \
		echo "Running part 1:"; \
		ruby day3.rb input.txt 1; \
		echo "Running part 2:"; \
		ruby day3.rb input.txt 2; \
	else \
		echo "Invalid option. Please choose 1, 2, or both."; \
	fi
