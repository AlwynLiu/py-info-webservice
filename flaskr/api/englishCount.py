from flask import Blueprint, render_template, request
import string, json


bp = Blueprint('englishcount', __name__, url_prefix='/englishcount')


@bp.route('/index', methods=['get'])
def count():
    """ 操作首页
    返回可操作功能的首页
    ---
    tags:
      - 单词计数
    parameters:
      - file:
        type: string
        default: all
    responses:
      200:
        description: success
        examples:
          data: success
    """
    return render_template("./englishCount/index.html")

@bp.route('/wordCount', methods=['post'])
def postFile():
    """ 计算单词数量
    把上传的文件搞成计算成单词
    ---
    tags:
      - 单词计数
    parameters:
      - file:
        type: string
        default: all
    responses:
      200:
        description: success
        examples:
          data: success
    """
    # 读取页面上传的文件内容
    wordstring = request.files.get('uploadFile').read()

    # 读取文本内容在单词频数
    # 上文读取的数据是r''的字节数据，需要转化成string
    wordstring = bytes.decode(wordstring)

    wordstring = replaceStr(wordstring)
    wordlist = wordstring.split()

    xmlString = ''
    for word in wordlist:
        if len(word) > 2 :
            xmlString += formatYoudaoXml(word, request.form['textText'])
    return '<wordbook>{}</wordbook>'.format(xmlString)

    # 格式化处理为字段格式的json数据返回
    # wordfreq = []
    # for w in wordlist:
    #     if len(w) > 2:
    #         wordfreq.append(wordlist.count(w))
    #     else:
    #         wordlist.remove(w)
    # d = dict(zip(wordlist, wordfreq))
    # return json.dumps(d, ensure_ascii=False)
    # return json.dumps(wordlist)


# 替换不需要的字符
def replaceStr(str):
    return str.replace('.', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('/*!', '').replace('《', '').replace('》', '')


# 拼接成有道词典需要的xml格式item
def formatYoudaoXml(word, tags='未分组'):
    return '''<item><word>{word}</word>
    <tags>{tags}</tags></item>'''.format(word=word, tags=tags)