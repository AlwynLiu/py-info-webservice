from flask import Blueprint, render_template, request
import string


bp = Blueprint('englishcount', __name__, url_prefix='/englishcount')


@bp.route('/wordCount', methods=['get', 'post'])
def count():
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
    wordstring = """
    /**
        * Create a cached version of a pure function.
        */
          function cached(fn) {
            var cache = Object.create(null);
            return (function cachedFn(str) {
              var hit = cache[str];
              return hit || (cache[str] = fn(str))
            })
          }
        
          /**
           * Camelize a hyphen-delimited string.
           */
          var camelizeRE = /-(\w)/g;
          var camelize = cached(function (str) {
            return str.replace(camelizeRE, function (_, c) { return c ? c.toUpperCase() : ''; })
          });
        
          /**
           * Capitalize a string.
           */
          var capitalize = cached(function (str) {
            return str.charAt(0).toUpperCase() + str.slice(1)
          });
        
          /**
           * Hyphenate a camelCase string.
           */
    """

    # 读取页面上传的文件内容
    postdata = request.files.get('uploadFile')
    # with open(request.files.get('uploadFile')) as file_obj:
    #     content = file_obj.read()
    #     print(content)
    print(postdata)
    # 读取文本内容在单词频数
    # wordstring = wordstring.replace('.', '')
    # wordlist = wordstring.split()
    # wordfreq = []
    # for w in wordlist:
    #     wordfreq.append(wordlist.count(w))
    # d = dict(zip(wordlist, wordfreq))
    # print(d)

    return render_template("./englishCount/index.html")

    # return "postdata"