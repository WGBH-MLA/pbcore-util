# pbcore-util

Helpful tools for the [PBCore](pbcore.org) metadata standard.

## Running Locally

### Clone the git repository

From a terminal
```
# Clone the Github repository.
git clone git@github.com:WGBH-MLA/pbcore-util.git

# Go into the application's root directory.
cd pbcore-util
```

### Start the application
```
docker compose up dev
```

This uses the configuraiton in [`docker-compose.yml`](docker-compose.yml) to start a Docker container called `pbcore-util-dev-1` and with port-forwarding on port 8000, and 

### View OpenAPI interface

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see OpenAPI web interface. This interface is automatically generated according to the OpenAPI standard, and provides documentation on how to use each endpoint of the application's API and interactive form components for trying it out.

### Stop and restart the application

From the terminal where you stared the application, simply hit Ctrl-C and wait for the all the workers to stop. You may need to stop/restart the application to see changes you have made. Sometimes you must explicitly rebuild the Docker image in order for your changes to take effect, in which case you can pass the `--build` flag to the `docker compose` command:
```
docker compose up dev --build
```
### Run tests

This application uses pytest for testing. You can run tests using the `test` service defined in `docker-compose.yml` with this command:
```
docker compose --rm run test
```
> [!TIP]
> The `--rm` flag will automatically remove the container once `pytest` has finished running, helping you avoid an accumulation of stopped containers that will never be started again.