import transformers
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# model_id = "meta-llama/Meta-Llama-2-7b"
model_dir = "./llama-models-main/models/llama2/Llama-2-7b"

model = LlamaForCausalLM.from_pretrained(model_dir)
tokenizer = LlamaTokenizer.from_pretrained(model_dir)

pipeline = transformers.pipeline(
  "text-generation",
  model="meta-llama/Meta-Llama-2-7b",
  model_kwargs={"torch_dtype": torch.bfloat16},
  device="cuda",
)

sequences = pipeline(
'I have tomatoes, basil and cheese at home. What can I cook for dinner?\n',

do_sample=True,

top_k=10,

num_return_sequences=1,

eos_token_id=tokenizer.eos_token_id,

max_length=400,

)

for seq in sequences:
  print(f"{seq['generated_text']}")