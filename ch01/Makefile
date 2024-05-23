install:
	..\practical-mlops\Scripts\python.exe -m pip install --upgrade pip && \
		..\practical-mlops\Scripts\python.exe -m pip install -r requirements.txt

lint:
	..\practical-mlops\Scripts\pylint --disable=R,C hello.py

test:
	python -m pytest -vv --cov=hello test_hello.py