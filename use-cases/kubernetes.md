## Kubernetes use case

You can monitor containers running in a Kubernetes cluster by adding Kubernetes-specific information under `kubernetes.`


### <a name="kubernetes"></a> Kubernetes fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| [container.id](https://github.com/elastic/ecs#container.id)  | core | keyword | Unique container id. | `fdbef803fa2b` |
| [container.name](https://github.com/elastic/ecs#container.name)  | extended | keyword | Container name. |  |
| [host.hostname](https://github.com/elastic/ecs#host.hostname)  | core | keyword | Hostname of the host.<br/>It can contain what `hostname` returns on Unix systems, the fully qualified domain name, or a name specified by the user. The sender decides which value to use. | `kube-high-cpu-42` |
| <a name="kubernetes.pod.name"></a>*kubernetes.pod.name* | (use case) | keyword | *Kubernetes pod name* | `foo-webserver` |
| <a name="kubernetes.namespace"></a>*kubernetes.namespace* | (use case) | keyword | *Kubernetes namespace* | `foo-team` |
| <a name="kubernetes.labels"></a>*kubernetes.labels* | (use case) | object | *Kubernetes labels map* |  |
| <a name="kubernetes.annotations"></a>*kubernetes.annotations* | (use case) | object | *Kubernetes annotations map* |  |
| <a name="kubernetes.container.name"></a>*kubernetes.container.name* | (use case) | keyword | *Kubernetes container name. This name is unique within the pod only. It is different from the `container.name` field.* |  |



