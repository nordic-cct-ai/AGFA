import os
import shutil
import nibabel as nib

# path_to_imagecas_data = "/media/fredrik/data/backup_IDUN/coronary_artery_segmentation/data/data_coronary_ImageCAS"
# path_to_imagecas_data_restructured = "/media/fredrik/server_data/data_imageCas_restructured/subset_3"
path_to_imagecas_data = "/media/fredrik/data/backup_IDUN/coronary_artery_segmentation/data/data_coronary_ImageCAS"
path_to_imagecas_data_restructured = "/media/fredrik/server_data/data_imageCas_restructured/subset_4"
train_folder = os.path.join(path_to_imagecas_data_restructured, "train")
train_folder_label = os.path.join(path_to_imagecas_data_restructured, "trainMask")
val_folder = os.path.join(path_to_imagecas_data_restructured, "val")
val_folder_label = os.path.join(path_to_imagecas_data_restructured, "valMask")
all_cases = []
training_cases = []
f_train = open("train.txt", "w")
validation_cases = []
f_val = open("val.txt", "w")
test_cases = []
f_test = open("test.txt", "w")

train_val_test_n = [200, 10, 10]
n_iter = 1
n_iter_val = 1
n_iter_test = 1
for tmp_folder in os.listdir(path_to_imagecas_data):

    if tmp_folder.endswith(")"):
        pass
    else:
        if n_iter <= train_val_test_n[0]:
            training_cases.append(str(tmp_folder))
            f_train.write(str(tmp_folder))
            if n_iter < train_val_test_n[0]:
                f_train.write("\n")
        n_iter +=1

        if n_iter_val <= train_val_test_n[1] and n_iter > train_val_test_n[0]:
            validation_cases.append(str(tmp_folder))
            f_val.write(str(tmp_folder))
            if n_iter_val < train_val_test_n[1]:
                f_val.write("\n")
            n_iter_val +=1
        if n_iter_test <= train_val_test_n[2] and n_iter > train_val_test_n[0] + train_val_test_n[0]:
            test_cases.append(str(tmp_folder))
            f_test.write(str(tmp_folder))
            if n_iter_test < train_val_test_n[2]:
                f_test.write("\n")
            n_iter_test +=1
print(training_cases)
print(validation_cases)
print(test_cases)
f_train.close()
f_val.close()
f_test.close()

os.makedirs(train_folder, exist_ok=True)
os.makedirs(train_folder_label, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(val_folder_label, exist_ok=True)

for tmp_case in training_cases:
    case_folder = os.path.join(path_to_imagecas_data, tmp_case)


    src_img = os.path.join(case_folder, "img.nii.gz")
    src_label = os.path.join(case_folder, "label.nii.gz")
    dst_img = os.path.join(train_folder, f"{tmp_case}.nii.gz")
    dst_label = os.path.join(train_folder_label, f"{tmp_case}.nii.gz")
    epi_img = nib.load(src_img)
    print(epi_img.shape)
    #if epi_img.shape[2] >= 275:
    shutil.copyfile(src_img, dst_img)
    shutil.copyfile(src_label, dst_label)

for tmp_case in validation_cases:
    case_folder = os.path.join(path_to_imagecas_data, tmp_case)


    src_img = os.path.join(case_folder, "img.nii.gz")
    src_label = os.path.join(case_folder, "label.nii.gz")
    dst_img = os.path.join(val_folder, f"{tmp_case}.nii.gz")
    dst_label = os.path.join(val_folder_label, f"{tmp_case}.nii.gz")
    epi_img = nib.load(src_img)
    print("val: ", epi_img.shape)
    # if epi_img.shape[2] >= 275:
    #     shutil.copyfile(src_img, dst_img)
    #     shutil.copyfile(src_label, dst_label)
    # else:
    shutil.copyfile(src_img, dst_img)
    shutil.copyfile(src_label, dst_label)

