import { Component, EventEmitter, Output, ViewChild, AfterViewInit, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { ContainerComponent } from '../../shared/container/container.component';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Router } from '@angular/router';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap'; // Подключение NgbModal
import { LoginComponent } from '../../auth/login/login.component';
import { InfoUserComponent } from "../../user/info-user/info-user.component"; // Импорт компонента входа
import { CommonModule } from '@angular/common'; // Импорт CommonModule

import { AuthService } from '../../core/services/auth.service';
import { Section1BannerComponent } from "./header-section1-banner/header-section1-banner.component"; 

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    MatButtonModule,
    MatMenuModule,
    MatIconModule,
    ContainerComponent,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    LoginComponent,
    InfoUserComponent,
    CommonModule // Добавляем CommonModule сюда
    ,
    Section1BannerComponent
],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  
  imageUrl = 'assets/images/promo/promo1.png';
  imageUrl2 = 'assets/images/promo/promo2.png';
  selected = 'option2';

  @ViewChild('loginModal') loginModal: any;
  @Output() loginClick = new EventEmitter<void>();

   constructor(
    private modalService: NgbModal, 
    private router: Router,
    private authService: AuthService // исправление ошибки, добавив модификатор private
    ) {}  

  navigateToLogin() {
    console.log('navigateToLogin method called');
    const loginComponent = document.getElementById('content');
    if (loginComponent) {
      this.modalService.open(loginComponent, { centered: true });
    }
  }

  isUserLoggedIn = false;

  ngOnInit(): void {
    // Подписываемся на изменения состояния авторизации
    this.authService.isLoggedIn$.subscribe((loggedIn) => {
      this.isUserLoggedIn = loggedIn;
    });
  }
}