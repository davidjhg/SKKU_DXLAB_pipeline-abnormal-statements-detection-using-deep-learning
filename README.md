# SKKU_DXLAB_pipeline-abnormal-statements-detection-using-deep-learning

<img src="result.PNG">

# 1. 프로젝트 개요 
국내 열수송관은 1980년대 자원 이용 효율 증가를 위해 실시된 에너지 사업 이후 전국 각지에 산재되어 있으나, 최근 매설되어 있는 열수송관의 노후화로 인한 파열 사고가 빈번히 발생하고 있음  
기존 인력의 부족과 검사 기술의 한계로 이를 상당 부분 개선 할 수 있는 인공지능 기반의 접근법이 필요  
본 프로젝트에서는 열화상 영상 기반의 딥러닝 접근법을 통하여 열수송관이 파열로 인한 온수 누출 탐지 방법을 개발함 

# 2. 열화상 데이터 
지역난방공사는 열화상 카메라와 유사 발열체 탐지를 위한 일반 영상 카메라가 장비된 드론을 사용하여 열수송관의 파열로 인한 위험 의심 지역 검진을 수행함  
해당 데이터를 기반으로 위험 의심 지역 추출을 위하여 전용 레이블링 툴을 구현하여 사용  
```python
python labeling_tool.py
```

# 3. 영상 분할 모델 
일반 영상과 열화상 영상을 입력 받아 위험 의심 지역 위치 정보를 반환 하도록 딥러닝 모델 구축
해당 모델은 Residual Block 기반의 두 Encoder와 단일 Decoder 로 구성되며 Skip Connection 구조 포함  

# 4. Environment
python  
pytorch  
opencv  
PIL  
torchvision  
scikit-learn  

