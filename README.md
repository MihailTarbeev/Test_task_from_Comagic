# Test_task_from_Comagic
Это серия заданий над проектом от компании "CoMagic", которую я выполнил за время стажировки
<h1>Привет!</h1>

[Первое задание](#первое-задание)
[Второе задание](#второе-задание)
[Третье задание](#третье-задание)
[Четвёртое задание](#четвёртое-задание)
[Пятое задание](#пятое-задание)

<h1>Первое задание</h1>
<p>Необходимо выполнить следующие пункты:</p>
<ul>
  <li>Клонировать данный репозиторий к себе на Git.</li>
  <li>Скопировать к себе на компьютер копию даного проекта.</li>
  <li>В файле node/service.py и node/config.yaml изменить с Example на необходимые названия.</li>
  <li>Запустите данный проект в VS Code, чтобы в Docker создался образ и контейнер.</li>
  <li>Найти текущий проект и его файлы в запущеном контейнере Docker.</li>
  <li>Сделать скриншот файлов которые нашли внутри контейнера и добавить в README.md.</li>
  <li>Запустить Ngrok htpp на порту 9000. Сделать его скриншот и добавить в README.md.</li>
</ul>
<p>Файлы, найденные внутри запущенного контейнера:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/8ca42a88-a546-48e8-8dac-66648e2655a9)

<p>Запущенный Ngrok htpp на порту 9000:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/1c6504de-4c41-4d2e-b4d5-a24eab707857)

<h1>Второе задание</h1>
<p>Необходимо создать три поля (текстовое поле, числовое поле и поле-переключатель).<br>В числовое и текстовое поля вводятся числа.<br>Сервис должен сложить эти числа и вернуть в виде типа данных, на который указывает поле-переключатель (Число или Текст).</p>
<p>Примеры работы сервиса:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/23852fa0-15cc-49b7-bc53-c4c6fd7602ee)

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/0c09b9a1-0dd6-4950-9f2f-1fa53aa368a7)

<h1>Третье задание</h1>
<p>Расширяем функциональность нашего сервиса.</p>
<p>Создадим дополнительное поле-переключатель "Включить поля", которое будет включать отображение двух полей с выпадающими списками из двух значений. Оба значения одинаковы в этих полях.</p>
<p>При одновременном выборе <b>Первого</b> значения в двух полях, появляется новое поле "Почта".<p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/acdc1577-4e43-402d-b4f6-fe44fbd8d42c)

<p>При одновременном выборе <b>Второго</b> значения в двух полях, появляется новое поле "Дата и время".

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/bba24b7d-295b-4cf8-b5f2-b0b8c9b233db)

<h1>Четвёртое задание</h1>
<p>Создание 2 сущностей нашего сервиса: Авторизации и Customer.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/2fd20510-ed9a-4235-92d6-b83ff4cb14d9)

<p>Пользователь в первом "кубике" вводит регистрационные данные от своей CRM./p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/92c82b21-16d8-4ff4-9d4a-b1d5b2d9aab1)

<p>Через соединение "кубиков" результат авторизации передаётся второму "кубику", отвечающему за получение данных о клиентах.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/46ddc445-ecab-42f9-b122-5e8d9b60f9e4)

<p>Созданы поля для выбора Ресурса, его методов и предустановленных фильтров.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/160e3ba9-68a8-4769-88dd-93badff610b4)

<p>На картинке выше в правой части можно наблюдать результат запроса у сущности Customer.</p>
<p>Данный проект выполнен с интеграцией сервиса AlfaCRM.</p>

<h1>Пятое задание</h1>
<p>Создаём сервис, который способен загружать файлы на гугл диск и получать список файлов.</p>
<p>Сервис состоит из четырёх "кубиков": Создание файла, Авторизация, Загрузка файла, Получение списка файлов.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/bc34b928-2038-444d-8a9e-c9641c09d044)

<p>Создаём наш тестовый файл.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/eedcabae-e887-488d-b96f-ff4dcf482847)

<p>Для авторизации нам понадобится JSON-файл с нашими приватными данными.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/c1f6fecc-c334-401f-979e-12de95574937)

<p>Вносим данные из этого JSON-файла в поле "Приватные данные".</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/b446fa3f-ea5d-4f49-9bfe-925926f111c1)

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/78895440-86ba-4c6a-8514-45ae157c68c9)

<p>После отработки этого кубика выскочит окно авторизации.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/ba11855d-a7b4-41c1-a75c-ac8900728704)

<p>Загружаем наш файл на сервер.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/8961763f-edfd-4b22-9593-6a202041a4ba)

<p>Получаем список находящихся на диске файлов:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/1850433e-19fa-482c-a6ef-df1d8d1e6efa)

