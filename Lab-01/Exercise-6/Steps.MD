In this exercise the student is going to explain different concepts to/with the group. It is important to grasp the concepts of Docker and some base-knowledge.

# Your tasks:
1. **Explain what a Dockerfile is.**
    1. How does it work?
        1. "A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession."
    2. Which instructions can be used?
        1. FROM, RUN, CMD, ENTRYPOINT, WORKDIR, COPY, ADD, EXPOSE, LABEL
    3. What do the above-mentioned instructions do?
        1. `FROM` = A FROM command allows you to create a base image such as an operating system, a programming language, etc. All the instructions executed after this command take place on this base image
        2. `RUN` = A RUN instruction is used to run specified commands. You can use several RUN instructions to run different commands. But it is an efficient approach to combine all the RUN instructions into a single one as each RUN command creates a new cache layer 
        3. `CMD` = If you want to run a docker container by specifying a default command that gets executed for all the containers of that image by default, you can use a CMD command
        4. `ENTRYPOINT` = The difference between ENTRYPOINT and CMD is that, if you try to specify default arguments in the docker run command, it will not ignore the ENTRYPOINT arguments.
        5. `WORKDIR` = You can specify your working directory inside the container using the instruction.
        6. `COPY` = This instruction allows you to copy a directory from your local machine to the docker container.
        7. `ADD` = Similar to COPY instruction, you can use ADD to copy files and folders from your local machine to docker containers. However, ADD also allows you to copy files from a URL as well as a tar file.
        8. `EXPOSE` = The EXPOSE instruction inside the dockerfile informs that the container is listening to the specified port in the network. The default protocol is TCP.
        9. `LABEL` = You can use a LABEL instruction to add description or meta data for a docker image. Its a key−value pair.
2. **Explain how a Docker image is built.**
    1. Which options do you know?
        1. "docker build", -t (TAG), -f (FILENAME), PATH-TO-DOCKERFILE
    2. What are they used for?
        1. `docker build` = the base command for building images
        2. `-t` (TAG) = a tag used after the base command to give the image a name
        3. `-f` (FILENAME) = a tag that can be used after the base command to specify a dockerfile thats named something else than "Dockerfile"
        4. `PATH-TO-DOCKERFILE` = To specify the path to the dockerfile
3. **Explain how a Docker container is runned.**
    1. Which options do you know?
        1. The HyperVisor spins up a virtual environment (the container) and boots the image up and listens to the entrypoint.
        2. "docker run", -it, -p, DOCKER-IMAGE, argument
    2. What are they used for?
        1. `docker run` = the base command for running images
        2. `-it` = a tag used after the base command to create interactive processes
        3. `-p` = is the option to expose ports (-p <HOST-PORT>:<CONTAINER-PORT>)
        4. `DOCKER-IMAGE` = the name for the docker image that should be runned
        5. argument = makes it possible for us to enter the container and interact with it under runtime. (e.g "bash")
