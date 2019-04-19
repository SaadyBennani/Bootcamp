class TodoList {
  constructor() {
    this.todos = []
  }

  addTodo(task) {
    this.todos.push({task, completed: false})
  }

  toggleComplete(idx) {
    let todo = this.todos[idx]
    todo.completed = !todo.completed
    }

  deleteTodo(idx) {
    this.todos = this.todos.filter((todo, i) => i !== idx)
  }
}

// functions
  const createTodoElement = (text) => {
  const elem = document.createElement('li')
  const deleteBtn = document.createElement('a')
  const toggleBtn = document.createElement('a')

  deleteBtn.innerHTML = '<i class = "fas fa-times"></i'
  deleteBtn.setAttribute('class', 'delete')
  toggleBtn.innerHTML = '<i class = "fas fa-check"></i'
  toggleBtn.setAttribute('class', 'toggle')




  elem.innerText = text
  elem.appendChild(deleteBtn)
  elem.appendChild(toggleBtn)

  //btn event listeners
  deleteBtn.addEventListener('click', (evt) =>{
    const li = evt.target.closest('li')
    const idx = parseInt(li.getAttribute('idx'))
    todoList.deleteTodo(idx)
    update(todoList)

  })

  toggleBtn.addEventListener('click', (evt) =>{
    const li = evt.target.closest('li')
    const idx = parseInt(li.getAttribute('idx'))
    todoList.toggleComplete(idx)
    update(todoList)
  })

  return elem
}

const update = (list) => {
    // clear all children from todosContainer
    while (todoContainer.lastChild) {
        todoContainer.removeChild(todoContainer.lastChild);
    }

    // map all todos to a new <li> element
    list.todos.map((todo, idx) => {
        const child = createTodoElement(todo.task)
        child.setAttribute('idx', idx)
        if (todo.completed) {
          child.classList.add('completed')
        } else {
          child.classList.remove('completed')
        }
        todoContainer.appendChild(child)
    })
}
//initialize todos
const todoList = new TodoList()

//selectors
const todoInput = document.querySelector('#todo-input')
const todoContainer = document.querySelector('#todo-container')

//event listeners
todoInput.addEventListener('keydown', (evt) => {
  if (evt.key==='Enter') {
    todoList.addTodo(todoInput.value)
    // todoContainer.appendChild(createTodoElement(todoInput.value))
    update(todoList)
    todoInput.value = ''
  }

})
