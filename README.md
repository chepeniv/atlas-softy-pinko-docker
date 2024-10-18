# Docker

## Context

utilizing the orchestration tool `Docker Compose`, here we will create an "infrastructure
for an application that utilizes a reverse proxy, a load balancer, two application servers, and one front-end server"

## High-level Design

one entry-point server that acts as a load balancer and reverse proxy server that 
routes traffic to either the two api servers or the front-end static-content server

the client will never be in direct communication with the front-end server.
our proxy will be the intermediary between the two.

before traffic is redirected to the api servers, it will need to be processed by a
load-balancing algorithm. we will implement a basic round-robin approach.

### round-robin load-balancing 

a method of distributing traffic across multiple nodes in a network. specifically,
in a turn-by-turn cyclical manner.

## References

[docker tutorial](https://docs.docker.com/get-started/introduction/)

