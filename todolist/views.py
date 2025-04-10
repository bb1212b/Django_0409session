from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

#헬로우
def welcome(request):
    return render(request, 'welcome.html')

#업데이트 
def update(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        todo_item.title = title
        todo_item.description = description
        todo_item.save()
        return redirect('work')
    return render(request, 'update.html', {'todo_item': todo_item})

#삭제
def delete(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('work')
    return render(request, 'delete.html', {'todo_item': todo_item})

#작동
def work(request, todo_id=None):
    if todo_id is not None:  # todo_id가 전달된 경우
        todo_item = get_object_or_404(TodoItem, id=todo_id)
        return render(request, 'work.html', {'todo_item': todo_item})
    elif request.method == 'POST':  # POST 요청일 때
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        TodoItem.objects.create(title=title, description=description)
        return redirect('work_detail', todo_id=TodoItem.objects.latest('id').id)  # 생성된 항목의 ID로 리다이렉트
    else:  # GET 요청일 때
        return render(request, 'work.html')
    