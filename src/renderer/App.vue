<template>
  <div id="app" class="app-container">
    <header class="app-header">
      <h1>🎨 Bulk Background Remover</h1>
      <p>Professional background removal with GPU acceleration</p>
    </header>

    <main class="app-main">
      <UploadArea @files-selected="handleFilesSelected" />
      
      <div v-if="processingFiles.length > 0" class="processing-section">
        <h2>Processing Queue</h2>
        <ProcessingQueue :files="processingFiles" />
      </div>

      <div v-if="processedImages.length > 0" class="results-section">
        <h2>Results</h2>
        <ResultsGallery :images="processedImages" />
      </div>
    </main>

    <footer class="app-footer">
      <p>© 2024 Bulk Background Remover - All Rights Reserved</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import UploadArea from './components/UploadArea.vue'
import ProcessingQueue from './components/ProcessingQueue.vue'
import ResultsGallery from './components/ResultsGallery.vue'

const processingFiles = ref([])
const processedImages = ref([])

const handleFilesSelected = async (files) => {
  processingFiles.value.push(...files)
  // Process files
}
</script>

<style scoped>
.app-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  text-align: center;
}

.app-main {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.app-footer {
  background: #f3f4f6;
  border-top: 1px solid #e5e7eb;
  padding: 20px;
  text-align: center;
  color: #6b7280;
}
</style>
