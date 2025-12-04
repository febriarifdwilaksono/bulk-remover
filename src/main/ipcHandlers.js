import { ipcMain } from 'electron'

ipcMain.handle('process-image', async (event, imagePath) => {
  try {
    // Flask backend call akan dilakukan di sini
    const response = await fetch('http://localhost:5000/process', {
      method: 'POST',
      body: JSON.stringify({ imagePath })
    })
    return await response.json()
  } catch (error) {
    return { error: error.message }
  }
})

ipcMain.handle('get-gpu-info', async (event) => {
  try {
    const response = await fetch('http://localhost:5000/gpu-info')
    return await response.json()
  } catch (error) {
    return { error: error.message }
  }
})
