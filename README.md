
### Getting into Docker


Docker is a platform that allows us to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime
Docker uses resource isolation in the OS kernel to run multiple containers on the same OS. 

### Steps for creating a docker image for a Flask app

The folder  DockerAPP in this repository contains a subfolder named UI, which contains a simple UI for Flask app. This flask app renders text **Intro to docker** 
and there's a `about` section. This is all about Flask app.

Using docker we will be creating an image for this Flask app, so that we can run it on any platform without getting worried about dependencies.

First we need to create a file named `Dockerfile`. This is the standard name and should always be same.
Inside this file we need to include dependencies required for running the application we have, along with the command to run it.

```
FROM python:3.6
RUN pip install FLASK==0.11.1
WORKDIR /UI
COPY UI /UI
CMD [ "python" ,"app.py"]
```

```
FROM python:3.6
```
This means that our image is dependent on base image python:3.6. So docker will first pull this image from dockerhub.

```
RUN pip install FLASK==0.11.1
```
This will run command to install Flask

The command ```WORKDIR /UI``` specifies that code of our concern resides inside directory named UI

```COPY UI /UI``` will copy the UI directory into docker with name as `UI`.

Now , the docker has python and flask installed in it and code for the Flask application has also been copied.So next step is all about running the `app.py` file to run flask application.

```CMD [ "python" ,"app.py"]``` means docker need to run command `python app.py` .

With this command Flask application will run and will be accesible from our browser of host machine.


Now we need to build docker image using this Dockerfile.
Command for creating image is:


```
docker image build -t flask_in_docker . 
```
This will create a docker image named `flask_in_docker`.

`.` at the end of the command means Dockerfile is present in the same directory from where we are running this command.


Now the image named `flask_in_docker` has been created.

With this image we can run the flask application on any host machine having docker installed on it.
You can check the list of available images using command:

```docker image ls```

To run the application with docker image, run command:

```docker run -p 5000:5000 -d flask_in_docker```

`p 5000:5000` is used for port binding between host machine and docker container.
First part denotes hostport and second part denotes port on docker container where flask application is supposed to run.

The URL which can be used to access the UI will be shown in terminal after the command runs successfully.



