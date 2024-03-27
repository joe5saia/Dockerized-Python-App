# Dockerized Python Script

This repo contains a very simple Dockerized python application that makes use of Docker and requirements.txt to
create a reproducible enviroment for exectuing this script. 

## How to Use

To use this container we first need to build it and then run it. To build the container
we need to use the "docker build" command. "Building" a container means taking the container
definition in the Dockerfile and turning it into a useable artifact that can be executed. This
is done using the following command

```bash
docker built -t my_script_app .
```

The `-t` argument stands for "tag" and it gives the container a user friendly name. The "."
argument tells the docker build command to look for the Dockerfile in the current directory.

## Running the script within the container

To run the script we can use the `docker run` command. Because our script takes 
arguments, we need to overwrite the "CMD" in the Dockerfile with the full command
we want to use, including the arguments. 

```bash
docker run -t my_script_app python script.py --first_name John --last_name Doe
```

`docker run -t my_script_app` tells docker to run the container with tag `my_script_app`

`python script.py --first_name John --last_name Doe` tells docker the command that we
want to execute in the container.
