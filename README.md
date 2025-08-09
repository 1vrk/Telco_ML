# Telco_ML
# Прогнозирование оттока клиентов телеком-компании
## Описание: Прогнозирование оттока клиентов телеком-компании на основе исторических данных. Проект включает полный цикл: от анализа данных до построения ML-модели.
### Данные: Telco Customer Churn 
### Анализ данных: Pandas, SQL, NumPy 
### Визуализация: Matplotlib, Seaborn
### ML-инструменты (предстоящие): Scikit-learn (mb CatBoost)
### Работа с БД: SQLAlchemy, MySQL Connector
## Выполненная работа (EDA)
- Подключение к БД и выгрузка данных
- Анализ распределения клиентов
- Визуализация ключевых метрик:
  - Тепловые карты оттока
  - Групповые столбчатые диаграммы
  - Анализ влияния техподдержки, услуг, тип контракта и т.п.
- Базовые модели: логисическая регрессия, случайный лес
- Сравнение результатов данных моделей
- Топ признаков каждой модели
  
# Пример
## процент оттока между разными типами интернет-услуг
<img width="689" height="579" alt="image" src="https://github.com/user-attachments/assets/ffccec18-4296-4d50-b8b2-8c466ba1a5b0" />

## распределение клиентов по типам контрактов
<img width="574" height="668" alt="image" src="https://github.com/user-attachments/assets/0bf39c9c-30dc-47fb-9540-0a6b9a871cc2" />

## исследовать комбинацию типа контракта и интернет-услуг на отток
<img width="1043" height="849" alt="image" src="https://github.com/user-attachments/assets/e796c4a3-14bf-4b74-9b0d-d8f3fce28e6d" />

## oпределить комбинации факторов (контракт+услуги+оплата) с максимальным оттоком
<img width="1039" height="1154" alt="image" src="https://github.com/user-attachments/assets/c53e9642-239c-462f-a116-659efbfefe82" />


# ML часть
## Предобработка данных для ML
<img width="987" height="503" alt="image" src="https://github.com/user-attachments/assets/f8ae627f-6452-4fff-9a58-5080b8189090" />
<img width="180" height="50" alt="image" src="https://github.com/user-attachments/assets/62df82f2-fd6d-4da0-b108-f98a3ef3bbb6" />

## Построение и оценка моделей:
### Логистическая регрессия:
<img width="639" height="591" alt="image" src="https://github.com/user-attachments/assets/0ff7a944-2940-4435-affe-fc8512f259e3" />

### Случайный лес
<img width="631" height="603" alt="image" src="https://github.com/user-attachments/assets/aea87aac-6dbb-451f-8ad5-7674a1c9028a" />

### Сравнение результатов
<img width="874" height="620" alt="image" src="https://github.com/user-attachments/assets/2e6cd65c-f2a9-4b51-99d2-70affd8ec224" />

## Топ признаков моделей
### Случайный лес
<img width="981" height="640" alt="image" src="https://github.com/user-attachments/assets/e86f3f2e-b59a-4a77-80f4-ae77c1075edf" />

### Логистическая регрессия:
<img width="996" height="643" alt="image" src="https://github.com/user-attachments/assets/ffa32839-9a2f-428e-9848-acd8d2b552e6" />

# Как запустить
1. Установите зависимости:
```bash
python pip install -r requirements.txt

```
2. Запустите Jupyter Notebook:
```bash
jupyter lab
```

# Note
```bash
Возможна ошибка с сохранением (plt.savefig) проверьте путь сохранения и также другие пути, например csv, спасибо!
```
