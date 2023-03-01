initialize_git:
	@echo "Initializing git..."
	git init 
	
install: 
	@echo "Installing..."
	pip install -r requirements.txt

setup: initialize_git install 
