# CyIVAChess
전세계적으로 가장 강력하다고 평가받는 stockfish를 상대로 강화학습을 이용해 인공지능 모델을 개발 및 학습




# 실행 환경 구성하기
## 라이브러리 install


텐서플로우 및 가상환경을 구성
텐서 플로우 2.10

conda create -n <가상환경 이름> python=3.10
conda activate <가상환경 이름>

cudnn - 8.1 -> 여러 버전이 같이 있으니 주의!
https://developer.nvidia.com/rdp/cudnn-archive#a-collapse81-112

cuda - 11.2
https://developer.nvidia.com/cuda-11.2.2-download-archive

pip install tensorflow==2.10


체스 기본 룰을 제공
pip install chess

GUI를 구성하기 위한 라이브러리
pip install pygame