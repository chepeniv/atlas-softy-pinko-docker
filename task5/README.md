# Building and Running

starting the docker deamon manually:
```bash
sudo systemctl start docker
```

starting it without the system utility manager :
```bash
sudo dockerd
```

## Backend

### build :

```bash
docker build -f ./back-end/Dockerfile -t softy-pinko-back-end:task3 ./back-end
```

### run :

```bash
docker run -p 5252:5252 -it --rm --name softy-pinko-back-end-task3 softy-pinko-back-end:task3
```

## Frontend

on a separate terminal 

### build :

```bash
docker build -f ./front-end/Dockerfile -t softy-pinko-front-end:task3 ./front-end
```

### run :

```bash
docker run -p 9000:9000 -it --rm --name softy-pinko-front-end-task3 softy-pinko-front-end:task3
```

