
from forms.test2_form import test2_form
from forms.adduser_form  import adduser_form
from services.test2_service import UserService
from services.baidu_service import baiduService
from routes import app
from test_a import render_template,flash, redirect, url_for,request,jsonify
from flask_login import login_required
from models.test2 import User
from forms.sucess_form import sucess_form


@app.route('/')
@app.route('/index.html')
def index():
    return "hello my world!!"

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/test2.html', methods=['GET', 'POST'])
def test2():
    test2form = test2_form()
    if test2form.validate_on_submit():
        result = UserService().do_login(username=test2form.username.data, password=test2form.password.data)
        if result:
            flash(f'欢迎{test2form.username.data}回来', category='success')
            return redirect(url_for('sucess'))
        else:
            flash('用户名或密码错误，请重试!', category='danger')
    return render_template('test2.html',form=test2form)

@app.route('/adduser.html', methods=['GET', 'POST'])
@login_required
def adduser():
    adduserform = adduser_form()
    new_adduser = User()
    new_adduser.userid = adduserform.addusername.data
    new_adduser.userpwd =adduserform.addpwd.data
    if adduserform.validate_on_submit():
        result,error_msg = UserService().do_adduser(user=new_adduser)
        if error_msg:
            flash('error', category='danger')
            
        else:
            flash(f'sucess', category='success')
            return render_template('sucess.html')
    return render_template('adduser.html',form=adduserform)


@app.route('/sucess.html', methods=['GET'])
@login_required
def sucess():
    sucessform = sucess_form()
    
    return render_template('sucess.html')
    #return render_template('sucess.html',form=sucessform)

@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    result,error_msg = baiduService().do_question(request.form['message'])
    if error_msg:
        flash('error', category='danger')
    else:

        message = request.form['message']
        
        fulfillment_text = result
        response_text = { "message":  fulfillment_text }
                    
    return jsonify(response_text)
