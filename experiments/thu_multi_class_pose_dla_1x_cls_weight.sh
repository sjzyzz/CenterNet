cd src
# train
python main.py multi_class_pose\
    --exp_id dla_1x_cls_weight_100 \
    --dataset thu_multi_class_pose \
    --batch_size 96 \
    --master_batch 36 --lr 5e-4 \
    --load_model ../exp/multi_class_pose/dla_3x_cls_weight_1/model_last.pth\
    --gpus 0,1,2 \
    --num_workers 16 \
    --trainval\
    --cls_weight 100 \
# test
python test.py  multi_class_pose\
    --exp_id dla_1x_cls_weight_100\
    --dataset thu_multi_class_pose\
    --keep_res \
    --resume \
    --trainval
cd ..