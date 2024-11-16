import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

// Создание функции authGuard с проверкой авторизации
export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router); // Используем DI для получения Router

  // Получаем данные о текущем пользователе из sessionStorage
  const user = sessionStorage.getItem('loggedInUser');

  // Если пользователь не найден, перенаправляем на страницу входа
  if (!user) {
    router.navigate(['/login']); // Путь к вашей странице входа
    return false; // Запретить доступ к защищенному маршруту
  }

  return true; // Разрешить доступ к защищенному маршруту
};

