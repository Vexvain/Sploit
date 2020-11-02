 ![SPLOIT](https://i.ibb.co/JRSjb6H/image-2020-11-02-172835.png)

# Docker Compose
Using Docker Compose is by far the easiest way to get Sploit up and running without too much of a hassle.
```
git clone https://github.com/Vexvain/Sploit.git
cd Sploit/Docker
docker-compose run --rm sploit
```

##### Docker
Just using Docker.
```
git clone https://github.com/Vexvain/Sploit.git
cd Sploit/Docker
# If you wish to edit default postgres service details, edit database.yml. Should work out of the box
# nano database.yml
docker network create -d bridge haknet
docker run --network haknet --name msfdb -e POSTGRES_PASSWORD=s3cr3t -d postgres
docker build -t sploit .
docker run -it --network haknet -p 80:80 -p 443:443 -p 4444:4444 sploit
```

##### Cloning
On any Linux system the following should work;

```bash
git clone https://github.com/Vexvain/Sploit
cd Sploit
chmod +x install.sh
./install.sh
```

Sploit is compatible with macOS, however, you have to be inside a virtual environment for it to run successfully

```bash
sudo -s << '_EOF'
pip2 install virtualenv --user
git clone https://github.com/Vexvain/Sploit.git
virtualenv <PATH-TO-YOUR-ENV>
source <PATH-TO-YOUR-ENV>/bin/activate
cd <PATH-TO-SPLOIT>
pip2 install -r requirements.txt
chmod +x install.sh
./install.sh
python sploit.py
_EOF
```

## Usage

Starting the program with `python sploit.py` will open a Sploit terminal session. The options for which are as follows.
```
1. Usage And Legal
2. Gather Hosts
3. Custom Hosts
4. Add Single Host
5. View Gathered Hosts
6. Exploit Gathered Hosts
99. Quit
```

Choosing option `2` will prompt you for a platform specific search query. Enter `IIS` or `Apache` in example and choose a search engine. After doing so the collected hosts will be saved to be used in the `Exploit` component.

Type `python sploit.py -h` to display all the options available to you

```
usage: python sploit.py -[c|z|s|a] -[q] QUERY
                            [-C] WORKSPACE LHOST LPORT [-e] [--whitewash] PATH
                            [--ruby-exec] [--msf-path] PATH [-E] EXPLOIT-FILE-PATH
                            [--rand-agent] [--proxy] PROTO://IP:PORT [-P] AGENT

optional arguments:
  -h, --help            show this help message and exit

search engines:
  possible search engines to use

  -c, --censys          use censys.io as the search engine to gather hosts
  -z, --zoomeye         use zoomeye.org as the search engine to gather hosts
  -s, --shodan          use shodan.io as the search engine to gather hosts
  -a, --all             search all available search engines to gather hosts

requests:
  arguments to edit your requests

  --proxy PROTO://IP:PORT
                        run behind a proxy while performing the searches
  --random-agent        use a random HTTP User-Agent header
  -P USER-AGENT, --personal-agent USER-AGENT
                        pass a personal User-Agent to use for HTTP requests
  -q QUERY, --query QUERY
                        pass your search query

exploits:
  arguments to edit your exploits

  -E PATH, --exploit-file PATH
                        provide a text file to convert into JSON and save for
                        later use
  -C WORKSPACE LHOST LPORT, --config WORKSPACE LHOST LPORT
                        set the configuration for MSF (IE -C default 127.0.0.1
                        8080)
  -e, --exploit         start exploiting the already gathered hosts

misc arguments:
  arguments that don't fit anywhere else

  --ruby-exec           if you need to run the Ruby executable with MSF use
                        this
  --msf-path MSF-PATH   pass the path to your framework if it is not in your
                        ENV PATH
  --whitelist PATH      only exploit hosts listed in the whitelist file
```


## Dependencies
_Note_: All dependencies should be installed using the above installation method, however, if you find they are not:

Sploit depends on the following Python2.7 modules.

```
requests
psutil
```

Should you find you do not have these installed get them with pip like so.

```bash
pip install requests psutil
```

or

```bash
pip install -r requirements.txt
```

Since the program invokes functionality from the Metasploit Framework, you need to have this installed also. Get it from Rapid7 by clicking [here](https://www.rapid7.com/products/metasploit/).
