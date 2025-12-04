<template>
  <div class="queue">
    <div v-for="file in files" :key="file.name" class="queue-item">
      <span>{{ file.name }}</span>
      <div class="progress">
        <div class="progress-bar" :style="{ width: file.progress + '%' }"></div>
      </div>
      <span class="status">{{ file.status }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  files: Array
})
</script>

<style scoped>
.queue {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.queue-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background: #f9fafb;
  border-radius: 4px;
}

.progress {
  flex: 1;
  height: 4px;
  background: #e5e7eb;
  border-radius: 2px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: #667eea;
  transition: width 0.3s;
}

.status {
  font-size: 12px;
  color: #6b7280;
}
</style>
