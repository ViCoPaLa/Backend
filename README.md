이 프로젝트는 Python 3.10.11 버전에서 작동합니다.

프로젝트 디렉토리로 이동합니다.

bash
Copy code
cd app
가상 환경 (virtual environment)을 설치합니다.

bash
Copy code
python -m venv venv
가상 환경을 활성화합니다.

Windows:

bash
Copy code
venv\Scripts\activate
macOS 및 Linux:

bash
Copy code
source venv/bin/activate
프로젝트에 필요한 종속성을 설치합니다.

bash
Copy code
pip install -r requirements.txt --use-pep517
.env 파일을 app 폴더로 이동시킵니다.

FastAPI 서버를 실행합니다. 개발 모드에서는 코드 변경이 감지되면 자동으로 다시 로드됩니다.

bash
Copy code
uvicorn main:app --reload
서버가 성공적으로 실행되면 브라우저에서 http://localhost:8000 또는 적절한 호스트 및 포트로 접속하여 FastAPI 애플리케이션을 사용할 수 있습니다.

참고: 실제로 프로젝트를 클론한 후 위의 단계를 따르면 FastAPI 서버를 로컬 환경에서 실행할 수 있습니다.