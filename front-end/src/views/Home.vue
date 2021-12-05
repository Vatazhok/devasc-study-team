<template>
  <AddTask v-show="showAddTask" @add-task="addTask" />
  <Tasks
    @toggle-reminder="toggleReminder"
    @delete-task="deleteTask"
    :tasks="tasks"
  />
</template>

<script>
import Tasks from '../components/Tasks'
import AddTask from '../components/AddTask'

export default {
  name: 'Home',
  props: {
    showAddTask: Boolean,
  },
  components: {
    Tasks,
    AddTask,
  },
  data() {
    return {
      tasks: [],
    }
  },
  methods: {
    async addTask(task) {
      const addTask = await fetch('http://127.0.0.1:5000', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(task),
      })

      const res = await fetch('http://127.0.0.1:5000')

      this.tasks = await res.json()
    },
    async deleteTask(index, id) {
      if (confirm('Are you sure?')) {
        const res = await fetch(`http://127.0.0.1:5000/?id=${index+1}`, {
          method: 'DELETE',
        })

        res.status === 200
          ? (this.tasks = this.tasks.filter((task) => task.id !== id))
          : alert('Error deleting task')
      }
    },
    async toggleReminder(index, reminder) {
      reminder = reminder === false;

      const res = await fetch(`http://127.0.0.1:5000/?id=${index+1}&reminder=${reminder}`, {
        method: 'PUT',
      })

      const data = await res.json()

      this.tasks = this.tasks.map((task) =>
        task.id === index ? { ...task, reminder: reminder } : task
      )
    },
    async fetchTasks() {
      const res = await fetch('http://127.0.0.1:5000')

      const data = await res.json()

      return data
    },
  },
  async created() {
    this.tasks = await this.fetchTasks()
  },
}
</script>
