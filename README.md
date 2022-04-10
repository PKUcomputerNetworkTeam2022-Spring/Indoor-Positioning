# 无限信号感知与室内定位

### 如何启动

1. 安装Django

   `pip install django`

2. 创建迁移

   `python manage.py makemigrations`

3. 执行迁移

   `python manage.py migrate`

   此后无需执行1-3步

4. 查看本机ip(用于部署，可选)

   - Windows
      `ipconfig` -> WLAN部分 -> IPv4(v6)地址
   
   - MacOS/Linux
      `ifconfig` -> addr

5. 运行开发服务器

   `python manage.py runserver [[ip:]port]`

   - 部署
      `python manage.py runserver $ip$:80`，其中`$ip$`是第四步查询的本机ip

   - 调试网页
      `python manage.py runserver 0:80`
      `python manage.py runserver 80`
      `python manage.py runserver`

6. 访问服务

   1. 若无异常，第5步输出类似于：
      ```
      Django version 3.2, using settings 'managing.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.
      ```

   2. 此时，通过第二行的网址(示例中为http://127.0.0.1:8000/)即可访问网页

      URL未设置时，你应在网页中看到一个火箭和以下内容：
      ```
      The install worked successfully! Congratulations!
      You are seeing this page because DEBUG=True is in
      your settings file and you have not configured any URLs.
      ```

      正常情况下呈现一个简单的页面，包含最近的一条记录信息

7. 关闭服务

   命令行键入CTRL-BREAK，服务将被关闭，终端恢复到可输入状态

### 进阶操作

在Django可正常启动后，可以使用进阶操作提升效率

- 后台管理

  1. 创建管理员账户

     `python manage.py createsuperuser`按提示输入信息

  2. 运行Django

  3. 访问后台并登录

     - 直接访问`项目URL/admin`(示例中为http://127.0.0.1:8000/admin/)
     - 访问项目首页，点击超链接跳转

- 单元测试

  1. 在`indoor_positioning/tests.py`中创建继承自`TestCase`的测试用例
  
     每个测试用例对应一个*场景*或*环境*
  
  2. 定义`setUp`为该测试用例的系列测试创建统一的环境
  
  3. 编写测试，测试是以`test`开始的方法
  
     **注意**：每个测试都将生成一个**独立**的实例并执行一次`setUp`
  
  4. 运行测试
  
     - Django自带测试
       - `python manage.py test`
       - `python manage.py test [APP[.FILE[.CASE[.TEST]]]]`
       - 单个测试不太方便，但安全
     - VSCode
       - 可通过左侧测试栏进行快捷、自动测试，并支持调试和部分测试，但**使用生产数据库**(测试后会恢复)，存在数据干扰
       - 也可使用launch.json，创建测试配置执行Django自带测试并调试
     
     **注意**：单元测试将启用独立的临时数据库，不干扰已有数据
