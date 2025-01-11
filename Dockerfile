FROM python:3.9.21-alpine3.21
WORKDIR /myapp
COPY ./tictactoe.py .
CMD ["python3","tictactoe.py"]
