# Stackoverflow Test


## Used technologies

Python


## Project setup ##

**Before cloning** the project - make sure that you have installed all of the packages.

`sudo apt-get install -y build-essential wget g++ git python3.5 python3.5-dev libxml2-dev python3-pip libffi-dev`

And clone the repo.

**After cloning** the repo you must setup environment in project dir.

Enter in you bash shell: `virtualenv .env -p /usr/bin/python3.5`.

Activate the environment `source .env/bin/activate`.

Next you must install requirement libraries: `pip3 install -r requirements.txt`.

### Setup application ###

Create `local.sh` file and move to project directory. That file for application's settings.

Example of local.sh file:

```
#!/usr/bin/env bash


export SECRET_KEY='akspd9u0q92pje01983eD)&*)(^%@(E'
export STACKOVERFLOW_CLIENT_ID='198026349017264389127'
export STACKOVERFLOW_CLIENT_SECRET='dasp[dk09aj98(('
export STACKOVERFLOW_KEY='a;ksdjl;asdhkasj;d(('
export STACKOVERFLOW_DOMAIN_URL='http://localhost:8000'

```

`SECRET_KEY` - application secret key.

`STACKOVERFLOW_CLIENT_ID` - client id from stack overflow.

`STACKOVERFLOW_CLIENT_SECRET` - client secret from stack overflow.

`STACKOVERFLOW_KEY` - client key from stack overflow.

`STACKOVERFLOW_DOMAIN_URL` - domain name for you application (*with http://*) from stack overflow.

`DEBUG` - application debug mode (`False` by default).

`HOST` - application host (`localhost` by default).

`PORT` - application port (`8000` by default).

## Launch application **NOT PRODUCTION** ##

Activate python virtual environment `source .env/bin/actvate`.

Activate `local.sh` settings file `source local.sh`.

Run `python server.py`
