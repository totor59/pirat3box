# coding: utf8
import os
import glob
import sqlite3
from bottle import Bottle, run, view, static_file, url, request, redirect, template, abort
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
                   'IP VARCHAR(100), USR VARCHAR(100), MSG TEXT)')
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
    messages = db.execute("SELECT * FROM CHAT LIMIT 100")
    return messages.fetchall()


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
        line = ws.receive()
        if line is not None:
            data = line.split(":", 1)
            usr = data[0]
            msg = data[1]
            ip = request.environ.get('REMOTE_ADDR')
            conn = sqlite3.connect('piratebox.db', timeout=10)
            db = conn.cursor()
            # Loot table
            db.execute("INSERT INTO CHAT(IP, USR, MSG)"
                       "VALUES (?, ?, ?)", (ip, usr, msg))
            conn.commit()
            conn.close()
            print usr, msg
            for u in users:
                u.send(line)
        else:
            break
    users.remove(ws)


@app.route('/')
def home():
    # UPLOAD
    disk = disk_usage()
    audio = get_gallery('audio')
    video = get_gallery('video')
    img = get_gallery('img')
    others = get_gallery('others')
    # TEMPLATE
    context = {'title': 'pirat3box',
               'diskspace': disk,
               'error': request.query.error,
               'success': request.query.success,
               'audio': audio,
               'video': video,
               'img': img,
               'others': others,
               'chat': get_messages()}
    return template('layout/base', context)


@app.post('/upload')
def upload():
    """Handle file upload form"""
    # get the 'newfile' field from the form
    newfile = request.files.get('newfile')
    # only allow upload of text files
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
    try:
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
 

