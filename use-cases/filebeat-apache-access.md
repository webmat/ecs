## Filebeat Apache use case

ECS fields used in Filebeat for the apache module.

### <a name="filebeat-apache-access"></a> Filebeat Apache fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| <a name="id"></a>*id* | (use case) | keyword | *Unique id to describe the event.* | `8a4f500d` |
| [@timestamp](https://github.com/elastic/ecs#@timestamp)  | core | date | Timestamp of the log line after processing. | `2016-05-23T08:05:34.853Z` |
| [message](https://github.com/elastic/ecs#message)  | core | text | Log message of the event | `Hello World` |
| [event.module](https://github.com/elastic/ecs#event.module)  | core | keyword | Currently fileset.module | `apache` |
| [event.dataset](https://github.com/elastic/ecs#event.dataset)  | core | keyword | Currenly fileset.name | `access` |
| [source.ip](https://github.com/elastic/ecs#source.ip)  | core | ip | Source ip of the request. Currently apache.access.remote_ip | `192.168.1.1` |
| [user.name](https://github.com/elastic/ecs#user.name)  | core | keyword | User name in the request. Currently apache.access.user_name | `ruflin` |
| <a name="http.method"></a>*http.method* | (use case) | keyword | *Http method, currently apache.access.method* | `GET` |
| <a name="http.url"></a>*http.url* | (use case) | keyword | *Http url, currently apache.access.url* | `http://elastic.co/` |
| [http.version](https://github.com/elastic/ecs#http.version)  | extended | keyword | Http version, currently apache.access.http_version | `1.1` |
| <a name="http.response.code"></a>*http.response.code* | (use case) | keyword | *Http response code, currently apache.access.response_code* | `404` |
| <a name="http.response.body_sent.bytes"></a>*http.response.body_sent.bytes* | (use case) | long | *Http response body bytes sent, currently apache.access.body_sent.bytes* | `117` |
| <a name="http.referer"></a>*http.referer* | (use case) | keyword | *Http referrer code, currently apache.access.referrer<br/>NOTE: In the RFC its misspell as referer and has become accepted standard* | `http://elastic.co/` |
| <a name="user_agent.&ast;"></a>*user_agent.&ast;* |  |  | *User agent fields as in schema. Currently under apache.access.user_agent.*<br/>* |  |
| [user_agent.original](https://github.com/elastic/ecs#user_agent.original)  | extended | keyword | Original user agent. Currently apache.access.agent | `http://elastic.co/` |
| <a name="geoip.&ast;"></a>*geoip.&ast;* |  |  | *User agent fields as in schema. Currently under apache.access.geoip.*<br/>These are extracted from source.ip<br/>Should they be under source.geoip?<br/>* |  |
| <a name="geoip...."></a>*geoip....* | (use case) | keyword | *All geoip fields.* |  |



