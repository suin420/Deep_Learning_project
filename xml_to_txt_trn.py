import xml.etree.ElementTree as ET
import os

class XmlToTxtTrnClass:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = ET.parse(file_path)
        self.root = None
        self.parse_file(file_path)

    def parse_file(self, file_path):
        tree = ET.parse(file_path)
        self.root = tree.getroot() # root element 가져오기 
    
    def label_encoding(self, label):
        mapping = {
            '코카콜라)코카콜라350ML': 0,
            '몬스터에너지울트라355ML': 4,
            '롯데레쓰비마일드커피200ml': 2,
            '농심웰치스포도355ml': 5,
            '코카환타오렌지250ML': 1,
            '롯데밀키스340ML': 3,
            '동아데미소다애플250ML': 6,
            '롯데칠성사이다190ML': 7,
            '해태포도봉봉340ML': 8,
            '동아데자와240ML': 9
        }
        mapped_label = mapping.get(label)
        if mapped_label is None:
            print(f"Label '{label}' has no matching encoding in the mapping dictionary.")
        return mapped_label



    def toTxt(self): 
        objects = self.root.findall('.//object') # 모든 object 엘리먼트를 찾기
        txt_line = "" # 텍스트 파일로 저장할 문자열 초기화

        # 바운딩 박스 좌표 출력
        for obj in objects:
            # 0~1 사이 값으로 정규화 
            xmin = int(obj.find('bndbox/xmin').text) / 2988 
            ymin = int(obj.find('bndbox/ymin').text) / 2988 
            xmax = int(obj.find('bndbox/xmax').text) / 2988 
            ymax = int(obj.find('bndbox/ymax').text) / 2988 

            # 모서리 좌표에서 센터 좌표로 반환 
            x = (xmax + xmin)/2
            y = (ymax + ymin)/2

            # width, height 구하기 
            width = abs(xmax - xmin)
            height = abs(ymax - ymin)

            # 라벨 지정 
            label = obj.find("name").text
            label = self.label_encoding(label)

            # <object-class> <x> <y> <width> <height>
            txt_line += f"{label} {x} {y} {width} {height}\n"
            
        name = self.root.find(".//filename").text # "filename" 엘리먼트 내의 파일 이름 추출
        name = name.replace(".jpg", ".txt")
                
        filename = self.file_path.split('/')
        filename = filename[-2]
        output_dir = os.path.join('final_data/train/labels', filename) # 저장할 디렉토리 경로 설정
        os.makedirs(output_dir, exist_ok=True)

        # 파일 경로 생성
        output_path = os.path.join(output_dir, name)

        # 텍스트 파일에 저장
        with open(output_path, 'w') as txt_file:
            txt_file.write(txt_line)


