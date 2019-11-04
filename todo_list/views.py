from todo_list import app, db
from flask import render_template, flash, redirect,url_for, request

from todo_list.forms import ListForm
from todo_list.models import List
# from 

@app.route('/add_item', methods=['GET', 'POST']) #添加待办事项
def add_item():
    form = ListForm()
    if form.validate_on_submit():
        transcation = List(title = form.data['title'], description = form.data['description'], status = form.data['tag'], deadline = form.data['deadline'])
        db.session.add(transcation)
        db.session.commit() 
        return redirect(url_for('list_item'))
    return render_template('add_item.html', form = form)


@app.route('/list_item', methods=['GET']) #显示所有待办事项
def list_item():
    todo_list = List.query.all()
    return render_template('list_item.html', todo_list = todo_list)


@app.route('/list_item/delete_item', methods=['GET']) #删除待办事项
def delete_item():
    item_id = request.args.get("item_id") #获取要删除的事项的ID
    delete_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    db.session.delete(delete_item)	 #删除该记录
    db.session.commit()
    return redirect(url_for('list_item'))

@app.route('/list_item/update_complete_status', methods=['GET']) #显示待办事项页面
def update_complete_status():
    item_id = request.args.get("item_id") #获取要修改的事项的ID
    update_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    update_item.status = 'Complete' #修改内容
    db.session.add(update_item)	    #提交操作
    db.session.commit()
    return redirect(url_for('complete_item'))

@app.route('/list_item/modify_item', methods=['GET']) #显示待办事项页面
def modify_item():
    item_id = request.args.get("item_id") #获取要修改的事项的ID
    
    modify_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    return render_template('modify_item.html', modify_item = modify_item, form = ListForm())    
    
@app.route('/complete_item', methods=['GET']) #已完成待办事项
def complete_item():
    complete_items = List.query.filter(List.status == "Complete").all()
    return render_template('complete_item.html', complete_items = complete_items)

@app.route('/uncomplete_item', methods=['GET']) #未完成待办事项
def uncomplete_item():
    uncomplete_items = List.query.filter(List.status == "Uncomplete").all()
    return render_template('uncomplete_item.html', uncomplete_items = uncomplete_items)





