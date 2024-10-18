# docker in 100 seconds - fireship

because virtual machines simulate the entire hardware architecture
as well as running a full operating system, they tend to be slow

docker on the other hand abstracts the kernel/os by using an intermediary
layer to communicate with the actual underlying os

the three primary components of docker are

### the `Dockerfile`

this tells docker how to build an image
```dockerfile
FROM ubuntu:20.04

# executes command in the image construction
RUN apt-get install sl

ENV PORT=8080

# command to run upon container startup
CMD ["echo", "hello, world!"]
```

### the image

this is a snapshot of the software and dependencies.
images are immutable and are used to initialize and run multiple containers.
create image file: 
```bash
docker build -t appname ./path/to/Dockerfile/
```

### the container

to run an image as a container execute:
```bash
docker run appname
```
docker cantainer apps can run simultaneously on multiple machines, clouds, pram, or wherever

# what is docker in 5 minutes - techsquidtv

it is often described as system agnostic while each instance runs in isolation.
each container typically runs a very specific task and then networked with other
containers for more functionality.

check created images: `docker images`

get images from docker hub : `docker pull imagename:optional_tag`

view running containers : `docker container ls`

## docker compose

# docker containers 101 - networkchuck

docker containers are meant to replace virtual machines in usecases
where only a single app is meant to run (not a full operating sys)

whereas virtual machines virtualize hardware, docker containers virtualize
the operating system

docker containers are quarantined and secure

access a running container : `docker exec -it appname program`

example: `docker exec -it mycentos bash`

# intro to docker i wish i had when i started - typecraft

 
