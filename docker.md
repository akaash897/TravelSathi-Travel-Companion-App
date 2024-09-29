## Outline of running and benchmarking the app with Docker (Containerization)

## Installation of Docker Desktop for Windows

1. Follow this [tutorial](https://www.youtube.com/watch?v=XgRGI0Pw2mM&ab_channel=ProgrammingKnowledge2)
2. Search Turn on windows features on and off, and enable Virtual machine platform


## Creation of Image, Dokerfile and .dockerignore

1. This containes configurations for docker image creation
2. Create image using command 
   ```bash     
   docker build .
   ```

## Running the app 

1. Run the container with parameters CPU=1 and Memory=2GB:
   Create image using command 
   ```bash     
   docker run -p 5000:5000 --cpus="1.0" --memory="2g" <image-name>
   ```

## Benchmarking using Apache bench
1. In new terminal, run benchmarking with 100 connection with 1000 requests:
   ```bash
   ab -c 100 -n 1000 http://localhost:5000/
   ```




