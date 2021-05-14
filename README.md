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

## Building Docker Base Image Locally

1. Clone the project, and `cd` into the cloned directory
2. Run `docker build -t weather-api-proxy-image .`

### Validating The Base Image

1. Run `docker run -d --name weather-api-proxy-container -p 80:5000 weather-api-proxy-image` to spawn the HTTP server as a background container
2. In your browser, access the application using your local Dockerhost URL as the base IP address

- E.G: If your local Docker host URL is _192.168.99.100_, visit http://192.168.99.100/ and validate you see the test message

## CICD

Continuous integration is setup to use `Github Actions` via the `.github/workflows/python-app.yml` and `.github/workflows/docker-publish.yml` files.

### Branching strategy

Were I part of a team, I'd use either Gitflow or Trunk-based development. However, for this small toy project, each commit to `master` triggers the build and unit tests (because I am the sole contributor and I want a quick feedback loop).

### Unit Testing

This is done via Github Actions workflow, in `.github/workflows/python-app.yml`. These use vanilla `pytest` and call Python unit test files on commit to `master`

### Container Build

This is done via Github Actions workflow, in `.github/workflows/docker-publish.yml`. This will run a series of Dockerfile linting tests, and push the completed image to Github's Container Registry (currently in Beta as of this writing).

You can pull the package directly via CLI: `docker pull docker.pkg.github.com/diamonddelt/weather-api-proxy/weather-api-proxy:latest`.

## Deploying to Kubernetes

1. Push the built image `weather-api-proxy-image` to any container registry of your choice.
2. Change the image tag from the registry within the `kubernetes/weather.yaml` file
3. Connect to your Kubernetes cluster, and run `kubectl apply -f kuberntes/weather.yaml`
4. The API is exposed as a NodePort service at port 30010, so if your worker node(s) has a routable IP/DNS (for example, 10.200.12.89), you could reach this API at `http://10.200.12.89:30010`

## References

- https://flask.palletsprojects.com/en/2.0.x/#
- http://www.7timer.info/doc.php?lang=en
- https://blog.jcharistech.com/2020/11/02/how-to-create-requirements-txt-file-in-python/
- https://docs.docker.com/language/python/build-images/
- https://www.techiediaries.com/python-unit-tests-github-actions/
