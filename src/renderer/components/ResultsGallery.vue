<template>
  <div class="gallery">
    <div v-for="image in images" :key="image.id" class="gallery-item">
      <img :src="image.src" :alt="image.name" />
      <div class="actions">
        <button @click="downloadImage(image)" class="btn btn-sm">Download</button>
        <button @click="deleteImage(image)" class="btn btn-sm btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['download', 'delete'])

defineProps({
  images: Array
})

const downloadImage = (image) => {
  emit('download', image)
}

const deleteImage = (image) => {
  emit('delete', image)
}
</script>

<style scoped>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.gallery-item {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.actions {
  padding: 10px;
  display: flex;
  gap: 8px;
  background: #f9fafb;
}

.btn-sm {
  flex: 1;
  padding: 8px 12px;
  font-size: 12px;
}

.btn-danger {
  background: #ef4444;
  color: white;
}
</style>
