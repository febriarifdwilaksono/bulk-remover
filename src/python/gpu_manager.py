import torch

def check_gpu():
    gpu_available = torch.cuda.is_available()
    
    info = {
        'gpu_available': gpu_available,
        'device': 'cuda' if gpu_available else 'cpu'
    }
    
    if gpu_available:
        info['gpu_name'] = torch.cuda.get_device_name(0)
        info['gpu_memory'] = torch.cuda.get_device_properties(0).total_memory / 1024**3
        info['cuda_version'] = torch.version.cuda
    
    return info
