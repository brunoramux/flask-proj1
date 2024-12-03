from flask import Flask, request, jsonify
from Models.task import Task

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  task = Task(id=data.get("id"), title=data.get("title"), description=data.get("description"))
  tasks.append(task)
  print(tasks)
  return jsonify({"message": "Tarefa criada com sucesso."})

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = []
  for task in tasks:
    task_list.append(task.to_dict())
  
  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }
  return jsonify(output)

@app.route('/task/<int:id>', methods=['GET'])
def get_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
  
  return jsonify({
    "message": "Tarefa não encontrada."
  })
  
@app.route('/task/<int:id>', methods=["PUT"])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
  if task == None:
    return jsonify({
      "message": "Não foi possível encontrar a tarefa"
    }), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  
  return jsonify({
    "message": "Tarefa atualizada com sucesso."
  })
  
@app.route('/task/<int:id>', methods=["DELETE"])
def delete_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
  if task == None:
    return jsonify({
      "message": "Não foi possível encontrar a tarefa"
    }), 404
  
  tasks.remove(task)
  return jsonify({
    "message": "Tarefa deletada com sucesso."
  })
 
if __name__ == "__main__":
  app.run(debug=True)