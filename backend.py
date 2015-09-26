"""
Simple todo backend REST API
"""

import sqlite3
import cherrypy
import os
import datetime

from mako.lookup import TemplateLookup

class SQLiteDB(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def __enter__(self):
        self.db = sqlite3.connect("db.sqlite")
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.rollback()
        self.db.close()

    def commit(self):
        self.db.commit()

class TodoController(object):
    def __init__(self, templates):
        self.templates = templates

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update(self, id):
        ok = False
        todo = cherrypy.request.json["todo"]
        todo["due"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with SQLiteDB() as db:

            db.cursor.execute("UPDATE todo SET what = ?, done = ?, due = ? WHERE id = ?", (todo["what"], todo["done"], todo["due"], id))
            ok = db.db.total_changes > 0
            db.commit()

        return {"status": 0 if ok else 1}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def delete(self, id):
        ok = False
        with SQLiteDB() as db:
            db.cursor.execute("DELETE FROM todo WHERE id = ?", [id])
            ok = db.db.total_changes > 0
            db.commit()

        return {"status": 0 if ok else 1}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        jobj = {"todos": []}
        with SQLiteDB() as db:
            db.cursor.execute("SELECT * FROM todo")
            row = db.cursor.fetchone()
            while row:
                jobj["todos"].append({"todo": dict(zip(row.keys(), row))})
                row = db.cursor.fetchone()

        return jobj

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add(self):
        with SQLiteDB() as db:
            for todo in cherrypy.request.json["todos"]:
                todo = todo["todo"]

                todo["due"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                db.cursor.execute("INSERT INTO todo (id, what, done, due) VALUES(NULL, ?, ?, ?)", (todo["what"], todo["done"], todo["due"]))
            db.commit()

        return {"status": 0}

    def index(self):
        return self.templates.get_template("index.tpl").render()

if __name__ == '__main__':
    templates = TemplateLookup(directories=['templates'], module_directory='tmp')

    todo = TodoController(templates)

    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    dispatcher.connect(route = "/", controller = todo, action="index", name = "index", conditions=dict(method=["GET"]))
    dispatcher.connect(route = "/todo/add", controller = todo, action="add", name = "add", conditions=dict(method=["POST"]))
    dispatcher.connect(route = "/todo/get", controller = todo, action="get", name = "get", conditions=dict(method=["GET"]))
    dispatcher.connect(route = "/todo/delete/{id}", requirements={"id": "\d+"}, controller = todo, action="delete", name = "delete", conditions=dict(method=["DELETE"]))
    dispatcher.connect(route = "/todo/update/{id}", requirements={"id": "\d+"}, controller = todo, action="update", name = "update", conditions=dict(method=["PUT"]))

    app_conf =  {"/":
                    {"request.dispatch": dispatcher,
                     "tools.staticdir.root": os.path.dirname(os.path.realpath(__file__)),
                     "tools.staticdir.index": "index.html",
                    },
                 "/static":
                     {"tools.staticdir.on": True,
                      "tools.staticdir.dir": "static/"}
                }
    cherrypy.config.update({'engine.autoreload.on': False})

    cherrypy.quickstart(None, "/", app_conf)
