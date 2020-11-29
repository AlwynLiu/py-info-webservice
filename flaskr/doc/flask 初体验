# flask 初体验

## 安装python3

从[python官网](https://www.python.org/downloads/)下载python想要的版本，安装到机器上，我使用的是window，安装时注意勾选上add python 3.9 to PATH, 这样可以不用再去配置环境变量了。

![1606623279202](D:\codeFiles\python\pywebservice\flaskr\doc\assets\flask 初体验\1606623279202.png)

## 安装flask 

```shell
pip3 install flask
```

## 编写api文件hello.py

```python
from flask import Flask

app = Flask(__name__)





@app.route('/hello', methods=['get'])

def hello():

  return 'hello world'





if __name__ == '__main__':

  app.run(debug=True)
```



## vscode 启动flask

vscode 先安装python组件![1606622673559](C:\Users\alvin\AppData\Roaming\Typora\typora-user-images\1606622673559.png)

然后在左下角选择flask安装的python的执行路径

![1606622760565](C:\Users\alvin\AppData\Roaming\Typora\typora-user-images\1606622760565.png)

最后点击右上角的启动，或者直接在shell中输入

```
py hello.py
```

最终的启动成功后的命令行显示

![1606623008282](C:\Users\alvin\AppData\Roaming\Typora\typora-user-images\1606623008282.png)

## 最终hello world效果

在浏览器中访问地址：http://127.0.0.1:5000/, 显示结果返回的代码上的hello world， 则是初次显示成功。

![1606623132570](C:\Users\alvin\AppData\Roaming\Typora\typora-user-images\1606623132570.png)