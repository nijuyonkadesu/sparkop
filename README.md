# Pyspark workshop ~


## Installation of pyspark in windows
follow [this](https://medium.com/@dipan.saha/getting-started-with-pyspark-day-1-37e5e6fdc14b) and try that sample program

## spark df vs pandas df

spark supports:
- A distributed collection of data grouped into named columns
- lazy & parallel computation
- in memory operations
- immutable

## install hadoop and pyspark
- (windows) https://medium.com/@dipan.saha/getting-started-with-pyspark-day-1-37e5e6fdc14b
- https://cloudzy.com/blog/install-hadoop-on-ubuntu/ 
- https://linuxgenie.net/how-to-install-pyspark-on-ubuntu-22-04/

## install redis 
- https://redis.io/docs/install/install-stack/linux/

## install docker
- https://docs.docker.com/engine/install/ubuntu/#installation-methods
- https://docs.docker.com/engine/install/linux-postinstall/

```bash
sudo systemctl enable redis-stack-server
sudo systemctl start redis-stack-server
redis-cli -h 127.0.0.1 -p 6379
FT.TAGVALS idx:shoes brand
FT.SEARCH idx:shoes "@colors:{silver} @brand:{Unique Bargains} women"
FT.SEARCH idx:shoes "@brand:{Brinley\\ Co\\.}"
redis-cli -h 127.0.0.1 -p 6379 keys product:* | xargs redis-cli DEL
```
## Tip
Do not save special characters in Redis.
Use redis as cache, not as search engine 😁

## Debug
```bash
FT._LIST
KEYS *user*
```
## Nice findings
- sc <- spark context [used to perform distributed operation, processing in parallel, writing to external storage]
- [parquet](https://www.linkedin.com/pulse/why-apache-parquet-instead-csv-files-mariano-silva)
- [all about pyspark](https://github.com/spark-examples/pyspark-examples)
- shard redis database - for multicore processing
- 1DB per redis instance (to reduce expiry key overhead) - 1 DB per feature
- clustering
- [redis examples](https://redis.readthedocs.io/en/stable/examples)

## Reffered Articles:
- https://www.linkedin.com/pulse/redis-design-patterns-high-volume-applications-melvin-rook
- 

## TODO
- read basics of dataframes

### Notes
Q: explain me. what is this concept of creating a new user, just for hadoop, then configuring a ssh client for local host, 
moving files to usr/local/hadoop, and giving ownership to that non sudo hadoop user.

and, magically, all users are able to access hadoop services.

A: The process you described involves several steps, each serving a specific purpose in setting up Hadoop on a Linux system. Let's break down each part:
1. **Creating a new user for Hadoop**: This is a common practice in Linux systems to isolate the Hadoop processes and files from other system processes and files. By creating a dedicated user for Hadoop, you can easily manage the permissions and ownership of Hadoop-related files. This way, you avoid potential conflicts with other system processes and files. This user is often referred to as a "non-sudo" user because it doesn't have superuser privileges, which is a good security practice [Source 0](https://learnubuntu.com/install-hadoop/), [Source 3](https://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/), [Source 4](https://medium.com/@madihaiqbal606/apache-hadoop-3-3-6-installation-on-ubuntu-22-04-2-lts-wsl-for-windows-bb57ed599bc6).
2. **Configuring SSH for the new user**: SSH (Secure Shell) is a protocol that provides secure remote login capabilities. It's essential for managing and interacting with Hadoop clusters. By generating an SSH key pair for the new user, you enable the user to authenticate themselves securely over SSH. This is particularly important in a multi-node Hadoop cluster where secure communication between nodes is crucial [Source 0](https://learnubuntu.com/install-hadoop/), [Source 4](https://medium.com/@madihaiqbal606/apache-hadoop-3-3-6-installation-on-ubuntu-22-04-2-lts-wsl-for-windows-bb57ed599bc6).
3. **Moving files to `/usr/local/hadoop` and changing ownership**: After downloading and extracting the Hadoop distribution, you move the extracted files to `/usr/local/hadoop`. This is a standard location for installing software on Unix-like operating systems. Changing the ownership of the Hadoop directory to the new user ensures that this user has the necessary permissions to read, write, and execute the Hadoop files [Source 3](https://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/).
4. **Accessing Hadoop services for all users**: The reason all users can access Hadoop services after setting up Hadoop under a specific user is because Hadoop itself doesn't enforce user-specific access control. Instead, Hadoop leverages the underlying Unix/Linux user and permission model. So, if a user has the necessary permissions to access a file or directory, they can do so, regardless of whether they are the owner of the file or directory or not. This is why you might see that all users can access Hadoop services after setting up Hadoop under a specific user [Source 3](https://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/).

## Postman installation in ubuntu
Yes, you can move it to the `/usr/local/bin` directory, which is typically included in the `PATH` and accessible to all users. Here are the steps to install Postman in Ubuntu from the `postman-linux-x64.tar.gz` file and make it available to all users:
1. Extract the tarball file. Replace `<file-name>` with the name of your file.
```bash
$ tar -xvzf <file-name>.tar.gz
```
2. Move the extracted Postman directory to `/usr/local/bin`.
```bash
$ sudo mv Postman /usr/local/bin/Postman
```
3. Create a symbolic link to the Postman executable in the `/usr/bin` directory.
```bash
$ sudo ln -s /usr/local/bin/Postman/Postman /usr/bin/postman
```
4. Create a `postman.desktop` file in `/usr/share/applications` to make Postman visible in the application menu for all users.
```bash
$ sudo vim /usr/share/applications/postman.desktop
```
5. Add the following content to the `postman.desktop` file.
```bash
[Desktop Entry]
Version=1.0
Name=Postman
Comment=Postman Desktop
Exec=/usr/bin/postman
Path=/usr/local/bin/Postman
Icon=/usr/local/bin/Postman/app/resources/app/assets/icon.png
Terminal=false
Type=Application
Categories=Development;
```
6. Validate your desktop file.
```bash
$ desktop-file-validate /usr/share/applications/postman.desktop
```
7. If you don't see any errors, you should be able to see the Postman icon in your dash. If you can't see the icon, update the desktop database.
```bash
$ sudo update-desktop-database
```
8. If you still can't see the icon, try logging out and logging back into your system [Source 4](https://tech.raturi.in/how-install-and-use-postman).
