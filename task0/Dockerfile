######## TASK0 ########
# based on ubuntu latest
# apt-get update
# apt-get upgrade -y
# echo "Hello, World!" on the terminal
#
######## DOCKER HUB BUILDING ########
# docker build -t <DOCKER_USERNAME>/<IMAGE_NAME> .
# docker push <DOCKER_USERNAME>/<IMAGE_NAME> 
#
######## CHECKER BUILDING ########
# docker build -f ./Dockerfile -t softy-pinko:task0 .
#
######## RUN CONTAINER (?) ########
# docker run -it --rm --name softy-pinko-task0 softy-pinko:task0

FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y

CMD ["echo", "Hello, World!"]
