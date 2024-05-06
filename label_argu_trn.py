import os
import shutil

# +
folder_path = 'final_data/train/labels'

# 폴더 내 txt 파일 이외의 파일은 삭제
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if not file.lower().endswith('.txt'):
            os.remove(file_path)
            print(f"'{file_path}' 파일을 삭제했습니다.")


# +
import os
import shutil

def copy_with_prefix(input_folder, output_folder, prefix):
    # 각 라벨 파일을 처리합니다.
    for filename in os.listdir(input_folder):
        if not filename.startswith('.ipynb_checkpoints'):  # .ipynb_checkpoints를 건너뜁니다.
            os.makedirs(output_folder, exist_ok=True)
            input_folder_path = os.path.join(input_folder, filename)
            output_folder_path = os.path.join(output_folder, f'{prefix}_{filename}')

            # 파일 복사
            shutil.copy2(input_folder_path, output_folder_path)
            
input_folder = 'final_data/train/labels' # 입력 이미지 폴더 경로
output_folder = 'final_data/train/labels_pre' # 출력 이미지 폴더 경로

# 다양한 변형에 대해 함수 호출
transformations = ['Brightness', 'Exposure', 'Blur', 'Noise', 'Cutout']
for transform in transformations:
    copy_with_prefix(input_folder, output_folder, transform)

print("라벨 파일 이름이 성공적으로 변경되었습니다.")
# -

# - 파일 이동 및 확인

# +
source_folder = 'final_data/train/labels_pre'
destination_folder = 'final_data/train/labels'

# source_folder의 파일을 destination_folder로 이동
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.move(file_path, destination_folder)

# +
source_folder = 'final_data/train/labels'

# 폴더 내 파일 수 세기
file_count = sum(len(files) for _, _, files in os.walk(source_folder))

print(f"폴더 '{source_folder}'에는 총 {file_count}개의 파일이 있습니다.")
# -



