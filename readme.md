
##### 文件目录

```
config.ini -------------------> 配置文件
docker_output.py -------------> 获取docker信息
get_requests.py --------------> 执行请求操作
zipkin_output.py -------------> 获取response time
run.sh -----------------------> 执行脚本
readme.md --------------------> 介绍
```

##### config.ini

* 暂时只存放了所有gateway的url，扩展时须配置config.ini

##### docker_output.py

* 执行命令
    * python docker_output.py file_name run_time
    * e.g.: python docker_output.py test1 120
* 输出结果
    * 在`run_time秒`后输出一个名为`docker_output_{file_name}.csv`的csv文件，之后进行读取
* 注意事项
    * 暂时仅支持单机版，也就是所有service的docker必须在一台机子上

##### get_requests.py

* 执行命令
    * python get_requests.py api在配置文件中的名称 运行时间 请求次数
    * e.g.: python get_requests.py gateway01 120 1
* 输出结果
    * 在`run_time秒`内对api发出`请求次数`次请求。

##### zipkin_output.py

* 执行命令
    * python zipkin_output.py run_time file_name 请求次数
    * e.g.: python zipkin_output.py 120 test1 1
* 输出结果
    * 在`run_time秒`后输出一个名为`json_data_{file_name}.csv`的csv文件，之后进行读取最近`请求次数`次结果
* 注意事项
    * 在zipkin中设置了时间，但是具体操作中这个时间加2秒左右，因为如果不加则会有些访问得不到


##### run.sh

* 执行命令
    * bash run.sh file_name run_time api在配置文件中的名称 请求次数
    * e.g.: bash run.sh test1 120 gateway01 1
* 输出结果
    * 依次执行`docker_output.py`,`docker_output.py`在`执行时间`后执行`zipkin_output.py`
