# Weather API Proxy

A simple Flask-based Python API server which proxies requests to a free weather API.

## About the API Proxy

The proxy exposes a `/weather` resource, which takes two optional querystring parameters:

1. longitude
2. latitude

The proxy will send these values to the 7timer API behind the scenes, so any errors resulting from the calls are dependant upon valid input latitude and longitude coordinates passed in.

For more information on the 7timer API, please visit http://www.7timer.info/doc.php?lang=en.

## Invoking the API Proxy

Once deployed, query the API proxy as follows:

```xml
/weather?longitude=<LONGITUDE_VALUE>&latitude=<LATITUDE_VALUE>
```

The data will be returned in JSON format, following the schema: http://www.7timer.info/doc.php?lang=en#machine_readable_api

## Building Docker Base Image

1. Clone the project, and `cd` into the cloned directory
2. Run `docker build -t weather-api-proxy-image .`

### Validating The Base Image

1. Run `docker run -d --name weather-api-proxy-container -p 80:5000 weather-api-proxy-image` to spawn the HTTP server as a background container
2. In your browser, access the application using your local Dockerhost URL as the base IP address

- E.G: If your local Docker host URL is _192.168.99.100_, visit http://192.168.99.100/ and validate you see the test message

## CICD

TBA

## Deploying to Kubernetes

TBA

## References

- https://flask.palletsprojects.com/en/2.0.x/#
- http://www.7timer.info/doc.php?lang=en
- https://blog.jcharistech.com/2020/11/02/how-to-create-requirements-txt-file-in-python/
- https://docs.docker.com/language/python/build-images/
- https://www.techiediaries.com/python-unit-tests-github-actions/
