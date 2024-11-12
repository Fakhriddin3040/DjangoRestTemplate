import express from 'express';
import fetch from 'node-fetch';
import cors from 'cors'; 

const app = express();
const PORT = 3000;

// Включаем CORS для всех маршрутов
app.use(cors());

app.get('/proxy', async (req, res) => {
  try {
    const response = await fetch('https://api.moysklad.ru/api/remap/1.2/entity/assortment?groupBy=consignment&limit=10', {
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
    console.log('Полученные данные от API:', data);

    const assortmentData = data.rows || [];
    const limitedData = assortmentData.slice(0, 10); // Ограничиваем до 10 объектов

    // Собираем все URL-адреса для групп из поля href в каждом объекте
    const urlsGroupProduct = limitedData.map(item => item.group?.meta?.href).filter(Boolean);

    // Выполняем параллельные запросы по каждому URL для групп
    const detailsPromises = urlsGroupProduct.map(url =>
      fetch(url, {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer 9903b4458420aa193f41d12c6c7205f8324a4f0f',
          'Accept-Encoding': 'gzip'
        }
      }).then(response => response.json())
    );

    // Ждём завершения всех запросов для групп
    const details = await Promise.all(detailsPromises);

    // Привязываем полученные данные для групп к исходным объектам
    const enrichedData = limitedData.map((item, index) => ({
      ...item,
      groupDetails: details[index]
    }));

    // Собираем все URL-адреса для изображений из поля images
    const urlsImgProduct = enrichedData.map(item => item.images?.meta?.href).filter(Boolean);

    // Выполняем параллельные запросы по каждому URL для изображений (ограничиваем до 10)
    const detailsPromisesImg = urlsImgProduct.slice(0, 10).map(url =>
      fetch(url, {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer 9903b4458420aa193f41d12c6c7205f8324a4f0f',
          'Accept-Encoding': 'gzip'
        }
      }).then(response => response.json())
    );

    // Ждём завершения всех запросов для изображений
    const imagesDetails = await Promise.all(detailsPromisesImg);

    // Привязываем данные изображений и загружаем каждое изображение
    const finalData = await Promise.all(enrichedData.map(async (item, index) => {
      const imageHref = imagesDetails[index]?.rows[0]?.miniature?.href || null;
      
      console.log("imageHref: ",imageHref);
      if (imageHref) {
        const imageResponse = await fetch(imageHref, {
          method: 'GET',
          headers: {
            'Authorization': 'Bearer 9903b4458420aa193f41d12c6c7205f8324a4f0f',
            'Accept-Encoding': 'gzip'
          }
        });

        if (imageResponse.ok) {
          const imageData = await imageResponse.arrayBuffer();
          return {
            ...item,
            // imageBuffer: 'data:image/png;base64,' + Buffer.from(imageData).toString('base64') // Конвертируем изображение в Base64
           imageBuffer: Buffer.from(imageData) // Конвертируем изображение в Base64

          };
        } else {
          console.warn(`Не удалось загрузить изображение для ${imageHref}`);
          return { ...item, imageBuffer: null };
        }
      } else {
        return { ...item, imageBuffer: null };
      }
    }));

    // Отправляем ответ с обогащенными данными и изображениями в формате Base64
    res.json(finalData);
  } catch (error) {
    console.error('Ошибка при запросе к платформе "Мой Склад"', error);
    res.status(500).json({ error: 'Ошибка при запросе к платформе "Мой Склад"' });
  }
});

app.listen(PORT, () => {
  console.log(`Прокси-сервер запущен на http://localhost:${PORT}`);
});
