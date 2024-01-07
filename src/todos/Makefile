APP_NAME = todos
IMAGE_TAG ?= $(shell git rev-parse --short HEAD)

run:
	pants run main.py

fmt:
	pants fmt ::

lint:
	pants lint ::

test:
	pants test ../../tests/src/$(APP_NAME)::

docker-build:
	APP=$(APP_NAME) ENVIRONMENT=dev GIT_COMMIT=$(IMAGE_TAG) pants package ./Dockerfile \
		--docker-default-repository=$(REPOSITORY_NAME)/{name}/{build_args.ENVIRONMENT}

docker-run:
	APP=$(APP_NAME) ENVIRONMENT=dev GIT_COMMIT=$(IMAGE_TAG) pants run ./Dockerfile \
		--docker-run-args="-p 8000:8000" \
		--docker-default-repository=$(REPOSITORY_NAME)/{name}/{build_args.ENVIRONMENT}

docker-push:
	APP=$(APP_NAME) ENVIRONMENT=dev GIT_COMMIT=$(IMAGE_TAG) pants publish ./Dockerfile \
		--docker-default-repository=$(REPOSITORY_NAME)/{name}/{build_args.ENVIRONMENT}
