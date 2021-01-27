## 内置的配置值

下列配置值是 Flask 内部使用的：

| `DEBUG`                         | 启用/禁止调试模式                                            |
| ------------------------------- | ------------------------------------------------------------ |
| `TESTING`                       | 启用/禁止测试模式                                            |
| `PROPAGATE_EXCEPTIONS`          | 显式地启用或者禁止异常的传播。 如果没有设置 或显式地设置为 None ， 当 TESTING 或 DEBUG 为真时， 隐式为真。 |
| `PRESERVE_CONTEXT_ON_EXCEPTION` | 默认情况下，如果应用工作在调试模式， 请求上下文不会在异常时出栈来允许调试器内省。 这可以通过这个键来禁用。 你同样可以用这个设定来强制启用它， 即使没有调试执行，这对调试生产应用很有用 (但风险也很大) |
| `SECRET_KEY`                    | 密钥                                                         |
| `SESSION_COOKIE_NAME`           | 会话 cookie 的名称                                           |
| `SESSION_COOKIE_DOMAIN`         | 会话 cookie 的域。如果没有设置的话， cookie 将会对 `SERVER_NAME` 所有的子域都有效。 |
| `SESSION_COOKIE_PATH`           | 会话 cookie 的路径。如果没有设置或者没有为 `'/'` 设置，cookie 将会对所有的 `APPLICATION_ROOT` 有效。 |
| `SESSION_COOKIE_HTTPONLY`       | 控制 cookie 是否应被设置 httponly 的标志， 默认为 True 。    |
| `SESSION_COOKIE_SECURE`         | 控制 cookie 是否应被设置安全标志，默认为 False。             |
| `PERMANENT_SESSION_LIFETIME`    | 一个持久化的会话的生存时间，作为一个 [`datetime.timedelta`](http://docs.python.org/dev/library/datetime.html#datetime.timedelta) 对象。从 Flask0.8 开始 也可以用一个整数来表示秒。 |
| `USE_X_SENDFILE`                | 启用/禁止 x-sendfile                                         |
| `LOGGER_NAME`                   | 日志记录器的名称                                             |
| `SERVER_NAME`                   | 服务器的名称以及端口，需要它为了支持子域名 (如: `'myapp.dev:5000'`)。注意 localhost 是 不支持子域名的因此设置成 “localhost” 是无意义的。 设置 `SERVER_NAME` 默认会允许在没有请求上下文 而仅有应用上下文时生成 URL。 |
| `APPLICATION_ROOT`              | 如果应用不占用完整的域名或子域名， 这个选项可以被设置为应用所在的路径。 这个路径也会用于会话 cookie 的路径值。 如果直接使用域名，则留作 `None`。 |
| `MAX_CONTENT_LENGTH`            | 如果设置为字节数， Flask 会拒绝内容长度大于 此值的请求进入，并返回一个 413 状态码。 |
| `SEND_FILE_MAX_AGE_DEFAULT`:    | 默认缓存控制的最大期限，以秒计， 在 [`send_static_file()`](http://www.pythondoc.com/flask/api.html#flask.Flask.send_static_file) (默认的静态文件处理器)和 [`send_file()`](http://www.pythondoc.com/flask/api.html#flask.send_file) 中使用。 对于单个文件，覆盖这个值，使用 [`get_send_file_max_age()`](http://www.pythondoc.com/flask/api.html#flask.Flask.get_send_file_max_age) 勾住 [`Flask`](http://www.pythondoc.com/flask/api.html#flask.Flask) 或者 [`Blueprint`](http://www.pythondoc.com/flask/api.html#flask.Blueprint)。 默认为 43200（12小时）。 |
| `TRAP_HTTP_EXCEPTIONS`          | 如果这个值被设置为 `True` ， Flask 不会执行 HTTP 异常的错误处理， 而是像对待其它异常一样，通过异常栈让它冒泡。 这对于需要找出 HTTP 异常源头的可怕调试情形是有用的。 |
| `TRAP_BAD_REQUEST_ERRORS`       | Werkzeug 处理请求中的特定数据的内部数据结构会 抛出同样也是“错误的请求”异常的特殊的 key errors 。 同样地，为了保持一致，许多操作可以 显式地抛出 BadRequest 异常。因为在调试中， 你希望准确地找出异常的原因， 这个设置用于在这些情形下调试。 如果这个值被设置为 `True` ， 你只会得到常规的回溯。 |
| `PREFERRED_URL_SCHEME`          | URL 模式用于 URL 生成。如果没有设置 URL 模式， 默认将为 `http` 。 |
| `JSON_AS_ASCII`                 | 默认情况下 Flask 序列化对象成 ascii 编码的 JSON。 如果不对该配置项就行设置的话，Flask 将不会编码成 ASCII 保持字符串原样，并且返回 unicode 字符串。`jsonfiy` 会自动按照 `utf-8` 进行编码并且传输。 |
| `JSON_SORT_KEYS`                | 默认情况下 Flask 将会依键值顺序的方式序列化 JSON。 这样做是为了确保字典哈希种子的独立性，返回值将会一致不会造成 额外的 HTTP 缓存。通过改变这个变量可以重载默认行为。 这是不推荐也许会带来缓存消耗的性能问题。 |
| `JSONIFY_PRETTYPRINT_REGULAR`   | 如果设置成 `True` (默认下)，jsonify 响应将会完美地打印。     |