# 🧃 시각장애인을 위한 음료 객체 인식 및 점자 변환
<br><br>

## 프로젝트 배경 및 목적
현재 음료 제품에 대한 점자 표기는 시각장애인들이 음료를 정확하게 구별하는 데 어려움을 겪고 있다. 기존 점자 표기는 제품명이 아닌 카테고리명만 포함되어 있어 불편함이 크고, 가독성이나 표기 위치에 대한 불만도 많다. 본 프로젝트는 딥러닝 객체 인식 기술과 점자 변환 기술을 활용해 시각장애인이 음료를 독립적으로 선택하고 구매할 수 있도록 돕는 시스템을 개발하여, 배리어 프리 환경을 실현하는 것을 목표로 한다.
<br><br>
## 주최/주관 및 팀원
- 국민대학교 AI빅데이터융합경영학과 딥러닝 수업 프로젝트
- 전공생 4명
<br><br>
## 프로젝트 기간
2023.09 ~ 2023.12 (3개월)
<br><br>
## 프로젝트 소개
### 1. 선행연구 분석
<img width="400" alt="스크린샷 2024-11-27 23 46 53" src="https://github.com/user-attachments/assets/02c73eb3-71c9-47e7-9f3e-aa96ea1db41c">
<img width="400" src="https://github.com/user-attachments/assets/1e20cf20-9974-4120-bd06-a8fef2cfce62">

### 2. 시나리오 설계
<img width="400" src="https://github.com/user-attachments/assets/12c737d1-083d-4971-8c05-0ddac537d490">
<img width="400" src="https://github.com/user-attachments/assets/371dfc13-a692-419a-aaf8-a05ed0956460">

### 3. 이미지 데이터 전처리
<img width="400" src="https://github.com/user-attachments/assets/15d2e797-65a3-403a-b754-07bdc488a56d">
<img width="400" src="https://github.com/user-attachments/assets/62177dec-1569-4cc0-b24c-1a2adde6306b">
<img width="400" src="https://github.com/user-attachments/assets/f158f765-a239-46a5-91ef-0efbbcccbe5b">
<img width="400" src="https://github.com/user-attachments/assets/f02ea311-f0da-41c4-9e7d-0f7bec43d26e">

### 4. 라벨 데이터 변환
<img width="400" src="https://github.com/user-attachments/assets/d03f1610-3dae-40c9-bae4-ef9ed9fa178f">

### 5. Yolov5 모델 전이학습 후 평가
<img width="400" src="https://github.com/user-attachments/assets/017f5540-9e13-49ca-be00-1864a5ee71de">
<img width="400" src="https://github.com/user-attachments/assets/da65dec1-5af5-4f24-bc4b-fb76baaa9ace">

### 6. 점자 변환
<img width="400" src="https://github.com/user-attachments/assets/d499dd57-900e-4b7e-acdb-87de1b4880e3">

[*중간발표 자료](https://github.com/suin420/Deep_Learning_project/blob/main/doc/%EB%94%A5%EB%9F%AC%EB%8B%9D_%EC%A4%91%EA%B0%84%EB%B0%9C%ED%91%9C.pdf)<br>
[*최종발표 자료](https://github.com/suin420/Deep_Learning_project/blob/main/doc/%EB%94%A5%EB%9F%AC%EB%8B%9D_%EC%B5%9C%EC%A2%85%EB%B0%9C%ED%91%9C.pdf)
<br><br>
## 프로세스
### 
### [*code tutorial](https://github.com/suin420/Deep_Learning_project/blob/main/doc/code_tutorial.ipynb)
<img width="400" src="https://github.com/user-attachments/assets/d7d60abe-2f4c-426f-bec0-4050e7b29918">

<br><br>
## 담당 역할
- 시나리오 설계 및 모델링 정의
- 데이터 augmentation&resize
- txt 파일(라벨 데이터) yolo 입력에 맞게 변환
- 점자 모듈 생성 및 모델 츌력과 연동
- 전체 프로세스 정리

<br><br>
## 기여 및 한계점
- 시각장애인을 위한 점자워치를 활용함으로써, 시끄러운 장소나 공공장소와 같은 환경에서도 음료를 스스로 구분할 수 있는 기회를 제공할 수 있다.

- 더 다양한 음료와, 이후 새로 출시될 음료까지 이미지와 라벨 파일 데이터만 존재한다면 큰 어려움 없이 해당 프로세스를 적용 가능하다.

- 팀원 모두 객체 인식 분야를 처음 접해보아서 기획 당시 고려한 다양한 모델들을 실제로 구현하고 결과를 비교하는 과정을 충분히 수행하지 못하였다. 이에 선행 연구 사례가 많은 YOLO 모델을 선택하게 되었다.

- 컴퓨팅 자원의 부족으로 더 많은 음료 클래스를 학습시키지 못한 점도 아쉬운 부분으로 꼽힌다. 이로 인해 더 넓은 범위의 음료를 인식하는 모델을 구축하는 것이 제한됐다.
