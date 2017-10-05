# coding: utf8
import os
import glob
import sqlite3
import datetime
import json
import cgi
from bottle import Bottle, run, view, static_file, url, request, redirect, template, abort, response
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

app = Bottle()
# Define dirs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
# For chat broadcast
users = set()


def db_init():
    try:
        conn = sqlite3.connect('piratebox.db', timeout=10)
        db = conn.cursor()
        db.execute('CREATE TABLE IF NOT EXISTS CHAT(ID INTEGER PRIMARY KEY,'
                   'DATE, USR VARCHAR(100), MSG TEXT)')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print e


def disk_usage():
    """
    Return actual disk usage in kilobytes
    :return: <dict> {usage(%), color(css class)}
    """
    disk = os.statvfs("/")
    capacity = (disk.f_bsize * disk.f_blocks)/1.048576e6
    available = (disk.f_bsize * disk.f_bavail)/1.048576e6
    used = (disk.f_bsize * (disk.f_blocks - disk.f_bavail))/1.048576e6
    usage = 100-(round(100*used/capacity, 2))
    mydict = {'usage': usage, 'color': 'success'}
    return mydict


def get_gallery(typ):
    return [os.path.basename(x) for x in glob.glob(os.path.join(UPLOAD_DIR,
            typ)+"/**")]


def get_messages():
    conn = sqlite3.connect('piratebox.db', timeout=10)
    db = conn.cursor()
    # Loot table
    row = db.execute("SELECT * FROM CHAT LIMIT 100")
    result = row.fetchall()
    #messages = list(result)
    messages = []
    for tpl in result:
        msg = list(tpl)
        date = datetime.datetime.strptime(msg[1], "%Y-%m-%d %H:%M:%S.%f")
        #print str(date.hour) + "h" + str(date.minute)
        msg.append(" <small class='text-muted'>" + str(date.hour) + "h" 
                   + str(date.minute) + "</small>")
        msg.append(str(date.day) + "/" + str(date.month))
        messages.append(msg)
    return messages

# Static files route
@app.get('/static/<filename:path>')
def get_static_files(filename):
        """Get Static files"""
        return static_file(filename, root=STATIC_DIR)


# Upload files route
@app.get('/uploads/<filename:path>')
def get_upload_files(filename):
        """Get Static files"""
        return static_file(filename, root=UPLOAD_DIR)



@app.get('/websocket', apply=[websocket])
def chat(ws):
    users.add(ws)
    while True:
        line = json.loads(ws.receive())
        if line is not None:
            usr = cgi.escape(line[0])
            msg = cgi.escape(line[1])
            date = datetime.datetime.now()
            conn = sqlite3.connect('piratebox.db', timeout=10)
            db = conn.cursor()
            db.execute("INSERT INTO CHAT(DATE, USR, MSG)"
                       "VALUES (?, ?, ?)", (date, usr, msg))
            conn.commit()
            conn.close()
            date = " <small class='text-muted'>" + str(date.hour) + "h" + str(date.minute) + "</small>"
            for u in users:
                u.send("<b>" + usr + "</b> - " + date + "<br>&nbsp;&nbsp;&nbsp;" + msg)
        else:
            break
    users.remove(ws)


@app.route('/')
def home():
    name = request.get_cookie('w00tw00t')
    if name is None:
        cookie = 0
    else:
        cookie = 1
    # TEMPLATE
    context = {'title': 'pirat3box',
               'diskspace': disk_usage(),
               'error': request.query.error,
               'success': request.query.success,
               'audio': get_gallery('audio'),
               'video': get_gallery('video'),
               'img': get_gallery('img'),
               'others': get_gallery('others'),
               'chat': get_messages(),
               'cookie': cookie,
               'name': name}
    return template('layout/base', context)


@app.post('/upload')
def upload():
    """Handle file upload form"""
    # get the 'newfile' input from the form
    try:
        newfile = request.files.get('newfile')
        filetype = newfile.content_type
        audio = ['audio/mpeg','audio/aac','audio/mp4','audio/ogg','audio/wav']
        video = ['video/avi','video/msvideo','video/mp4','video/ogg']
        img = ['image/jpeg', 'image/pjpeg','image/png','image/gif']
        if filetype in audio:
            DEST_DIR = os.path.join(UPLOAD_DIR, 'audio')
        elif filetype in video:
            DEST_DIR = os.path.join(UPLOAD_DIR, 'video')
        elif filetype in img:
            DEST_DIR = os.path.join(UPLOAD_DIR, 'img')
        else: 
            DEST_DIR = os.path.join(UPLOAD_DIR, 'others')
        save_path = os.path.join(DEST_DIR, newfile.filename)
        newfile.save(save_path)
    except:
        redirect('/?error=Upload Error')
    return redirect('/?success=Fichier uploadé avec succès')

if __name__ == "__main__":
    db_init()
    run(app, host='0.0.0.0', port=8080, 
        reloader=True, debug=True,
        server=GeventWebSocketServer)
 

