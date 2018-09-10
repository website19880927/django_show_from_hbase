# django_show_from_hbase

从HBASE中获取数据，利用django 进行展示，同时使用redis管理session，nginx 与uwsgi 分别作为静态服务器，应用服务器，做负载均衡。简单搭建框架，使用Linux， 需要另外安装Linux系统的配置，包括nginx，uwgi,redis,hbase,hadoop,zookeeper
