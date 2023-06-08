from transformers import AutoModelForCausalLM, AutoTokenizer
from optimum.bettertransformer import BetterTransformer

def load_model(
    base, 
    finetuned, 
    mode_cpu,
    mode_mps,
    mode_full_gpu,
    mode_8bit,
    mode_4bit,
    force_download_ckpt
):
    tokenizer = AutoTokenizer.from_pretrained(base, trust_remote_code=True)
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        base, 
        load_in_8bit=mode_8bit, 
        load_in_4bit=mode_4bit,
        device_map="auto",
        trust_remote_code=True)

    if not mode_8bit and not mode_4bit:
        model.half()

    model = BetterTransformer.transform(model)
    return model, tokenizer