initialize_git:
	@echo "Github initialization"
	git init 

install:
    @echo "Github initialization"
	pip install -r requirements.txt

setup: initialize_git install

