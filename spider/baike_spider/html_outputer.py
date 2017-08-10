#encoding:utf-8
# 输出器

class Html_outputer(object):
    # 收集数据
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出html文档
    def output_html(self):
        fout = open('output.html','w')
        #fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for data in self.datas: 
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</html>")
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
    
    
    



