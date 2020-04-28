NAME := hydra-debug
TAG	:= $$(git rev-parse --short=8 HEAD)
IMG	:= ${NAME}:${TAG}
LATEST := ${NAME}:latest

build:
	@docker build -t ${IMG} .
	@docker tag ${IMG} ${LATEST}

dev: build
	@docker tag ${IMG} ${NAME}:dev

test: build
	@docker tag ${IMG} ${NAME}:test

live: build
	@docker tag ${IMG} ${NAME}:live
