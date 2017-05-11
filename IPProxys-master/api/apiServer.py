'''
定义几个关键字，count type,protocol,country,area,
'''
import urllib
import http.server
import json
from urllib.request import urlparse
import logging
from config import API_PORT
from db.SQLiteHelper import SqliteHelper

__author__ = 'Xaxdus'
logger = logging.getLogger('api')  # 日志记录

# keylist=['count', 'types','protocol','country','area']


class WebRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_get(self):  # 请注意之前是do_GET(self)
        """
        """
        ip_dict = {}  # 之前是dict

        parsed_path = urlparse.urlparse(self.path)
        # 定义一个获取成功链接的返回结果
        try:
            query = urllib.unquote(parsed_path.query)
            # print(query)  # 测试输出
            logger.info("query %s" % query)  # 指定query指定给logger
            # 获取返回的url的值
            if query.find('&') != -1:
                param_list = query.split('&')
                for param in param_list:
                    ip_dict[param.split('=')[0]] = param.split('=')[1]
            else:
                    ip_dict[query.split('=')[0]] = query.split('=')[1]

            sql_helper = SqliteHelper()  #
            # 处理删除代理的请求
            if 'delete' in ip_dict:   # 之前的写法dict.has_key('delete')
                condition = "ip='" + ip_dict['ip'] + "' AND port=" + ip_dict['port']
                sql_helper.delete(SqliteHelper.tableName, condition)
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Success delete proxy: " + ip_dict['ip'] + ":" + ip_dict['port'])
            else:
                str_count = ''
                conditions = []
                for key in ip_dict:
                    if key == 'count':
                        str_count = 'LIMIT 0,%s' % ip_dict[key]
                    if key == 'country' or key == 'area':
                        conditions .append(key+" LIKE '"+ip_dict[key]+"%'")
                    elif key == 'types' or key == 'protocol' or key == 'country' or key == 'area':
                        conditions .append(key+"="+ip_dict[key])
                if len(conditions) > 1:
                    conditions = ' AND '.join(conditions)
                else:
                    conditions = conditions[0]
                result = sql_helper.select(sql_helper.tableName, conditions, str_count)
                # print type(result)
                # for r in  result:
                #     print r
                data = [{'ip': item[0], 'port': item[1]} for item in result]  # 返回有效的ip数据
                data = json.dumps(data)  # 生成json数据格式
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            logger.warning(str(e))
            self.send_response(404)

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', API_PORT), WebRequestHandler)
    server.serve_forever()
