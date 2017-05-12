AWESOME ADMIN
=============

一个针对 django admin  UI及功能的改进版本

目前该项目正在开发中

考虑到使用了商业模板，禁止提交任何商业代码，样式文件暂时不入库
后期有精力去商业化后，正式对外。

我们目前使用的商业模板是 inspina。向大家推荐下，很不错的管理模板


## 开发配置


### 模板引用

因为有大量静态资源使用了商业模板

需要配置路径指向商业模板，比如：

```python

STATICFILES_DIRS = (
    os.path.expanduser('~/OneDrive/Resources/themes'),
)
```


### 引入包

对于需要参与开发本模块的同学，请自行添加  `PYTHONPATH` 路径。
基于内部项目开发的同学，请确保代码仓库路径与 `settings.py` 中声明路径一致







