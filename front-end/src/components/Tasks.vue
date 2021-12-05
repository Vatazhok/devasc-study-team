<template>
  <div :key="task.id" v-for="(task, index) in tasks">
    <Task
      @toggle-reminder="$emit('toggle-reminder', index, task.reminder)"
      @delete-task="$emit('delete-task', index, task.id)"
      :task="task"
    />
  </div>
</template>

<script>
import Task from './Task'

export default {
  name: 'Tasks',
  props: {
    tasks: {},
  },
  components: {
    Task,
  },
  emits: ['delete-task', 'toggle-reminder'],
}
</script>
