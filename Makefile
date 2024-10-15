# Makefile for eve_playground Project

# Variables
PROJECT_DIR=backend
VENV_DIR=.venv
DOCKER_IMAGE=backend-lms
DOCKER_CONTAINER=backend-lms

.PHONY: env install run build docker-run docker-stop docker-remove clean

# Target to create a Python virtual environment
env:
	@echo "Creating Python virtual environment in $(VENV_DIR)..."
	python3 -m venv $(VENV_DIR)

# Target to install Python dependencies
install: env
	@echo "Activating virtual environment and installing dependencies..."
	@. $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r $(PROJECT_DIR)/requirements.txt

# Target to run the application
run:
	@echo "Activating virtual environment and running the application..."
	@. $(VENV_DIR)/bin/activate && python -m backend

# Target to build the Docker image
build:
	@echo "Building Docker image $(DOCKER_IMAGE)..."
	docker build -t $(DOCKER_IMAGE) .

# Target to run the Docker container
docker-run:
	@echo "Running Docker container $(DOCKER_CONTAINER)..."
	docker run -d -p 5000:5000 --name $(DOCKER_CONTAINER) --env-file $(PROJECT_DIR)/.env $(DOCKER_IMAGE)

# Target to stop the Docker container
docker-stop:
	@echo "Stopping Docker container $(DOCKER_CONTAINER)..."
	docker stop $(DOCKER_CONTAINER)

# Target to remove the Docker container
docker-remove:
	@echo "Removing Docker container $(DOCKER_CONTAINER)..."
	docker rm $(DOCKER# Makefile for eve_playground Project

# Target to clean up virtual environment and temporary files
clean:
	@echo "Cleaning up: removing virtual environment and temporary files..."
	rm -rf $(VENV_DIR)
	@echo "Clean up completed."

# Target to seed the database with sample data
seed:
	@echo "Seeding the database with sample data..."
	@. $(VENV_DIR)/bin/activate && python -m namiz.seed

test:
	@echo "Running tests"
	PYTHONPATH="." pytest namiz --cov=namiz -v