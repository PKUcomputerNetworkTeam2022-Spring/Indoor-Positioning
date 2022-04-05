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

7. 关闭服务

   命令行键入CTRL-BREAK，服务将被关闭，终端恢复到可输入状态
