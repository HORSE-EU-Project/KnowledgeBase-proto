# HORSE project 

## WP4 - Knowledge Base prototype
Welcome to the HORSE project's Knowledge Base prototype development repository.

### ⚠️ DISCLAIMER
The contents of this repository are intended solely for testing purposes to assess the functionality of the API. This is not the final implementation of the Knowledge Base (KB) and should not be considered as such. We are actively working on further developments and improvements to the KB, and this repository serves as a testing environment only. Thank you for your understanding.

### ⚙️SETUP REQUIREMENTS
- preferred terminal 
- docker desktop
    - installation guide for Windows: https://docs.docker.com/desktop/install/windows-install/
    - installation guide for Mac: https://docs.docker.com/desktop/install/mac-install/
- docker: check if it is installed using ```docker --version``` in your terminal

### 📄USAGE INSTRUCTIONS
1. Download the repo using git clone 
2. Open Docker Desktop app
3. Open terminal and go into api-proto/
4. Start docker compose using: `docker compose up -d`. The first time it will take a while because it needs to download and install all packages and build the docker image. Once it has finished you should see: 
```
 ✔ Network api-proto_default         Created                    0.1s
 ✔ Container api-proto-web-server-1  Started                    0.3s 
```
5. Open a web browser and go to http://localhost/docs to access the API documentation


The web server in now running and you can send requests to localhost using the API! 🚀🚀

6. When finished, stop docker compose writing in the terminal `docker compose down -v`. Once it has stopped you should see: 
```
 ✔ Container api-proto-web-server-1  Removed                    0.5s 
 ✔ Network api-proto_default         Removed                    0.3s 
```