from flask import Blueprint


admin_page = Blueprint('admin', __name__)


@admin_page.route('/admin/objects', methods=['GET'])
def get():
    """
    FIXME: Create debug purpose file input UI
    """
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data action=/objects>
      <input type=file name=graphic_model>
      <input type=submit value=Upload>
    </form>
    '''

