# Tor Blacklist

Tor Blacklist is an API that returns a list of tor ips (from https://www.dan.me.uk/torlist/), crossing the data with your own whitelist.

You can:
  - Saves a whitelist to database.
  - Get a blacklist, based on your own whitelist.
  - Get a blacklist from https://www.dan.me.uk/torlist/ (like a proxy)

### Tech

Tor Blacklist uses a number of projects to work properly:

* [Python]
* [Flask]
* [Docker]

### Installation

Tor Blacklist requires [Docker](https://www.docker.com/) to run.

Install the dependencies and start the server.

```sh
$ make install
$ make build
$ make run
```

### Using

Tor Blacklist has 3 endpoint.

##### GET /blacklist-proxy
This endpoint just returns a list of ips from https://www.dan.me.uk/torlist/ (like a proxy).

##### GET /blacklist
This endpoint returns a list of  ips, removing your whitelist from this list.

##### POST /whitelist
This endpoint should receive an ip, and save it to the database.

Body format:
```sh
{
    "ip": "111.111.111.111"
}
```

### Todos

 - To implement POST endpoint to save whitelist in a database
