FROM python:3.9

LABEL maintainer="csm66865407@gmail.com"
LABEL version="1.0.0"
LABEL description="Service for crafting readme"

# 이미지 내부의 작업 디렉토리를 /usr/src/app로 설정 (bash가 입력될 곳)
WORKDIR /usr/src/app

# 현재 디렉토리의 모든 파일과 폴더를 이미지의 현재 작업 디렉토리 "/usr/src/app"로 복사
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]