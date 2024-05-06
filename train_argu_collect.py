import torch
from torchvision import transforms
from PIL import Image
import os
import numpy as np
import random
import shutil

# ## 이미지 Preprocessing 및 Argument

input_folder = 'final_data/train/images/' # 입력 이미지 폴더 경로
output_folder = 'final_data/train/images_pre/' # 출력 이미지 폴더 경로
os.makedirs(output_folder, exist_ok=True)

### Brightness --------------------------------------------------------------------------------------
Brightness = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ColorJitter(brightness=(1.0, 2.5), # 밝기 
                           ),
    transforms.ToTensor()
])

for filename in os.listdir(input_folder):
    try:
        # 이미지 열기
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img = Brightness(img) # 이미지 전처리 및 augmentation 적용

        output_path = os.path.join(output_folder, f'Brightness_{filename}') # 저장할 경로 지정

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(output_path)

    except Exception as e:
        print(f'Brightness_{filename} 저장 실패: {e}')

### Blur -------------------------------------------------------------------------------------------
Blur = transforms.Compose([
    transforms.Resize((224, 224)),              
    # GaussianBlur 적용
    transforms.GaussianBlur(kernel_size=(19, 19), sigma=(0.3, 0.9)), # sigma를 조절하면 흐림 조절가능
    transforms.ToTensor()
])

for filename in os.listdir(input_folder):
    try:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img = Blur(img) # 이미지 전처리 및 augmentation 적용

        output_path = os.path.join(output_folder, f'Blur_{filename}') # 저장할 경로 지정

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(output_path)

    except Exception as e:
        print(f'Blur_{filename} 저장 실패: {e}')

### Cutout ----------------------------------------------------------------------------------------
class CUTOUT:
    def __init__(self, n_holes=1, length=40):
        self.n_holes = n_holes
        self.length = length

    def __call__(self, img):
        img = np.array(img)
        h, w, _ = img.shape

        for _ in range(self.n_holes):
            y = random.randint(self.length // 2, h - 1 - self.length // 2)
            x = random.randint(self.length // 2, w - 1 - self.length // 2)
            #y = random.randint(0, h - 1)
            #x = random.randint(0, w - 1)

            y1 = np.clip(y - self.length // 2, 0, h)
            y2 = np.clip(y + self.length // 2, 0, h)
            x1 = np.clip(x - self.length // 2, 0, w)
            x2 = np.clip(x + self.length // 2, 0, w)

            img[y1:y2, x1:x2] = 0

        return Image.fromarray(img)

cutout = transforms.Compose([
    transforms.Resize((224, 224)),              
    CUTOUT(n_holes=2, length=40),  # Cutout augmentation 적용
    transforms.ToTensor()
])

for filename in os.listdir(input_folder):
    try:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img = cutout(img) # 이미지 전처리 및 augmentation 적용

        output_path = os.path.join(output_folder, f'Cutout_{filename}') # 저장할 경로 지정

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(output_path)

    except Exception as e:
        print(f'cutout_{filename} 저장 실패: {e}')

# Exposure ------------------------------------------------------------------------------------
Exposure = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ColorJitter(contrast=(0.5, 2.5),
                           ),
    transforms.ToTensor()
])

for filename in os.listdir(input_folder):
    try:
        # 이미지 열기
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img = Exposure(img) # 이미지 전처리 및 augmentation 적용

        output_path = os.path.join(output_folder, f'Exposure_{filename}') # 저장할 경로 지정

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(output_path)

    except Exception as e:
        print(f'Exposure_{filename} 저장 실패: {e}')

### Noise -------------------------------------------------------------------------------------
class AddGaussianNoise:
    def __init__(self, mean=0, std=0.1):
        self.mean = mean
        self.std = std

    def __call__(self, img):
        np_img = np.array(img)
        h, w, c = np_img.shape
        noise = np.random.normal(self.mean, self.std, (h, w, c))
        noisy_img = np.clip(np_img + noise * 255, 0, 255).astype(np.uint8)
        return Image.fromarray(noisy_img)

Noise = transforms.Compose([
    transforms.Resize((224, 224)),              
    AddGaussianNoise(mean=0, std=0.2),
    transforms.ToTensor()
])

for filename in os.listdir(input_folder):
    try:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img = Noise(img) # 이미지 전처리 및 augmentation 적용

        output_path = os.path.join(output_folder, f'Noise_{filename}') # 저장할 경로 지정

        img_pil = transforms.ToPILImage()(img)
        img_pil.save(output_path)

    except Exception as e:
        print(f'Noise_{filename} 저장 실패: {e}')

# - 전처리 파일 총 개수 확인 코드

# +
source_folder = 'final_data/train/images_pre'

# 폴더 내 파일 수 세기
file_count = sum(len(files) for _, _, files in os.walk(source_folder))

print(f"폴더 '{source_folder}'에는 총 {file_count}개의 파일이 있습니다.")
# -

# - argument한 파일들 iamges_pre > images 로 옮기기

# +
source_folder = 'final_data/train/images_pre'
destination_folder = 'final_data/train/images'

# source_folder의 파일을 destination_folder로 이동
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        shutil.move(file_path, destination_folder)


# +
import os

folder_path = 'final_data/train/images'

# 폴더 내 파일 중 이미지 파일이 아닌 것은 삭제
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if not any(file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.bmp']):
            os.remove(file_path)
            print(f"'{file_path}' 파일을 삭제했습니다.")
# -


