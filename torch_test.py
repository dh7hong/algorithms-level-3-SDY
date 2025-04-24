import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available. Using GPU:")
    print(f"Device name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA device count: {torch.cuda.device_count()}")
    print(f"Current device: {torch.cuda.current_device()}")
else:
    print("CUDA is not available. Using CPU.")