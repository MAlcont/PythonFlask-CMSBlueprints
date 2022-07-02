from flask import Blueprint, render_template, abort
from cms.admin.models import Type, Content, Setting, User

admin_bp = Blueprint('admin', , url_prefix='/admin')

@admin.route('/admin/', defaults={'type': 'page'})
@admin.route('/admin/<type>')
def content(type):
    if requested_type(type):
        content = Content.query.join(Type).filter(Type.name == type)
        return render_template('admin/content.html', type=type, content=content)
    else:
        abort(404)

@admin.route('/admin/create/<type>')
def create(type):
    if requested_type(type):
        types = Type.query.all()
        return render_template('admin/content_form.html', title='Create', types=types, type_name=type)
    else:
        abort(404)

@admin.route('/admin/users')
def users():
    users = User.query.all()
    return render_template('admin/users.html', title='Users', users=users)

@admin.route('/admin/settings')
def settings():
    settings = Setting.query.all()
    return render_template('admin/settings.html', title='Settings', settings=settings)

def requested_type(type):
    types = [row.name for row in Type.query.all()]
    return True if type in types else False