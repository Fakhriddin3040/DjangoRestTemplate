declare var google: any;

import { Component, OnInit, inject, PLATFORM_ID } from '@angular/core';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';

import { Router } from '@angular/router'; // Импортируем Router из Angular
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, MatFormFieldModule, MatInputModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent implements OnInit {
  // Используем новую функцию inject для инъекции зависимостей
  private platformId = inject(PLATFORM_ID);
  private router = inject(Router); // Используем Angular Router

  ngOnInit(): void {
    // Проверяем, работает ли приложение в браузере
    if (isPlatformBrowser(this.platformId)) {
      this.loadGoogleScript().then(() => {
        google.accounts.id.initialize({
          client_id:
            '409809896736-fckja2ujg9itegt7r06k2itrt409472a.apps.googleusercontent.com',
          callback: (response: any) => {
            this.handlelogin(response);
            return false; // Останавливаем обработку дальнейших событий
          },
        });

        google.accounts.id.renderButton(
          document.getElementById('googleSignInButton'),
          { theme: 'outline', size: 'large' }
        );
      });
    }
  }

  loadGoogleScript(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (typeof google !== 'undefined') {
        resolve();
      } else {
        const script = document.createElement('script');
        script.src = 'https://accounts.google.com/gsi/client';
        script.async = true;
        script.defer = true;
        script.onload = () => resolve();
        script.onerror = (error) => {
          console.error('Error loading Google script:', error);
          reject(error);
        };
        document.body.appendChild(script);
      }
    });
  }
  private decoderToken(token: string) {
    return JSON.parse(atob(token.split('.')[1]));
  }

  handlelogin(response: any) {
    if (response) {
      try {
        console.log('Google login response:', response);
        const payload = this.decoderToken(response.credential);
        if (isPlatformBrowser(this.platformId)) {
          sessionStorage.setItem(
            'loggedInUser',
            JSON.stringify({
              name: payload.name,
              email: payload.email,
              picture: payload.picture, 
            })
          );
        }
        
      } catch (error) {
        console.error('Error handling login response:', error);
      }
    }
  }
}
