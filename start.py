# coding: utf8
import os
from bottle import Bottle, run, view, static_file, url, request, redirect

app = Bottle()
# Define dirs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')


def disk_usage():
    """
    Return actual disk usage in kilobytes
    :return: <tuple> (capacity, available, used) 
    """
    disk = os.statvfs("/")
    capacity = (disk.f_bsize * disk.f_blocks)/1.048576e6
    available = (disk.f_bsize * disk.f_bavail)/1.048576e6
    used = (disk.f_bsize * (disk.f_blocks - disk.f_bavail))/1.048576e6
    usage = 100-(round(100*used/capacity ,2))
    mydict = {'usage': usage, 'color': 'success'}
    return mydict


# Static files route
@app.get('/static/<filename:path>')
def get_static_files(filename):
        """Get Static files"""
        return static_file(filename, root=STATIC_DIR)

@app.route('/')
@view('views/chat.tpl')
def chat():
    context = {'content': 'Hello Bottle.py'}
    return context


@app.route('/')
@view('views/gallery.tpl')
def gallery():
    disk = disk_usage() 
    context = {'content': 'Hello Bottle.py',
               'diskspace': disk,
               'error': request.query.error,
               'success': request.query.success}
    return context


@app.post('/upload')
def upload():
    """Handle file upload form"""
    # get the 'newfile' field from the form
    newfile = request.files.get('newfile')
    # only allow upload of text files
    if newfile.content_type != 'text/plain':
        return redirect('/?error=Only text files allowed')
    try:
        save_path = os.path.join(UPLOAD_DIR, newfile.filename)
        newfile.save(save_path)
    except:
        redirect('/?error=Upload Error')
    return redirect('/?success=Fichier uploadé avec succès')

if __name__ == "__main__":
    run(app, host='localhost', port=8080, reloader=True, debug=True)
