## 进行评测 mmlu
CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli eval \
--model_name_or_path /home/chuokun_xu/model/Meta-Llama-3-8B-Instruct \
--template llama3 \
--task ceval_test \
--lang en \
--n_shot 5 \
--batch_size 1

