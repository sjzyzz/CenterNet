cd src
# train
python main.py ctdet --exp_id thu_resdcn18 --arch resdcn_18 --batch_size 64 --master_batch -1 --lr 5e-4 --gpus 0 --num_workers 16 --resume
# test
python src/test.py ctdet --exp_id thu_resdcn18 --arch resdcn_18 --keep_res --resume
# flip test
# python test.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 --keep_res --resume --flip_test 
# multi scale test
# python test.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 --keep_res --resume --flip_test --test_scales 0.5,0.75,1,1.25,1.5
cd ..
