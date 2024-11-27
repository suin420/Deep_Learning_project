# 🧃 시각장애인을 위한 음료 객체 인식 및 점자 변환
<br><br>
## 프로젝트 배경 및 목적

## 주최/주관 및 팀원

## 프로젝트 기간

## 프로젝트 소개

## 프로세스
### code tutorial
<img src="https://github.com/user-attachments/assets/d7d60abe-2f4c-426f-bec0-4050e7b29918" width="600" />

#### 01. txt conversion
- txt_main.py
  - hub_data의 label(.xml)을 txt로 변경하여 final_data에 저장
  - hub_data의 image(.jpg)를 final_data로 복사
  - robo_data의 image, label을 final_data로 동일하게 복사
    
    - final_data/train/images : 1740개  
      final_data/train/labels : 1740개  
      final_data/valid/images : 210개  
      final_data/valid/labels : 210개  

#### 02. Augmentation
     
(1) Image Augmentation
- train_argu_collect.py & valid_argu_collect.py
  - 이미지 5종류의 augmentation 후 images_pre에 저장
  - images_pre의 이미지들을 train/valid에 각각 images로 이동 (원본 + augmentation)

    - final_data/train/images : 10440개  
      final_data/train/labels : 1740개  
      final_data/valid/images : 1260개  
      final_data/valid/labels : 210개

(2) Label Increase
- label_argu_train.py & label_argu_valid.py
  - 원본 labels를 augmentation한 images와 같은 이름으로 labels_pre에 저장
  - labels_pre의 라벨들을 train/valid에 각각 labels로 이동 (원본*6)

    - final_data/train/images : 10440개  
      final_data/train/labels : 10440개  
      final_data/valid/images : 1260개  
      final_data/valid/labels : 1260개

#### 03. Modeling & Braille Translation
- yolo/yolov5/model_train.ipnyb
  - yolo 모델 학습 및 test 이미지로 테스트 후 test에서 예측한 클래스 이름 추출
  - 추출한 클래스 이름을 점자로 변환

## 역할

## 배우고 느낀 점
