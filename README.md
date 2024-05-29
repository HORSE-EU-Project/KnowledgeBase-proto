# HORSE project 

## WP4 - Knowledge Base
Welcome to the HORSE project's Knowledge Base development repository.

## ⬆️ LATEST UPDATES 
If this is not the first time you run the Knowledge Base and you want to use the latest updates, please follow the instructions:
1. Open Docker desktop
2. Delete "knowledgebase-proto" from containers

<img src="./src/images/knowledgebase-proto-docker-desktop.png" width="60%" />

3. Delete "knowledgebase-proto-web-server" from images

<img src="./src/images/docker-desktop-images.png" width="20%" /> <img src="./src/images/delete-image-web-server.png" width="80%" />

4. Go into the main folder of this repo, called "KnowledgeBase-proto". If there is a folder called "db", delete it.

<img src="./src/images/delete-db.png" width="15%" />

5. Now that your environment is clean again, follow "Usage Instructions" starting from point 5: `docker compose up -d`.

Enjoy 😀

### ⚠️ DISCLAIMER
The contents of this repository are intended solely for testing purposes to assess the functionality of the API. This is not the final implementation of the Knowledge Base (KB) and should not be considered as such. We are actively working on further developments and improvements to the KB, and this repository serves as a testing environment only. Thank you for your understanding.

### 📖 ABOUT THE KNOWLEDGE BASE
The Knowledge Base (KB) is a centralized database for the HORSE project, designed to store and provide essential information on attack mitigations. It retrieves a prioritized list of mitigation measures for specific attacks, including detailed descriptions to guide users on their application. Enhanced with AI, the KB offers intelligent responses, improving decision-making and security.

### ⚙️ SETUP REQUIREMENTS
- preferred terminal 
- docker desktop
    - installation guide for Linux: https://docs.docker.com/desktop/install/linux-install/
    - installation guide for Windows: https://docs.docker.com/desktop/install/windows-install/
    - installation guide for Mac: https://docs.docker.com/desktop/install/mac-install/
- docker: check if it is installed using ```docker --version``` in your terminal

### 📄 USAGE INSTRUCTIONS
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
 ✔ Container api-proto-web-server-1        Started                       8.7s 
 ✔ Container attacks-mitigations-database  Started                       8.7s 
```
6. Open a web browser and go to http://localhost/docs to access the API documentation


The web server and the attacks-mitigations database are now running. You can send requests to localhost using the API! 🚀🚀

7. When finished, stop docker compose writing in terminal `docker compose down -v`. Once it has stopped you should see: 
```
 ✔ Container api-proto-web-server-1        Removed                       0.5s 
 ✔ Container attacks-mitigations-database  Removed                       0.7s
 ✔ Network api-proto_default               Removed                       0.3s 
```