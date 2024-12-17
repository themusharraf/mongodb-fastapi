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
  -e MONGO_INITDB_ROOT_PASSWORD=1 \
  mongo:latest
```

### Step 3: Verify MongoDB Container

- Check if the container is running by executing the following command:
```bash
docker ps
```

- Expected Output:
```markdown


CONTAINER ID   IMAGE         COMMAND      CREATED        STATUS       PORTS                      NAMES
abc12345       mongo:latest  "mongo"     10 seconds ago Up 10 secs   0.0.0.0:27017->27017/tcp   mongodb-container
This shows that the MongoDB container is successfully running and accessible through port 27017.
```