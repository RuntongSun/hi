# 创建应用实例
import sys

from wxcloudrun import app

@app.route('/wechat', methods=['GET', 'POST'])
def wechat_handler():
    # ... 处理微信消息 ...
    return 'ok', 200  # 简单返回'ok'作为响应，以确保路由设置正确


# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])
