## APM use case

ECS usage for the APM data.

### <a name="apm"></a> APM fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| <a name="id"></a>*id* | (use case) | keyword | *Unique id to describe the event.* | `8a4f500d` |
| [@timestamp](https://github.com/elastic/ecs#@timestamp)  | core | date | Timestamp when the event was created in the app / service. | `2016-05-23T08:05:34.853Z` |
| <a name="agent.&ast;"></a>*agent.&ast;* |  |  | *The agent fields are used to describe which agent did send the information.<br/>* |  |
| [agent.version](https://github.com/elastic/ecs#agent.version)  | core | keyword | APM Agent version. | `3.14.0` |
| [agent.name](https://github.com/elastic/ecs#agent.name)  | core | keyword | APM agent name. | `elastic-node` |
| <a name="service.&ast;"></a>*service.&ast;* |  |  | *The service fields describe the service inside which the APM agent is running.<br/>* |  |
| [service.id](https://github.com/elastic/ecs#service.id)  | core | keyword | Unique identifier of the running service. | `d37e5ebfe0ae6c4972dbe9f0174a1637bb8247f6` |
| [service.name](https://github.com/elastic/ecs#service.name)  | core | keyword | Name of the service the agent is running in. This is normally a user defined name. | `user-service` |
| [service.version](https://github.com/elastic/ecs#service.version)  | core | keyword | Version of the service the agent is running in. This depends on if the service is given a version. | `3.2.4` |



