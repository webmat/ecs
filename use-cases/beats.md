## Beats use case

ECS fields used in Beats.

### <a name="beats"></a> Beats fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| <a name="id"></a>*id* | (use case) | keyword | *Unique id to describe the event.* | `8a4f500d` |
| <a name="timestamp"></a>*timestamp* | (use case) | date | *Timestamp when the event was created.* | `2016-05-23T08:05:34.853Z` |
| <a name="agent.&ast;"></a>*agent.&ast;* |  |  | *The agent fields are used to describe by which beat the information was collected.<br/>* |  |
| [agent.version](https://github.com/elastic/ecs#agent.version)  | core | keyword | Beat version. | `6.0.0-rc2` |
| [agent.name](https://github.com/elastic/ecs#agent.name)  | core | keyword | Beat name. | `filebeat` |
| [agent.id](https://github.com/elastic/ecs#agent.id)  | core | keyword | Unique beat identifier. | `8a4f500d` |



