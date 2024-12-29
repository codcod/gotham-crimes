# Makefile
# Interact with the app

HOST = 127.0.0.1
PORT = 8000

# *Default* id of a crime to get or delete. This parameter needs to be added
# when calling a Makefile target that is aware of such variable:
#
# 	$ make api/get-crime ID=2
# 	$ make api/delete-crime ID=2
#
ID = 1

# --- interact with the app: call individual APIs

.PHONY: api/add-crime
api/add-crime:
	@http -b POST http://$(HOST):$(PORT)/api/crimes < tests/load/crime.json

.PHONY: api/get-crime
api/get-crime:
	@echo "Getting crime number: $(ID)"
	@http -b GET http://$(HOST):$(PORT)/api/crimes/$(ID)

.PHONY: api/get-crimes
api/get-crimes:
	@http -b "http://$(HOST):$(PORT)/api/crimes?skip=10&take=2"

.PHONY: api/delete-crime
api/delete-crime:
	@echo "Deleting crime number: $(ID)"
	@http -b DELETE "http://$(HOST):$(PORT)/api/crimes/$(ID)"


# --- interact with the app: load testing

.PHONY: load/wrk
load/wrk:
	wrk -t12 -c500 -d5s --latency "http://$(HOST):$(PORT)/api/crimes?skip=0&take=10"

.PHONY: load/hey
load/hey:
	hey -z 10s -c 50 -t 1 "http://$(HOST):$(PORT)/api/crimes?skip=0&take=10"

.PHONY: load/add-crimes
load/add-crimes:
	hey -z 10s -c 25 -t 12 \
       -m POST \
       -H "Content-Type: application/json" \
       -d '{ \
               "type": "Burglary", \
               "description": "Someone committed a crime", \
               "location": "Gotham", \
               "suspect_name": "Joker", \
               "date_time": "2012-04-23T18:25:43Z", \
               "latitude": 49.80404, \
               "longitude": 9.96233 \
           }' \
       http://$(HOST):$(PORT)/api/crimes

# --- work with code

.PHONY: .pre-commit
.pre-commit:
	pre-commit run --all-files
