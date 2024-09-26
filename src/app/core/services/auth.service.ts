declare var google: any;
import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // Хранение состояния авторизации пользователя
  private isLoggedInSubject = new BehaviorSubject<boolean>(this.isAuthenticated());
  isLoggedIn$ = this.isLoggedInSubject.asObservable();

  constructor(private router: Router, @Inject(PLATFORM_ID) private platformId: Object) {}

  // Метод для выхода
  logout(): void {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('loggedInUser');
    this.isLoggedInSubject.next(false);  // Обновляем состояние на "неавторизован"
    this.router.navigate(['/login']);
  }

  // Метод для проверки аутентификации
  isAuthenticated(): boolean {
    return isPlatformBrowser(this.platformId) && !!sessionStorage.getItem('token');
  }

  // Метод для установки авторизованного пользователя
  setLoggedInUser(userData: any, token: string): void {
    if (isPlatformBrowser(this.platformId)) {
      sessionStorage.setItem('loggedInUser', JSON.stringify(userData));
      sessionStorage.setItem('token', token);  // Сохраняем токен
      this.isLoggedInSubject.next(true);  // Обновляем состояние на "авторизован"
    }
  }

  // Получение данных о текущем пользователе
  getLoggedInUser(): any {
    if (isPlatformBrowser(this.platformId)) {
      const user = sessionStorage.getItem('loggedInUser');
      return user ? JSON.parse(user) : null;
    }
    return null; // Возвращаем null, если не в браузере
  }

  // Декодирование токена (JWT)
  private decodeToken(token: string): any {
    return JSON.parse(atob(token.split('.')[1]));
  }
}