FROM python:3.8-alpine
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

# Build the image
# sudo docker image build -t bavodenys/flask .
# To run the image
# sudo docker run -p 5000:5000 bavodenys/flask
# Access in internet browser: localhost:5000
