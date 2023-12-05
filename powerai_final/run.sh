#! /bin/bash
#SBATCH --job-name=test
#SBATCH --output=test.out
#SBATCH --error=vasp.err
#SBATCH --gpus=1
source /home//apps/package/pytorch/2.1.0+cuda118_cp310/env.sh
source activate py310

python main.py