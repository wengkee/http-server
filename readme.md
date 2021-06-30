#  HTTP Server
Simple HTTP server written in Python 3 which will read a file from and serve it to the page.


## Prequisite
* Install Python 3 
* Prepare a content file, e.g. any-file.txt
* (optional) Install `keytool` for generating PEM file for hosting with HTTPS

## Quickstart
### HTTP 
1. Run the following to host on http://localhost:8888
    ```
    python http-server.py any-file.txt
    ```

### HTTPS
1. Generate a PEM file
    ```
   chmod u+x keystore/gen_pem.sh && ./keystore/gen_pem.sh
   ```

2. Run the following to host on https://localhost:8888
    ```
    python https-server.py any-file.txt
    ```