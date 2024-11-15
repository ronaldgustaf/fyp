import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import transformers
from langchain_huggingface import HuggingFacePipeline

class LlamaLLM:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        """
        Initialize the Llama 2 model with a given model name and access token.
        
        Parameters:
        - model_name (str): The name or path of the model on Hugging Face.
        - access_token (str): Your Hugging Face access token.
        - device (str): The device to load the model on (e.g., 'cuda' or 'cpu').
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = model_name
        self.access_token = open(r"./tokens.txt","r").read()

        # Load the tokenizer and model from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_auth_token=self.access_token)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name, 
            use_auth_token=self.access_token, 
            torch_dtype=torch.float16
        ).to(self.device)

        # Set up the pipeline for text generation
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if self.device == "cuda" else -1,  # 0 for GPU, -1 for CPU
            max_new_tokens=512,
            do_sample=True,
            return_full_text=False,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id
        )

        # Wrap the pipeline in a HuggingFacePipeline for easy integration with LangChain or other libraries
        self.llm = HuggingFacePipeline(pipeline=self.pipe, model_kwargs={'temperature': 0.1})

