
import poplib
import email
import datetime
import time
import os
# import xlrd
# import xlwt
import shutil
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import smtplib as sm
import email.mime.multipart
import email.mime.text
import time
import datetime
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import datetime as datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)
m = yesterday.strftime("%Y%m%d")
print(m)
msg = email.mime.multipart.MIMEMultipart()

shutil.rmtree('D:\\WJ\\用户画像输入\\')
os.mkdir('D:\\WJ\\用户画像输入\\')

# 输入邮件地址, 口令和POP3服务器地址:
email = '671292565@qq.com'      #邮箱
password = 'xrzozgziucplbbbe'   #pop码
pop3_server = 'pop.qq.com'      #不要改！


def decode_str(s):  # 字符编码转换
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def get_att(msg):
    import email
    attachment_files = []

    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        contType = part.get_content_type()

        if file_name:
            h = email.header.Header(file_name)
            dh = email.header.decode_header(h)  # 对附件名称进行解码
            filename = dh[0][0]
            if dh[0][1]:
                filename = decode_str(str(filename, dh[0][1]))  # 将附件名称可读化
                print(filename)
                # filename = filename.encode("utf-8")
            if 'xls' in filename:
                data = part.get_payload(decode=True)  # 下载附件
                att_file = open('D:\\WJ\\用户画像输入\\' + filename, 'wb')  # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
                attachment_files.append(filename)
                att_file.write(data)  # 保存附件
                att_file.close()
            return attachment_files


def get_email_headers(msg):
    # 邮件的From, To, Subject存在于根对象上:
    headers = {}
    for header in ['From', 'To', 'Subject', 'Date']:
        value = msg.get(header, '')
        if value:
            if header == 'Date':
                headers['date'] = value
            if header == 'Subject':
                # 需要解码Subject字符串:
                subject = decode_str(value)
                headers['subject'] = subject
            else:
                # 需要解码Email地址:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
                if header == 'From':
                    from_address = value
                    headers['from'] = from_address
                else:
                    to_address = value
                    headers['to'] = to_address
    content_type = msg.get_content_type()
    print('head content_type: ', content_type)
    return headers


# 连接到POP3服务器,有些邮箱服务器需要ssl加密，对于不需要加密的服务器可以使用poplib.POP3()
server = poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
# 打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
# 身份认证:
server.user(email)
server.pass_(password)
# 返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# print(mails)
index = len(mails)

for i in range(index, 0, -1):
    # 倒序遍历邮件
    resp, lines, octets = server.retr(i)
    # lines存储了邮件的原始文本的每一行,
    # 邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8', "ignore")
    # 解析邮件:
    msg = Parser().parsestr(msg_content)

    # message = email.message_from_string(filename.decode("utf-8"))
    # sender = email.utils.parseaddr(message.get('from'))[1]
    # 获取邮件时间
    # date1 = time.strptime(msg.get("Date")[0:24], '%a, %d %b %Y %H:%M:%S')  # 格式化收件时间
    # print(date1)
    # date2 = time.strftime("%Y%m%d", date1)  # 邮件时间格式转换
    # print(date2)
    # if '20210917' < m:
    #     continue
    #
    #     print(msg)
    # f_list = get_att(msg)  # 获取附件
f_list = get_att(msg)
server.quit()
