# Running Docker Image on AWS Lightsail

This README provides the steps to run a Docker image on an AWS Lightsail instance.

## 1. Creating an AWS Lightsail Instance

First, you'll need to set up a new Lightsail instance:

1. Navigate to the [Lightsail home page](https://aws.amazon.com/lightsail/) and click the `Create instance` button.
2. Choose `Linux/Unix` platform, and then select `OS Only` and `Amazon Linux 2`.
3. Choose your instance plan (the cheapest should be sufficient for basic applications).

4. Name your instance and click `Create instance`.

Wait a few moments for your instance to be created. You will then see your new instance in the Lightsail home page.

## 2. Connecting to the Instance

1. Click on the instance you created, then click `Connect using SSH`. This will open a new window with a command-line interface.

## 3. Installing Docker on the Instance

First, you need to update the installed packages and package cache on your instance:

```
sudo yum update -y
```

Then, install Docker:

```
sudo amazon-linux-extras install docker -y
```

Start the Docker service:

```
sudo service docker start
```

Add the `ec2-user` to the Docker group so you can execute Docker commands without using `sudo`:

```
sudo usermod -a -G docker ec2-user
```

Log out and log back in again to pick up the new Docker group permissions. You can do this by closing your current SSH terminal window and reconnecting to your instance in a new one.

## 4. Pulling and Running Docker Image

Pull your Docker image:

```
docker pull <your_username>/portfolio-website
```

Now, you can run your Docker image:

```
docker run -d -p 80:80 <your_username>/portfolio-website
```

Your application should now be running on your Lightsail instance, and you should be able to access it by navigating to the public IP address of your instance in your web browser.

**Note**: If your Lightsail instance has a firewall, make sure that it allows traffic on the port that your application is running on (port 80 in this case). You can check and modify this in the `Networking` tab of your Lightsail instance.

## 5. Docker Commands

Here are some useful Docker commands:

- To view running Docker containers, use `docker ps`.
- To stop a running Docker container, use `docker stop <container_id>`.
- To view your Docker images, use `docker images`.

Remember to replace `<your_username>` with your Docker username.
