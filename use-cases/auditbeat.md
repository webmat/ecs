## Auditbeat use case

ECS usage in Auditbeat.

### <a name="auditbeat"></a> Auditbeat fields


| Field  | Level  | Type  | Description  | Example  |
|---|---|---|---|---|
| [event.module](https://github.com/elastic/ecs#event.module)  | core | keyword | Auditbeat module name. | `mysql` |
| <a name="file.&ast;"></a>*file.&ast;* |  |  | *File attributes.<br/>* |  |
| [file.path](https://github.com/elastic/ecs#file.path)  | extended | keyword | The path to the file. |  |
| [file.target_path](https://github.com/elastic/ecs#file.target_path)  | extended | keyword | The target path for symlinks. |  |
| [file.type](https://github.com/elastic/ecs#file.type)  | extended | keyword | The file type (file, dir, or symlink). |  |
| [file.device](https://github.com/elastic/ecs#file.device)  | extended | keyword | The device. |  |
| [file.inode](https://github.com/elastic/ecs#file.inode)  | extended | keyword | The inode representing the file in the filesystem. |  |
| [file.uid](https://github.com/elastic/ecs#file.uid)  | extended | keyword | The user ID (UID) or security identifier (SID) of the file owner. |  |
| [file.owner](https://github.com/elastic/ecs#file.owner)  | extended | keyword | The file owner's username. |  |
| [file.gid](https://github.com/elastic/ecs#file.gid)  | extended | keyword | The primary group ID (GID) of the file. |  |
| [file.group](https://github.com/elastic/ecs#file.group)  | extended | keyword | The primary group name of the file. |  |
| [file.mode](https://github.com/elastic/ecs#file.mode)  | extended | keyword | The mode of the file in octal representation. | `416` |
| [file.size](https://github.com/elastic/ecs#file.size)  | extended | long | The file size in bytes (field is only added when `type` is `file`). |  |
| [file.mtime](https://github.com/elastic/ecs#file.mtime)  | extended | date | The last modified time of the file (time when content was modified). |  |
| [file.ctime](https://github.com/elastic/ecs#file.ctime)  | extended | date | The last change time of the file (time when metadata was changed). |  |
| <a name="hash.&ast;"></a>*hash.&ast;* |  |  | *Hash fields used in Auditbeat.<br/>The hash field contains cryptographic hashes of data associated with the event (such as a file). The keys are names of cryptographic algorithms. The values are encoded as hexidecimal (lower-case).<br/>All fields in user can have one or multiple entries.<br/>* |  |
| <a name="hash.blake2b_256"></a>*hash.blake2b_256* | (use case) | keyword | *BLAKE2b-256 hash of the file.* |  |
| <a name="hash.blake2b_384"></a>*hash.blake2b_384* | (use case) | keyword | *BLAKE2b-384 hash of the file.* |  |
| <a name="hash.blake2b_512"></a>*hash.blake2b_512* | (use case) | keyword | *BLAKE2b-512 hash of the file.* |  |
| <a name="hash.md5"></a>*hash.md5* | (use case) | keyword | *MD5 hash.* |  |
| <a name="hash.sha1"></a>*hash.sha1* | (use case) | keyword | *SHA-1 hash.* |  |
| <a name="hash.sha224"></a>*hash.sha224* | (use case) | keyword | *SHA-224 hash (SHA-2 family).* |  |
| <a name="hash.sha256"></a>*hash.sha256* | (use case) | keyword | *SHA-256 hash (SHA-2 family).* |  |
| <a name="hash.sha384"></a>*hash.sha384* | (use case) | keyword | *SHA-384 hash (SHA-2 family).* |  |
| <a name="hash.sha512"></a>*hash.sha512* | (use case) | keyword | *SHA-512 hash (SHA-2 family).* |  |
| <a name="hash.sha512_224"></a>*hash.sha512_224* | (use case) | keyword | *SHA-512/224 hash (SHA-2 family).* |  |
| <a name="hash.sha512_256"></a>*hash.sha512_256* | (use case) | keyword | *SHA-512/256 hash (SHA-2 family).* |  |
| <a name="hash.sha3_224"></a>*hash.sha3_224* | (use case) | keyword | *SHA3-224 hash (SHA-3 family).* |  |
| <a name="hash.sha3_256"></a>*hash.sha3_256* | (use case) | keyword | *SHA3-256 hash (SHA-3 family).* |  |
| <a name="hash.sha3_384"></a>*hash.sha3_384* | (use case) | keyword | *SHA3-384 hash (SHA-3 family).* |  |
| <a name="hash.sha3_512"></a>*hash.sha3_512* | (use case) | keyword | *SHA3-512 hash (SHA-3 family).* |  |
| <a name="hash.xxh64"></a>*hash.xxh64* | (use case) | keyword | *XX64 hash of the file.* |  |



