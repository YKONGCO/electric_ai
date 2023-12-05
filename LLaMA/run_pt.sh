#! /bin/bash
#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --error=vasp.err
#SBATCH --gpus=1
#SBATCH --time=00:05:00
source /home//apps/package/pytorch/2.1.0+cuda118_cp310/env.sh
source activate py310


CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage pt \
    --model_name_or_path /home/bingxing2/home/scx6d3v/.cache/modelscope/hub/ZhipuAI/chatglm2-6b \
    --do_train \
    --dataset all \
    --template chatglm2 \
    --finetuning_type lora \
    --lora_target query_key_value \
    --output_dir /home/bingxing2/home/scx6d3v/chatglm/lora/LLaMA-Factory-main/saves/lora/version_pt_1 \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 100 \
    --learning_rate 1e-4 \
    --num_train_epochs 25.0 \
    --plot_loss \
    --fp16 



