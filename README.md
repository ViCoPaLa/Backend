### 사용법

이 프로젝트는 Python 3.10.11 버전에서 작동합니다.

1. 프로젝트 디렉토리로 이동한다.
```bash
cd app
```

2. 가상 환경을 설치한다.
```bash
python -m venv venv
```

3. 가상 환경을 활성화한다
- Windows
  ```bash
  venv/Scripts/activate
  ```
- macOS 및 Linux
  ```bash
  source venv/bin/activate
  ```
  
4. 프로젝트에 필요한 종속성을 설치한다.
   ```bash
   pip install -r requirements.txt --use-pep517
   ```

5. .env 파일을 'app'폴더로 이동한다.
   .env 파일은 mjkweon17로부터 받으면 됨

6. 아래 명령어를 입력하여 FastAPI 서버를 실행함
   ```bash
   uvicorn main:app --reload
   ```
   서버가 성공적으로 실행되면 브라우저에서 http://localhost:8000 또는 적절한 호스트 및 포트로 접속하여 FastAPI 애플리케이션을 사용할 수 있습니다.

