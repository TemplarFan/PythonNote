import tornado.ioloop
import tornado.web
import json

course ={
    "001": "Python",
    "002": "introduction of AI", 
    "003": "Software Engineering",
    }

import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("<h1>Hello, NEU.<h1>")
        # self.write
        self.render("index.html")

class CourseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(course))

    def post(self):
        cid = self.get_argument("cid")
        cname = self.get_argument("cname")
        if cid in course:
            self.write("Already exist.")
        else:
            course[cid] = cname
            self.write("success")

    def put(self):
        cid = self.get_argument("cid")
        cname = self.get_argument("cname")

        if cid in course:
            course[cid] = cname
            self.write("update successfull")
        else:
            self.write("not exist")

    def delete(self):
        cid = self.get_argument("cid")
        if cid in course:
            del course[cid]
            self.write("delete successfull")
        else:
            self.write("Not exist.")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/course", CourseHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()