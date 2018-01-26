from flask import  Flask,request

app = Flask(__name__)

@app.route('get_request',methods=['GET','POST'])
def get_request():
    print 'method: %s' % request.method
    print 'headers: %s' % request.headers
    print 'url: %s' % request.url
    print 'cookies: %s' % request.cookies

    # args: 获取请求的参数
    print 'args: %s' % request.args.get('name')

    # form: 获取表单数据
    print 'form: %s' % request.form.get('name')

    # data: 获取原始数据:文本/JSON等
    print 'data: %s' % request.data

    # files: 获取文件信息
    print 'file: %s' % request.files
    image_file = request.files.get('pic')
    image_file.save('./girl.png')

    return 'get_request'


if __name__ == '__main__':
    app.run(debug=True)