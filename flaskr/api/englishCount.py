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
    postdata = request.form['textText']
    with open(request.files.get('uploadFile')) as file_obj:
        content = file_obj.read()
        print(content)
    print(postdata)
    return render_template("./englishCount/index.html")
