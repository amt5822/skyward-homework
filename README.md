To run the docker container locally:
- docker build -t serverapp .
- docker run -it serverapp
- open browser
- navigate to localhost:7000/
- navigate to localhost:7000/health/

Note, the docker workflow is triggered when the repository is tagged in the "vx.x.x" format. The python workflow check runs with every pushed commit.
