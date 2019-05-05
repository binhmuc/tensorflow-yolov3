cat ./thien_data/labels.txt | head -n  14 > ./thien_data/train.txt
cat ./thien_data/labels.txt | tail -n +2 > ./thien_data/test.txt
python core/convert_tfrecord.py --dataset_txt ./thien_data/train.txt --tfrecord_path_prefix ./thien_data/thien_train
python core/convert_tfrecord.py --dataset_txt ./thien_data/test.txt  --tfrecord_path_prefix ./thien_data/thien_test