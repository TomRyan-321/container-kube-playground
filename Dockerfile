FROM python:3.12.11
WORKDIR /app
COPY src .
RUN pip3 install -r requirements.txt
# Garbage secret keys for secret scan testing
ENV AWS_ACCESS_KEY_ID="AKIATESTTESTTESTTEST"
ENV AWS_SECRET_ACCESS_KEY="abcdefghijklmnopqrstuvwxyz1234567890ABCD"
USER 1234
ENTRYPOINT ["python"]
CMD ["app.py"]
