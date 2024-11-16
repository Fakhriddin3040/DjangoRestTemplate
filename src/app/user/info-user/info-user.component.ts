import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common'; // Для директив вроде *ngIf
import { AuthService } from '../../core/services/auth.service'; // Импорт AuthService

@Component({
  selector: 'app-info-user',
  standalone: true,
  imports: [CommonModule], // Импортируем CommonModule для использования *ngIf, *ngFor
  templateUrl: './info-user.component.html',
  styleUrl: './info-user.component.scss'
})
export class InfoUserComponent implements OnInit {
  user: any;  // Объект пользователя

  constructor(private authService: AuthService) {}

  auth = inject(AuthService); // Внедрение сервиса с помощью inject

  ngOnInit(): void {
    // Получаем данные пользователя из AuthService
    this.user = this.authService.getLoggedInUser();
    console.log(this.user);  // Проверяем, что данные пользователя получены
  }

  logout(): void {
    this.auth.logout(); // Вызов метода logout
  }
}
