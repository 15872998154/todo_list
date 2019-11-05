from todo_list import app, db
from flask import render_template, flash, redirect,url_for, request
from todo_list.forms import ListForm, DeadlineForm
from todo_list.models import List 
import datetime


@app.route('/', methods=['GET']) 
def index():
    return render_template('index.html')

#添加待办事项
@app.route('/add_item', methods=['GET', 'POST']) 
def add_item():
    form = ListForm()
    if form.validate_on_submit():
        transcation = List(title = form.data['title'], description = form.data['description'], status = form.data['tag'], deadline = form.data['deadline'])
        db.session.add(transcation)
        db.session.commit() 
        return redirect(url_for('list_item'))
    return render_template('add_item.html', form = form)

#所有待办事项
@app.route('/list_item', methods=['GET']) 
def list_item():
    todo_list = List.query.all()
    return render_template('list_item.html', todo_list = todo_list)

#删除待办事项
@app.route('/list_item/delete_item', methods=['GET']) 
def delete_item():
    item_id = request.args.get("item_id") #获取要删除的事项的ID
    delete_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    db.session.delete(delete_item)	 #删除该记录
    db.session.commit()
    return redirect(url_for('list_item'))

#完成事项
@app.route('/list_item/update_complete_status', methods=['GET']) 
def update_complete_status():
    item_id = request.args.get("item_id") #获取要修改的事项的ID
    update_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    update_item.status = 'Complete' #修改内容
    db.session.add(update_item)	    #提交操作
    db.session.commit()
    return redirect(url_for('complete_item'))

#显示修改事项页面
@app.route('/list_item/modify_item', methods=['GET']) 
def modify_item():
    item_id = request.args.get("item_id") #获取要修改的事项的ID
    modify_item = List.query.filter_by(id = item_id).first() #数据库查询该记录
    return render_template('modify_item.html', modify_item = modify_item, form = ListForm())    

#处理修改操作
@app.route('/list_item/modify_item', methods=['POST']) 
def deal_with_modify_item():
    modify_item = request.values.to_dict();
    modify_item_id = modify_item.get("modify_item_id") #获取要修改的事项的ID
    title = modify_item.get("title") 
    description = modify_item.get("description") 
    string_deadline = modify_item.get("deadline") 
    deadline = datetime.datetime.strptime(string_deadline, '%Y-%m-%d')
    tag = modify_item.get("tag") 
    modify_item = List.query.filter_by(id = modify_item_id).first() #数据库查询该记录
    modify_item.title = title
    modify_item.description = description
    modify_item.deadline = deadline
    modify_item.status = tag
    db.session.add(modify_item)	    #提交操作
    db.session.commit()
    return redirect(url_for('list_item'))    


#已完成待办事项    
@app.route('/complete_item', methods=['GET']) 
def complete_item():
    complete_items = List.query.filter(List.status == "Complete").all()
    return render_template('complete_item.html', complete_items = complete_items)

#未完成待办事项
@app.route('/uncomplete_item', methods=['GET']) 
def uncomplete_item():
    deadline_form = DeadlineForm()
    uncomplete_items = List.query.filter(List.status == "Uncomplete").all()
    return render_template('uncomplete_item.html', uncomplete_items = uncomplete_items, deadline_form = deadline_form)

@app.route('/deadline_search', methods=['GET', 'POST']) #已完成待办事项
def deadline_search():
    deadline_form = DeadlineForm()
    if deadline_form.validate_on_submit():
        deadline_form = DeadlineForm()
        uncomplete_items = List.query.filter(List.status == "Uncomplete").filter(List.deadline <= deadline_form.data['deadline']).all()
        return render_template('uncomplete_item.html', uncomplete_items = uncomplete_items, deadline_form = deadline_form)
    

	
		
	
	
	



