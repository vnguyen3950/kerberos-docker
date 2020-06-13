#!/bin/bash
/etc/init.d/webmin restart
cat << EOF  | kadmin.local
add_principal -pw alice alice/admin@EXAMPLE.COM
add_principal -pw bob bob
add_principal -randkey host/krb5-kdc-server-example-com.kerberos-docker_devcontainer_default@EXAMPLE.COM
ktadd -norandkey host/krb5-kdc-server-example-com.kerberos-docker_devcontainer_default@EXAMPLE.COM
ktadd krbtgt/EXAMPLE.COM@EXAMPLE.COM