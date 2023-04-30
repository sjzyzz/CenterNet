cd src
# train
# python main.py thu_multi_pose --exp_id dla_1x --dataset thu_basketball_hp --batch_size 96 --master_batch 32 --lr 5e-4 --load_model /root/CenterNet/models/multi_pose_dla_3x.pth --gpus 0,1,2 --num_workers 16 --trainval
python main.py thu_multi_pose --exp_id dla_1x --dataset thu_basketball_hp --batch_size 96 --master_batch 32 --lr 5e-4 --resume --gpus 0,1,2 --num_workers 16 --trainval
# test
python test.py thu_multi_pose --exp_id dla_1x --dataset thu_basketball_hp --keep_res --resume --trainval
# flip test
# python test.py multi_pose --exp_id dla_1x --dataset coco_hp --keep_res --resume --flip_test
cd ..