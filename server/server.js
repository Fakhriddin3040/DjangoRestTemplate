import express from 'express';
import fetch from 'node-fetch';
import cors from 'cors'; 

const app = express();
const PORT = 3000;

// Включаем CORS для всех маршрутов
app.use(cors());

app.get('/proxy', async (req, res) => {
  try {
    const response = await fetch('https://api.moysklad.ru/api/remap/1.2/entity/assortment?groupBy=consignment', {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer 9903b4458420aa193f41d12c6c7205f8324a4f0f',
        'Accept-Encoding': 'gzip'
      }
    });

    if (!response.ok) {
      throw new Error(`Ошибка запроса: ${response.status}`);
    }

    const data = await response.json();
    res.json(data);
  } catch (error) {
    console.error('Ошибка при запросе к платформе "Мой Склад"', error);
    res.status(500).json({ error: 'Ошибка при запросе к платформе "Мой Склад"' });
  }
});

app.listen(PORT, () => {
  console.log(`Прокси-сервер запущен на http://localhost:${PORT}`);
});
