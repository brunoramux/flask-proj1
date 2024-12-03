from flask import Flask, request
from Models.task import Task

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
  data = request.get_json()
  task = Task(id=data.get("id"), title=data.get("title"), description=data.get("description"))
  tasks.append(task)
  print(tasks)
  return "Nova tarefa criada com sucesso"

if __name__ == "__main__":
  app.run(debug=True)