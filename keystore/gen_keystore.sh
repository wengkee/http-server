# rm https_*
# https://stackoverflow.com/questions/652916/converting-a-java-keystore-into-pem-format
keystore_file="https_server.keys"
keystore_alias="https_server"
p12_file="https_server.p12"
pem_file="https_server.pem"

keytool -genkey -keystore $keystore_file -alias $keystore_alias -keyalg RSA -keysize 2048

keytool -importkeystore -srckeystore $keystore_file \
       -destkeystore $p12_file \
       -srcstoretype jks \
       -deststoretype pkcs12

openssl pkcs12 -in $p12_file -out $pem_file