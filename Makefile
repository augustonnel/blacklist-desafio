install:
	pip install -r requirements.txt

build:
	docker build -t app .

run:
	docker run -p 5000:5000 app