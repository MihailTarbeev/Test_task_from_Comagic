# Test_task_from_Comagic
Это серия заданий над проектом от компании "CoMagic", которую я выполнил за время стажировки
<h1>Привет!</h1>

[Первое задание](#первое-задание) <br>
[Второе задание](#второе-задание) <br>
[Третье задание](#третье-задание) <br>
[Четвёртое задание](#четвёртое-задание) <br>
[Пятое задание](#пятое-задание) <br>

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
<p>Создание сервиса, который способен взаимодействовать с гугл диском.</p>
<p>А именно: <b>загружать файлы на диск</b> и <b>получать список файлов на диске</b>.</p>
<p>Для работы с Google Drive API необходимо пройти аутентификацию с помощью протокола OAuth 2.0.</p>
<p>Входными данными для работы с нашим сервисом будут:</p>
<ul>
  <li>client_id</li>
  <li>client _secret</li>
  <li>refresh_token</li>
  <li>Загружаемый файл</li>
</ul>

<p>Чтобы узнать client_id и client_secret нужно настроить проект в Google API Console. В Credentials находим наши данные.</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/fe9bf3cc-e787-4068-8c7e-85bb0b48b3fc)

<p>Чтобы получить refresh_token нужно:</p>
<p>1) Отправить GET запрос на аутентификацию в Google по url https://accounts.google.com/o/oauth2/v2/auth со следующими параметрами:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/5985c357-4b6e-4304-9dfe-0b4cf7a04c0e)

<p>Ответ включает параметр code , одноразовый код авторизации, который нам понадобится.</p>
<p>2) Отправляем POST запрос по url https://oauth2.googleapis.com/token со следующими параметрами:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/e193e10e-bd24-4f7a-91e0-df545347d62a)

<p>В ответе находим refresh_token.</p>
<p>Загружаемый файл создаётся при помощь сервиса File Server.</p>

<p>Вся структура наших "кубиков" выглядит следующим образом:</p>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/e4a38069-b86a-4aaa-a36c-9824cc9eafb2)

<ul>
<li>Создаём наш файл.</li><br>
  
  ![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/2535001d-0ec4-4f99-9e15-176e653dbca8)

<li>Получаем access_token.</li><br>

  ![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/104098bc-d925-4924-a7f8-aed1a921f0e3)

<li>Загружаем наш файл.</li><br>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/ebf113be-a2b6-4a76-b887-088681da490f)

<li>Получаем список файлов, находящихся на гугл диске.</li><br>

![image](https://github.com/MihailTarbeev/Test_task_from_Comagic/assets/132607365/5061c2fd-ff7e-42d0-9d72-1b3e7056f533)

</ul>
