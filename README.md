Description
===========

#### Production

The latest version of [Ghost](http://ghost.org/about/) installed with
[Nginx](http://wiki.nginx.org/Main/), [Node.js](http://nodejs.org/) and
a Cloud Database running [MySQL 5.1](http://www.mysql.com/about/).

This template will only function with RackConnect v3.


Instructions
===========

#### Getting Started

Ghost is a new blogging platform dedicated to providing a simple, easy to use
approach to blogging. Ghost allows you to write and publish your own blog,
giving you the tools to make it easy and even fun to do. It's simple,
elegant, and designed so that you can spend less time messing with making
your blog work - and more time blogging.

The first step with your new blog is to navigate to `/ghost/signup` where you
will create the your user. Ghost currently only supports one user at this
time. After filling out this info, you will be redirected to the admin panel
where you can start customizing your blog and adding new posts. To access the
admin panel again, navigate to `/ghost`.

For more information on using Ghost please check out Ghost's [usage
forums](https://ghost.org/forum/using-ghost/).

#### Plugins

Ghost is new and is still in heavy development. However, there are already
some plugins and themes to help customize your experience. Checkout the Ghost
[Marketplace](http://marketplace.ghost.org/) for links. Users coming from
WordPress may also be interested in this [WordPress
plugin](http://wordpress.org/plugins/ghost/) to help migrate data from
WordPress to Ghost.

#### Details of Your Setup
This deployment was stood up using [Ansible](http://www.ansible.com/).
Once the stack has been deployed, Ansible will not run again unless you update the
stack. **Any changes made to the configuration may be overwritten when the stack
is updated.**

Ghost was installed from the latest version available.  It has been installed to
/var/www/ghost/.  Ghost is running on port 2368.

[nginx](https://www.nginx.com/) has been configured to serve static content
for Ghost, as well as to forward all HTTP and HTTPS connections to Ghost.

MySQL is being hosted on a Cloud Database instance, running MySQL 5.1.
Backups for MySQL are provided by [Holland](http://wiki.hollandbackup.org/),
which is running on the server.

#### Logging in via SSH
The private key provided with this deployment can be used to log in as
root via SSH. We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).
This key can be used to log into all servers on this deployment.
Additionally, passwordless authentication is configured from the Master
server to all secondary servers.


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::RandomString
  * OS::Heat::SoftwareConfig
  * OS::Heat::SoftwareDeployment
  * OS::Nova::KeyPair
  * OS::Nova::Server
  * OS::Trove::Instance
  * Rackspace::Cloud::BackupConfig
  * Rackspace::CloudMonitoring::Check
  * Rackspace::RackConnect::PublicIP
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `ghost_url`: Domain to use with Ghost Site (Default: example.com)
* `ghost_email`: E-mail Address for Ghost Admin User (Default: admin@example.com)
* `rc_network_name`: Name or UUID of RackConnected network to attach this server to 
* `flavor`: Flavor of Cloud Server to use for Ghost (Default: 4 GB General Purpose v1)
* `database_disk`: Size of the Cloud Database volume in GB (Default: 5)
* `database_flavor`: Flavor for the Cloud Database (Default: 1GB Instance)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `ghost_public_ip`: Server Public IP 
* `ghost_admin_url`: Ghost Admin URL 
* `ghost_public_url`: Ghost Public URL 
* `mysql_user`: Database User 
* `mysql_password`: Database Password 
* `ssh_private_key`: SSH Private Key 

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
