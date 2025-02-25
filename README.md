# task-manager

### Клонируем репозиторий**
```sh
git clone git@github.com:KiselevVv/task-manager.git
```

### **2. Создаем файл .env**
```sh
DATABASE_URL=sqlite+aiosqlite:///./mydb.db
```

### **3. Собираем и запускаем контейнер**
```sh
docker-compose up --build
```
После успешного запуска API будет доступно по адресу:  
**http://localhost:8000/docs**