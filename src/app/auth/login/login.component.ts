declare var google: any;
import {
  Component,
  ViewChild,
  TemplateRef,
  AfterViewInit,
  OnInit,
  inject,
  PLATFORM_ID,  
  
} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { isPlatformBrowser } from '@angular/common';
import { AuthService } from '../../core/services/auth.service';
import { TranslateModule, TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [TranslateModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements AfterViewInit, OnInit {

  private platformId = inject(PLATFORM_ID);
  

  @ViewChild('content') content!: TemplateRef<any>;

  constructor(
    private modalService: NgbModal, 
    private authService: AuthService,
    private translate: TranslateService
  ) 
    {
      this.translate.setDefaultLang('ru');
    }

  ngAfterViewInit() {
    // Проверка, что шаблон инициализирован
    if (this.content) {
      console.log('Template initialized:', this.content);
    } else {
      console.log('Template not found');
    }
  }

  navigateToLogin() {
    console.log('navigateToLogin method called');
    if (this.content) {
      const modalRef = this.modalService.open(this.content, { centered: true });

      modalRef.result.then(
        () => {},
        () => {
          console.log('Modal closed');
        }
      );

      // Рендерим кнопку Google после полной инициализации модального окна
      modalRef.shown.subscribe(() => {
        setTimeout(() => this.renderGoogleButton(), 0); // Ожидаем рендер модального окна
      });
    } else {
      console.log('Template not found');
    }
  }

  renderGoogleButton() {
    if (isPlatformBrowser(this.platformId)) {
      this.loadGoogleScript().then(() => {
        google.accounts.id.initialize({
          client_id: '409809896736-fckja2ujg9itegt7r06k2itrt409472a.apps.googleusercontent.com',
          callback: (response: any) => {
            this.handlelogin(response); // Обработка логина
            return false;
          },
        });

        google.accounts.id.renderButton(
          document.getElementById('googleSignInButtonModal'), // Убедитесь, что ID совпадает с элементом в шаблоне
          { theme: 'outline', size: 'large' }
        );
      });
    }
  }

  ngOnInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.loadGoogleScript();
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
        const payload = this.decoderToken(response.credential);
        if (isPlatformBrowser(this.platformId)) {
          // Используем AuthService для обновления состояния
          this.authService.setLoggedInUser({
            name: payload.name,
            email: payload.email,
            picture: payload.picture,
          }, response.credential);
        }
      } catch (error) {
        console.error('Error handling login response:', error);
      }
    }
  }
}