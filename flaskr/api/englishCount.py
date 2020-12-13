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
    # with open(request.files.get('uploadFile')) as file_obj:
    #     content = file_obj.read()
    #     print(content)
    # 读取文本内容在单词频数
    wordstring = bytes.decode(wordstring)
    wordstring = replaceStr(wordstring)
    wordlist = wordstring.split()
    wordfreq = []
    for w in wordlist:
        if(len(w) > 2):
            wordfreq.append(wordlist.count(w))
        else:
            wordlist.remove(w)
    d = dict(zip(wordlist, wordfreq))
    return json.dumps(d, ensure_ascii=False)

def replaceStr(str):
    return str.replace('.', '').replace('{', '')\
        .replace('}','').replace('(','')\
        .replace(')','').replace('/*!','')