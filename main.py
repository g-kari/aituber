import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig

model_name = "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct"
model_name = "elyza/ELYZA-japanese-Llama-2-7b"
pretrained_model_dir = "ELYZA-7B-fast-inst-GPTQ"  # GPTQ量子化結果の格納ディレクトリ
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 4bit GPTQ設定、exllamaはモデルが全てGPUに乗らないとエラーになるのでdisableにする
gptq_config = GPTQConfig(
    bits=4,
    dataset="c4",
    tokenizer=tokenizer,
    use_exllama=False,
    cache_examples_on_gpu=False,
    use_cuda_fp16=True,
)
# 量子化前のモデルは極力GPUを使わないようにdevice_mapを定義
my_device_map = {
    "model.embed_tokens": "cpu",
    "model.layers": "cpu",
    "model.norm": "cpu",
    "lm_head": "cpu",
}
# Auto-GPTQがGPTQConfigの設定に従ってモデルを読み込んでくれる
quantized_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map=my_device_map,
    torch_dtype=torch.float16,
    quantization_config=gptq_config,
)
# Auto-GPTQで量子化されたモデルをsafetensors形式でローカルディレクトリに格納
quantized_model.to("cpu")
quantized_model.save_pretrained(pretrained_model_dir, safe_serialization=True)
tokenizer.save_pretrained(pretrained_model_dir)
