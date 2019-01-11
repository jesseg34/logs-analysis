# Logs Analysis
---------------
* Prints reports from the Udacity Logs Analysis project database
* This app was written In Python 3.7.

Prerequisites
-------------
* Python 3.7.x
* Vagrant
* VirtualBox


Instructions
------------
1. Clone or download the vagrant enviroment from [Udacity](https://github.com/udacity/fullstack-nanodegree-vm.git) 
2. Run command `vagrant up` while targeting the vagrant folder of the repo in step 1.
3. Once the VM is running, execute command `vagrant ssh`
4. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Place the sql file in the vagrant folder
6. Run command `cd /vagrant` to enter the shared vagrant folder while logged into the VM
7. Run command `psql -d news -f newsdata.sql` to import the database
8. Execute the log app by running `python log.py`

Credit
------
Credit goes to the Udacity Full Stack nanodegree program