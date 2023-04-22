cd src
# train
# python main.py multi_pose --exp_id res_18 --arch res_18 --dataset thu_basketball_hp --batch_size 128 --master_batch 9 --lr 5e-4 --gpus 0,1,2,3 --num_workers 16
# test
python test.py multi_pose --exp_id res_18 --arch res_18 --dataset thu_basketball_hp --keep_res --resume
# flip test
# python test.py multi_pose --exp_id dla_1x --dataset coco_hp --keep_res --resume --flip_test
cd ..
