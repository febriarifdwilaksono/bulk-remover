<template>
  <div class="upload-area" @dragover="dragover = true" @dragleave="dragover = false" @drop="handleDrop">
    <div class="upload-content" :class="{ dragover }">
      <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
        <polyline points="17 8 12 3 7 8"></polyline>
        <line x1="12" y1="3" x2="12" y2="15"></line>
      </svg>
      <h3>Drop images here or click to upload</h3>
      <p>Supported: JPG, PNG, WebP</p>
      <input type="file" multiple @change="handleFileSelect" accept="image/*" style="display: none;" ref="fileInput" />
      <button @click="$refs.fileInput.click()" class="btn btn-primary">Select Files</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['files-selected'])
const dragover = ref(false)
const fileInput = ref(null)

const handleFileSelect = (e) => {
  emit('files-selected', Array.from(e.target.files))
}

const handleDrop = (e) => {
  e.preventDefault()
  dragover.value = false
  emit('files-selected', Array.from(e.dataTransfer.files))
}
</script>

<style scoped>
.upload-area {
  border: 2px dashed #cbd5e1;
  border-radius: 8px;
  padding: 40px;
  text-align: center;
  transition: all 0.3s ease;
}

.upload-area.dragover {
  border-color: #667eea;
  background: #f0f4ff;
}

.upload-icon {
  width: 48px;
  height: 48px;
  color: #667eea;
  margin-bottom: 16px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover {
  background: #5568d3;
}
</style>
