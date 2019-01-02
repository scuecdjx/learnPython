from urllib import request
import re    #导入正则表达式包
from docx import Document  #导入文档包



website = 'http://www.chinawenben.com/file/esswr6xuxzastvocstatu3ws_1.html'
def getUrl(url):
    #第一步获取url
    url_request = request.Request(url)
    #第二部打开url
    url_response = request.urlopen(url_request)
    #第三部解码，转化为utf-8
    data  = url_response.read().decode('utf-8')
    return data
result = ''
for i in range(1,9):
    url = website.replace('_1','_%d'%i)
    next_url = getUrl(url)
    #利用正则表达式匹配相应的标签内容，返回值为list
    text = re.findall(r'<p>+[^"]+</p>',next_url)
    #print(text)
    #去除标签
    t = re.findall(r'>(.*?)<',str(text))
    for j in t:
        j=j.replace('\\r\\n','\n')  #处理换行符
        result = result+j

file = Document()#新建文档
file.add_paragraph(result)#写入文档，文档基本内容为段落
file.save('/home/scuecdjx/code/python/spider/yaoxueyingyu.docx')#保存文档

