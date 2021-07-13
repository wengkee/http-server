#  HTTP Server
Simple HTTP server written in Python 3 which will read a file from and serve it to the page.


## Prequisite
* Install Python 3 
* Prepare a content file
* (optional) Install `keytool` for generating PEM file for hosting with HTTPS

## Quickstart
### HTTP 
```
$ python http-server.py -h
usage: http-server.py [-h] [-p, --port port] [-a, --address address] filename

Host a HTTP/HTTPS server

positional arguments:
  filename              the filename of the data file to be hosted by the
                        server

optional arguments:
  -h, --help            show this help message and exit
  -p, --port port       the port of the server
  -a, --address address
                        the address of the server
```

Run the following to host on http://127.0.0.1:8080

 ```
 $ python http-server.py hello-world.txt
 ```

Check it out
```
$ curl -s http://127.0.0.1:8080
Hello World
```

### HTTPS
1. Generate a PEM file
 ```
$ chmod u+x keystore/gen_pem.sh && ./keystore/gen_pem.sh
```

2. Run the following to host on https://localhost:8888
 ```
$ python https-server.py any-file.txt
 ```