import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedInSubject = new BehaviorSubject<boolean>(this.isAuthenticated());
  isLoggedIn$ = this.isLoggedInSubject.asObservable();

  constructor(private router: Router, @Inject(PLATFORM_ID) private platformId: Object) {}

  logout(): void {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('loggedInUser');
    this.isLoggedInSubject.next(false);
    this.router.navigate(['/login']);
  }

  isAuthenticated(): boolean {
    return isPlatformBrowser(this.platformId) && !!sessionStorage.getItem('token');
  }

  setLoggedInUser(userData: any, token: string): void {
    if (isPlatformBrowser(this.platformId)) {
      sessionStorage.setItem('loggedInUser', JSON.stringify(userData));
      sessionStorage.setItem('token', token);
      this.isLoggedInSubject.next(true);
    }
  }

  getLoggedInUser(): any {
    if (isPlatformBrowser(this.platformId)) {
      const user = sessionStorage.getItem('loggedInUser');
      return user ? JSON.parse(user) : null;
    }
    return null;
  }

  private decodeToken(token: string): any {
    return JSON.parse(atob(token.split('.')[1]));
  }
}