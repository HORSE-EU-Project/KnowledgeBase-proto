# HORSE project 

## WP4 - Knowledge Base
Welcome to the HORSE project's Knowledge Base development repository.

### ⚠️ DISCLAIMER
The contents of this repository are intended solely for testing purposes to assess the functionality of the API. This is not the final implementation of the Knowledge Base (KB) and should not be considered as such. We are actively working on further developments and improvements to the KB, and this repository serves as a testing environment only. Thank you for your understanding.

### ⚙️SETUP REQUIREMENTS
- preferred terminal 
- docker desktop
    - installation guide for Linux: https://docs.docker.com/desktop/install/linux-install/
    - installation guide for Windows: https://docs.docker.com/desktop/install/windows-install/
    - installation guide for Mac: https://docs.docker.com/desktop/install/mac-install/
- docker: check if it is installed using ```docker --version``` in your terminal

### 📄USAGE INSTRUCTIONS
1. Download the repo using git clone 
2. Open Docker Desktop app
3. Open terminal and go into api-proto/
4. Install postgres docker image using `docker pull postgres`. When it's done you should see a list of 
```
710e142705f8: Pull complete
cb628c265f09: Pull complete
```
5. Start docker compose using: `docker compose up -d`. The first time it will take a while because it needs to download and install all packages and build the docker image. Once it has finished you should see: 
```
 ✔ Network api-proto_default               Created                       0.1s 
 ✔ Container api-proto-web-server-1        Started                       0.1s 
 ✔ Container attacks-mitigations-database  Started                       0.2s 
```
6. Open a web browser and go to http://localhost/docs to access the API documentation


The web server and the attacks-mitigations database are now running. You can send requests to localhost using the API! 🚀🚀

7. When finished, stop docker compose writing in terminal `docker compose down -v`. Once it has stopped you should see: 
```
 ✔ Container api-proto-web-server-1        Removed                       0.5s 
 ✔ Container attacks-mitigations-database  Removed                       0.7s
 ✔ Network api-proto_default               Removed                       0.3s 
```