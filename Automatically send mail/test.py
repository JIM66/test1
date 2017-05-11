# import smtplib
# from email.mime.text import MIMEText
# import csv
# email_list = []
# f = open('E:\客户资料\客户资料列表.csv', 'r')
# try:
#     cs_list = csv.reader(f)
#     header = next(cs_list)
#     for i in cs_list:
#         print(i)
#         email_list.append(i[1])
#     # print(email_list)
#         if i[2] == '男':
#             b = i[0][0]+'先生，附件中是您在鱼米金服购买产品合同，请查收附件'
#         else:
#             b = i[0][0]+'女士，附件中是您在鱼米金服购买产品合同，请查收附件'
#         print(b)
#         msg = MIMEText(b)
#         msg['Subject'] = '蒋少兵'
#         msg['From'] = 'jim@shyumi.com'
#         for j in email_list:
#             msg['To'] = j
#             smtp = smtplib.SMTP()
#             smtp.connect('smtp.shyumi.com')
#             smtp.login(user='jim@shyumi.com', password='Jiang0110486')
#             smtp.send_message(msg)
#             smtp.quit()
# finally:
#     f.close()


import os
for i in os.listdir('E:\客户资料'):
    # print(i)
    # print(i.rfind('.'))
    # print(type(i))
    # print(i[i.rfind('.')+1:])
    if i[i.rfind('.')+1:] == 'pdf':
        print(i)


