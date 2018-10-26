## TLS use case

You can store TLS-related metadata under `tls.`, when appropriate.


### <a name="tls"></a> TLS fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| [source.ip](https://github.com/elastic/ecs#source.ip)  | core | ip | IP address of the source.<br/>Can be one or multiple IPv4 or IPv6 addresses. | `10.1.1.10` |
| [destination.ip](https://github.com/elastic/ecs#destination.ip)  | core | ip | IP address of the destination.<br/>Can be one or multiple IPv4 or IPv6 addresses. | `5.5.5.5` |
| [destination.port](https://github.com/elastic/ecs#destination.port)  | core | long | Port of the destination. | `443` |
| <a name="tls.version"></a>*tls.version* | (use case) | keyword | *TLS version.* | `TLSv1.2` |
| <a name="tls.certificates"></a>*tls.certificates* | (use case) | keyword | *An array of certificates.* |  |
| <a name="tls.servername"></a>*tls.servername* | (use case) | keyword | *Server name requested by the client.* | `localhost` |
| <a name="tls.ciphersuite"></a>*tls.ciphersuite* | (use case) | keyword | *Name of the cipher used for the communication.* | `ECDHE-ECDSA-AES-128-CBC-SHA` |



