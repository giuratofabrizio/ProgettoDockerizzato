FROM nikolaik/python-nodejs

WORKDIR /app 
RUN npm install -g nodemon

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["nodemon", "./app.py"]