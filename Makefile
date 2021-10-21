# usage make start
# Used to run the main application
start: 
	@docker-compose down && \
	docker-compose build --pull --no-cache && \
	docker-compose \
		-f .ci/docker-compose.yml \
	up -d --remove-orphans

# usage make test
# This command will run a docker container without persistant data
# Ideally used to test our work
test:
	@docker-compose down && \
	docker-compose build --pull --no-cache && \
	docker-compose \
		-f docker-compose.yml \
		-f docker-compose.test.yml \
		up -d --remove-orphans