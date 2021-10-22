.PHONY: test train experiment
IMAGE_NAME = ameron/sidecar-model-service-example:1.0.0

default:
	cat Makefile

test:
	pytest

image: test
	docker build -f docker/Dockerfile -t ${IMAGE_NAME} .

run: image
	docker run -p 8000:8000 --rm --name sidecar-model-service-example --env-file docker/local.env ${IMAGE_NAME}

stop:
	docker stop sidecar-model-service-example && docker rm sidecar-model-service-example
