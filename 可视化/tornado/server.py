import tornado.web
import tornado.ioloop
import tornado.httpserver

from pyecharts.charts import Bar
from pyecharts import options as opts


def bar_base() -> str:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c.dump_options()


def set_default_header(self):
    # 后面的*可以换成ip地址，意为允许访问的地址
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE")
    self.set_header("Content-Type", "application/json; charset=UTF-8")


class BarChart(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        set_default_header(self)
        chart_result = bar_base()
        # 返回结果
        self.write(chart_result)
        self.finish()


class PageHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.render("index-bak.html")


def make_app():
    return tornado.web.Application([
        (r"/", PageHandler),
        (r"/getBarChart", BarChart),
    ])


if __name__ == "__main__":
    port = 8889
    app = make_app()
    sockets = tornado.netutil.bind_sockets(port)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.add_sockets(sockets)
    print("Server Start Running!\nHost: {} Port: {}".format("127.0.0.1", port))
    tornado.ioloop.IOLoop.instance().start()