**WARNING: THIS COMMIT IS ONLY TO ILLUSTRATE TWO DIFFERENT WAYS OF REPRESENTING CORE VS EXTENDED FIELDS**

# Elastic Common Schema (ECS)

The Elastic Common Schema (ECS) defines a common set of fields for
ingesting data into Elasticsearch. A common schema helps you correlate
data from sources like logs and metrics or IT operations
analytics and security analytics.

ECS is still under development and backward compatibility is not guaranteed. Any
feedback on the general structure, missing fields, or existing fields is appreciated.
For contributions please read the [Contributing Guide](CONTRIBUTING.md).

<a name="ecs-version"></a>The current version of ECS is `0.1.0`.

# In this readme

* [Fields](#fields)
* [Use cases](#use-cases)
* [Implementing ECS](#implementing-ecs)
* [FAQ](#faq-ecs)

# <a name="fields"></a>Fields

ECS defines these fields.
 * [Event fields](#event)

**WARNING: THIS COMMIT IS ONLY TO ILLUSTRATE TWO DIFFERENT WAYS OF REPRESENTING CORE VS EXTENDED FIELDS**

## <a name="event"></a> Event fields

The event fields are used for context information about the data itself.

| Field  | ECS Level | Description  | Data type  | Multi Field  | Example  |
|---|---|---|---|---|---|
| <a name="event.id"></a>event.id  | Core | Unique ID to describe the event.  | keyword  |   | `8a4f500d`  |
| <a name="event.category"></a>event.category  | Core | Event category.<br/>This can be a user defined category.  | keyword  |   | `metrics`  |
| <a name="event.type"></a>event.type  | Core | A type given to this kind of event which can be used for grouping.<br/>This is normally defined by the user.  | keyword  |   | `nginx-stats-metrics`  |
| <a name="event.action"></a>event.action  | Core | The action captured by the event. The type of action will vary from system to system but is likely to include actions by security services, such as blocking or quarantining; as well as more generic actions such as login events, file i/o or proxy forwarding events.<br/>The value is normally defined by the user.  | keyword  |   | `reject`  |
| <a name="event.module"></a>event.module  | Core | Name of the module this data is coming from.<br/>This information is coming from the modules used in Beats or Logstash.  | keyword  |   | `mysql`  |
| <a name="event.dataset"></a>event.dataset  | Core | Name of the dataset.<br/>The concept of a `dataset` (fileset / metricset) is used in Beats as a subset of modules. It contains the information which is currently stored in metricset.name and metricset.module or fileset.name.  | keyword  |   | `stats`  |
| <a name="event.severity"></a>event.severity  | Core | Severity describes the severity of the event. What the different severity values mean can very different between use cases. It's up to the implementer to make sure severities are consistent across events.  | long  |   | `7`  |
| <a name="event.original"></a>event.original  | Core | Raw text message of entire event. Used to demonstrate log integrity.<br/>This field is not indexed and doc_values are disabled. It cannot be searched, but it can be retrieved from `_source`.  | keyword  |   | `Sep 19 08:26:10 host CEF:0&#124;Security&#124; threatmanager&#124;1.0&#124;100&#124; worm successfully stopped&#124;10&#124;src=10.0.0.1 dst=2.1.2.2spt=1232`  |
| <a name="event.hash"></a>event.hash  | Extended | Hash (perhaps logstash fingerprint) of raw field to be able to demonstrate log integrity.  | keyword  |   | `123456789012345678901234567890ABCD`  |
| <a name="event.version"></a>event.version  | Core | The version field contains the version an event for ECS adheres to.<br/>This field should be provided as part of each event to make it possible to detect to which ECS version an event belongs.<br/>event.version is a required field and must exist in all events. It describes which ECS version the event adheres to.<br/>The current version is 0.1.0.  | keyword  |   | `0.1.0`  |
| <a name="event.duration"></a>event.duration  | Core | Duration of the event in nanoseconds.  | long  |   |   |
| <a name="event.created"></a>event.created  | Core | event.created contains the date when the event was created.<br/>This timestamp is distinct from @timestamp in that @timestamp contains the processed timestamp. For logs these two timestamps can be different as the timestamp in the log line and when the event is read for example by Filebeat are not identical. `@timestamp` must contain the timestamp extracted from the log line, event.created when the log line is read. The same could apply to package capturing where @timestamp contains the timestamp extracted from the network package and event.created when the event was created.<br/>In case the two timestamps are identical, @timestamp should be used.  | date  |   |   |
| <a name="event.risk_score"></a>event.risk_score  | Core | Risk score or priority of the event (e.g. security solutions). Use your system's original value here.  | float  |   |   |
| <a name="event.risk_score_norm"></a>event.risk_score_norm  | Extended | Normalized risk score or priority of the event, on a scale of 0 to 100.<br/>This is mainly useful if you use more than one system that assigns risk scores, and you want to see a normalized value across all systems.  | float  |   |   |



# <a name="use-cases"></a>Use cases

These are example on how ECS fields can be used in different use cases. Most use
cases not only contain ECS fields but additional fields which are not in ECS to
describe the full use case. The fields which are not in ECS are in italic.

Contributions of additional uses cases on top of ECS are welcome.

 * [APM](https://github.com/elastic/ecs/blob/master/use-cases/apm.md)
 * [Auditbeat](https://github.com/elastic/ecs/blob/master/use-cases/auditbeat.md)
 * [Beats](https://github.com/elastic/ecs/blob/master/use-cases/beats.md)
 * [Filebeat Apache](https://github.com/elastic/ecs/blob/master/use-cases/filebeat-apache-access.md)
 * [Logging](https://github.com/elastic/ecs/blob/master/use-cases/logging.md)
 * [Metricbeat](https://github.com/elastic/ecs/blob/master/use-cases/metricbeat.md)



# <a name="implementing-ecs"></a>Implementing ECS

## Guidelines

* The document MUST have the `@timestamp` field.
* The [data type](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/mapping-types.html) defined for an ECS field MUST be used.
* It SHOULD have the field `event.version` to define which version of ECS it uses.
* As many fields as possible should be mapped to ECS.

**Writing fields**

* All fields must be lower case
* Combine words using underscore
* No special characters except `_`

**Naming fields**

* *Present tense.* Use present tense unless field describes historical information.
* *Singular or plural.* Use singular and plural names properly to reflect the field content. For example, use `requests_per_sec` rather than `request_per_sec`.
* *General to specific.* Organise the prefixes from general to specific to allow grouping fields into objects with a prefix like `host.*`.
* *Avoid repetition.* Avoid stuttering of words. If part of the field name is already in the prefix, do not repeat it. Example: `host.host_ip` should be `host.ip`.
* *Use prefixes.* Fields must be prefixed except for the base fields. For example all `host` fields are prefixed with `host.`. See `dot` notation in FAQ for more details.
* Do not use abbreviations. (A few exceptions like `ip` exist.)

## Understanding ECS conventions

### Multi-fields text indexing

ElasticSearch can index text multiple ways:

* [text](https://www.elastic.co/guide/en/elasticsearch/reference/current/text.html) indexing allows for full text search, or searching arbitrary words that
  are part of the field.
* [keyword](https://www.elastic.co/guide/en/elasticsearch/reference/current/keyword.html) indexing allows for much faster
  [exact match](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html)
  and [prefix search](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-prefix-query.html),
  and allows for [aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html)
  (what Kibana visualizations are built on).

In some cases, only one type of indexing makes sense for a field.

However there are cases where both types of indexing can be useful, and we want
to index both ways.
As an example, log messages can sometimes be short enough that it makes sense
to sort them by frequency (that's an aggregation). They can also be long and
varied enough that full text search can be useful on them.

Whenever both types of indexing are helpful, we use multi-fields indexing. The
convention used is the following:

* `foo`: `text` indexing.
  The top level of the field (its plain name) is used for full text search.
* `foo.raw`: `keyword` indexing.
  The nested field has suffix `.raw` and is what you will use for aggregations.
  * Performance tip: when filtering your stream in Kibana (or elsewhere), if you
    are filtering for an exact match or doing a prefix search,
    both `text` and `keyword` field can be used, but doing so on the `keyword`
    field (named `.raw`) will be much faster and less memory intensive.

**Keyword only fields**

The fields that only make sense as type `keyword` are not named `foo.raw`, the
plain field (`foo`) will be of type `keyword`, with no nested field.

### IDs are keywords not integers

Despite the fact that IDs are often integers in various systems, this is not
always the case. Since we want to make it possible to map as many data sources
to ECS as possible, we default to using the `keyword` type for IDs.

# <a name="about-ecs"></a>FAQ

## What are the benefits of using ECS?

The benefits to a user adopting these fields and names in their clusters are:

* **Data correlation.** Ability to easily correlate data from the same or different sources, including:
    * data from metrics, logs, and apm
    * data from the same machines/hosts
    * data from the same service
* **Ease of recall.** Improved ability to remember commonly used field names (because there is a single set, not a set per data source)
* **Ease of deduction.** Improved ability to deduce field names (because the field naming follows a small number of rules with few exceptions)
* **Reuse.** Ability to re-use analysis content (searches, visualizations, dashboards, alerts, reports, and ML jobs) across multiple data sources
* **Future proofing.** Ability to use any future Elastic-provided analysis content in your environment without modifications

## What if I have fields that conflict with ECS?

The [rename processor](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/rename-processor.html) can help you resolve field conflicts. For example, imagine that you already have a field called "user," but ECS employs `user` as an object. You can use the rename processor on ingest time to rename your field to the matching ECS field. If your field does not match ECS, you can rename your field to `user.value` instead.

## What if my events have additional fields?

Events may contain fields in addition to ECS fields. These fields can follow the ECS naming and writing rules, but this is not a requirement.

## Why does ECS use a dot notation instead of an underline notation?

There are two common key formats for ingesting data into Elasticsearch:

* Dot notation: `user.firstname: Nicolas`, `user.lastname: Ruflin`
* Underline notation: `user_firstname: Nicolas`, `user_lastname: Ruflin`

For ECS we decided to use the dot notation. Here's some background on this decision.

### What is the difference between the two notations?

Ingesting `user.firstname: Nicolas` and `user.lastname: Ruflin` is identical to ingesting the following JSON:

```
"user": {
  "firstname": "Nicolas",
  "lastname": "Ruflin"
}
```

In Elasticsearch, `user` is represented as an [object datatype](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/object.html). In the case of the underline notation, both are just [string datatypes](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html).

NOTE: ECS does not use [nested datatypes](https://www.elastic.co/guide/en/elasticsearch/reference/current/nested.html), which are arrays of objects.

### Advantages of dot notation

With dot notation, each prefix in Elasticsearch is an object. Each object can have [parameters](https://www.elastic.co/guide/en/elasticsearch/reference/current/object.html#object-params) that control how fields inside the object are treated. In the context of ECS, for example, these parameters would allow you to disable dynamic property creation for certain prefixes.

Individual objects give you more flexibility on both the ingest and the event sides.  In Elasticsearch, for example, you can use the remove processor to drop complete objects instead of selecting each key inside. You don't have to know ahead of time which keys will be in an object.

In Beats, you can simplify the creation of events. For example, you can treat each object as an object (or struct in Golang), which makes constructing and modifying each part of the final event easier.

### Disadvantage of dot notation

In Elasticsearch, each key can only have one type. For example, if `user` is an `object`, you can't use it as a`keyword` type in the same index, like `{"user": "nicolas ruflin"}`. This restriction can be an issue in certain datasets. For the ECS data itself, this is not an issue because all fields are predefined.

### What if I already use the underline notation?

Mixing the underline notation with the ECS dot notation is not a problem. As long as there are no conflicts, they can coexist in the same document.
