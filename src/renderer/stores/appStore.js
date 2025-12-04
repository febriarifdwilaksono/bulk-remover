import { reactive } from 'vue'

export const appStore = reactive({
  processingFiles: [],
  processedImages: [],
  gpuInfo: null,
  currentMode: 'standard',

  addProcessingFile(file) {
    this.processingFiles.push({
      name: file.name,
      progress: 0,
      status: 'pending'
    })
  },

  updateProgress(index, progress) {
    if (this.processingFiles[index]) {
      this.processingFiles[index].progress = progress
    }
  },

  addProcessedImage(image) {
    this.processedImages.push(image)
  },

  removeProcessedImage(id) {
    this.processedImages = this.processedImages.filter(img => img.id !== id)
  }
})
