cat ./data_vehicle/labels.txt | head -n  7000 > ./data_vehicle/train.txt
cat ./data_vehicle/labels.txt | tail -n +7001 > ./data_vehicle/test.txt
python core/convert_tfrecord.py --dataset_txt ./data_vehicle/train.txt --tfrecord_path_prefix ./data_vehicle/vehicle_train
python core/convert_tfrecord.py --dataset_txt ./data_vehicle/test.txt  --tfrecord_path_prefix ./data_vehicle/vehicle_test