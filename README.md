# OpenEHR demographic service

> This project is part of Thayse Marques Solis' masters project, yet to be released.

This project is an implementation of a web service which provides access to a storage of patient entries (`PERSON`) and correlated data (`VERSIONED_PARTY`, `VERSION<PARTY>` and `CONTRIBUTION`) according to the OpenEHR Reference Model. The API is detailed on the `api.md` file.

Patients are instances of the `PERSON` class which also meet the restrictions of the `openEHR-DEMOGRAPHIC-PERSON.person-patient.v0` archetype.

> This service depends on the [Demographic Database](https://github.com/ThaySolis/demographic-database) to run.

## Running locally

In order to run this service locally, you must first create the Python virtual environment:

```bash
python3 -m venv venv
```

Then, after activating the virtual environment, you must install all requirements.

```bash
pip install -r requirements.txt
```

Finally, you may run the Python application:

```bash
python app.py
```

## Environment variables

In order to run this application, the following environment variables must be set:

- `PLAIN_HTTP`: if `yes`, the server will run in HTTP mode, else it will run in HTTPS mode.
- `SERVER_PORT`: the port that will receive incoming HTTP requests.
- `SYSTEM_ID`: the system ID to use when generating version identifiers on the system.
- `INCLUDE_USAGE_STATISTICS`: if `yes`, the server will collect usage statisticas and provide an additional route `/usage_statistics` to get usage statistics.
- `USAGE_STATISTICS_MAX_SAMPLES`: the maximum number of timing samples collected for the usage statistics.
- `AUTH_USERNAME`: username that must be used to access this service using HTTP basic authentication.
- `AUTH_PASSWORD`: password that must be used to access this service using HTTP basic authentication.
- `DB_URI`: the host that will be used to connect with the MongoDB database.
- `DB_PORT`: the port that will be used to connect with the MongoDB database.
- `DB_USERNAME`: username that will be used to access the MongoDB database.
- `DB_PASSWORD`: password that will be used to access the MongoDB database.

The `.env` file is provided with sample values for these variables.
