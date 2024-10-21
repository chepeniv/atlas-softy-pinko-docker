######## TASK2 ########

######## BUILD IMAGE ########
# docker build -f ./front-end/Dockerfile -t softy-pinko-front-end:task2 ./front-end

######## STARTUP CONTAINER ########
# docker run -p 9000:9000 -it --rm --name softy-pinko-front-end-task2 softy-pinko-front-end:task2

######## VERIFY ########
# localhost:9000

FROM nginx:latest

COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end 
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

EXPOSE 9000

