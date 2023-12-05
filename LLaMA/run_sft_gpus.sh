#! /bin/bash
#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --error=vasp.err
#SBATCH --gpus=1
#SBATCH --time=00:05:00
source /home//apps/package/pytorch/2.1.0+cuda118_cp310/env.sh
source activate py310


deepspeed --num_gpus 2 --master_port=9901 src/train_bash.py \
    --deepspeed ds_config.json \
    --stage sft \
    --model_name_or_path /home/liuhaifeng/.cache/modelscope/hub/ZhipuAI/chatglm2-6b \
    --do_train \
    --dataset dataset_sf \
    --template chatglm2 \
    --finetuning_type lora \
    --lora_target query_key_value\
    --output_dir /home/liuhaifeng/chatglm/lora/LLaMA-Factory-main/saves/ChatGLM2-6B-Chat/lora/version6 \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 100 \
    --learning_rate 1e-4 \
    --num_train_epochs 35.0 \
    --plot_loss \
    --fp16 



