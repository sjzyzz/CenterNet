cd src
# train
python main.py multi_class_pose\
     --exp_id dla_3x_cls_weight_1 \
     --dataset thu_multi_class_pose \
     --batch_size 96 \
    --master_batch 36 \
    --lr 5e-4 \
    --resume\
    --gpus 0,1,2 \
    --num_workers 16 \
    --trainval\
    --cls_weight 1 \
    --num_epochs 230 \
    --lr_step 180,210
# test
python src/test.py multi_class_pose\
    --exp_id dla_3x_cls_weight_1\
    --dataset thu_multi_class_pose\
    --keep_res \
    --resume \
    --trainval
cd ..