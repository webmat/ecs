## Logging use case

ECS fields used in logging use cases.

### <a name="logging"></a> Logging fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| <a name="id"></a>*id* | (use case) | keyword | *Unique id of the log entry.* | `8a4f500d` |
| <a name="timestamp"></a>*timestamp* | (use case) | date | *Timestamp of the log line.* | `2016-05-23T08:05:34.853Z` |
| [message](https://github.com/elastic/ecs#message)  | core | text | The log message.<br/>This can contain the full log line or based on the processing only the extracted message part. This is expected to be human readable. | `Hello World` |
| <a name="hostname"></a>*hostname* | (use case) | keyword | *Hostname extracted from the log line.* | `www.example.com` |
| <a name="ip"></a>*ip* | (use case) | ip | *IP Address extracted from the log line. Can be IPv4 or IPv6.* | `192.168.1.12` |
| [log.level](https://github.com/elastic/ecs#log.level)  | core | keyword | Log level field. Is expected to be `WARN`, `ERR`, `INFO` etc. | `ERR` |
| <a name="log.line"></a>*log.line* | (use case) | long | *Line number the log event was collected from.* | `18` |
| <a name="log.offset"></a>*log.offset* | (use case) | long | *Offset of the log event.* | `12` |
| <a name="source.&ast;"></a>*source.&ast;* |  |  | *Describes from where the log entries come from.<br/>* |  |
| <a name="source.path"></a>*source.path* | (use case) | keyword | *File path of the file the data is harvested from.* | `/var/log/test.log` |



