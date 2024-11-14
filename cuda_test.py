import torch

print()
# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
    
    
# import transformers
# import torch

# model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

# pipeline = transformers.pipeline(
#   "text-generation",
#   model="meta-llama/Meta-Llama-3.1-8B-Instruct",
#   model_kwargs={"torch_dtype": torch.bfloat16},
#   device="cuda",
# )

# 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