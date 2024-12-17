# MongoDB with Docker

This guide demonstrates how to create and run a **MongoDB container** using **Docker**. It includes all the necessary steps to get MongoDB up and running on your machine.

## Step 1: Pull the MongoDB Docker Image

Run the following command to download the latest MongoDB image from Docker Hub:

```bash
docker pull mongo:latest
```

### Step 2: Run the MongoDB Container

- Use the following command to start a MongoDB container:
```bash
docker run -d \
  --name mongodb-container \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret \
  mongo:latest
```
