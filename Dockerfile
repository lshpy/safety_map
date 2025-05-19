FROM python:3.10-slim

# 작업 디렉토리
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 프로젝트 복사
COPY . .

# 포트 설정
EXPOSE 7860

# Streamlit 앱 실행
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
