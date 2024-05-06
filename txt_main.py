from xml_to_txt_trn import XmlToTxtTrnClass
from xml_to_txt_val import XmlToTxtValClass
import os
import shutil

# ## TRAIN

# - AIhub 데이터 XML > TXT

parent_folder_trn ='hub_data/train/label'
subfolders_trn = [f.path for f in os.scandir(parent_folder_trn) if f.is_dir()]

for folder_path in subfolders_trn:
    folder_name = os.path.basename(folder_path)

    # meta.xml을 불러와야 정상적으로 가능 
    xml_files = [file for file in os.listdir(folder_path) if "meta" in file and file.endswith(".xml")]    

    for xml_file_name in xml_files:
        xml_file_path = os.path.join(folder_path, xml_file_name)

        # 클래스 초기화 및 변환 수행
        converter = XmlToTxtTrnClass(xml_file_path)
        converter.toTxt()

# - labels 경로 내에 모든 txt 파일 넣기

# +
labels_folder = 'final_data/train/labels'

# 각 하위 폴더의 텍스트 파일을 labels 폴더로 이동
for root, dirs, files in os.walk(labels_folder):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            dest_path = os.path.join(labels_folder, file)
            shutil.move(file_path, dest_path)

# 모든 하위 폴더를 삭제 (단, labels 폴더는 지우지 않음)
for root, dirs, files in os.walk(labels_folder):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if dir_path != labels_folder:  # labels 폴더는 지우지 않음
            shutil.rmtree(dir_path)
# -

# - image 복사

# +
source_folder = 'hub_data/train/image'
destination_folder = 'final_data/train/images'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)
# -

# - robo_data image, label final_data로 복사

# +
source_folder = 'robo_data/train/images'
destination_folder = 'final_data/train/images'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)

# +
source_folder = 'robo_data/train/labels'
destination_folder = 'final_data/train/labels'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)
# -



# ## VALID

# - AIhub 데이터 XML > TXT

# ----------------------------------------------
parent_folder_val='hub_data/valid/label'
subfolders_val = [f.path for f in os.scandir(parent_folder_val) if f.is_dir()]

for folder_path in subfolders_val:
    folder_name = os.path.basename(folder_path)

    # meta.xml을 불러와야 정상적으로 가능 
    xml_files = [file for file in os.listdir(folder_path) if "meta" in file and file.endswith(".xml")]    

    for xml_file_name in xml_files:
        xml_file_path = os.path.join(folder_path, xml_file_name)

        # 클래스 초기화 및 변환 수행
        converter = XmlToTxtValClass(xml_file_path)
        converter.toTxt()

# - labels 경로 내에 모든 txt 파일 넣기

# +
labels_folder = 'final_data/valid/labels'

# 각 하위 폴더의 텍스트 파일을 labels 폴더로 이동
for root, dirs, files in os.walk(labels_folder):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            dest_path = os.path.join(labels_folder, file)
            shutil.move(file_path, dest_path)

# 모든 하위 폴더를 삭제 (단, labels 폴더는 지우지 않음)
for root, dirs, files in os.walk(labels_folder):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if dir_path != labels_folder:  # labels 폴더는 지우지 않음
            shutil.rmtree(dir_path)
# -
# - image 복사

# +
source_folder = 'hub_data/valid/image'
destination_folder = 'final_data/valid/images'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)
# -


# - robo_data image, label final_data로 복사

# +
source_folder = 'robo_data/valid/images'
destination_folder = 'final_data/valid/images'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)

# +
source_folder = 'robo_data/valid/labels'
destination_folder = 'final_data/valid/labels'

# source_folder의 파일을 destination_folder로 복사
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.copy(file_path, destination_folder)
# -


