import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './layout/header/header.component';
import { MainComponent } from "./layout/main/main.component";
import { FooterComponent } from "./layout/footer/footer.component";
import { LoginComponent } from "./auth/login/login.component";


import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common'; // Импортируйте CommonModule
import { RegisterComponent } from './auth/register/register.component';
import { BreadcrumbNavigationComponent } from "./shared/components/breadcrumb-navigation/breadcrumb-navigation.component";
import { ContainerComponent } from "./shared/container/container.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HeaderComponent,
    MainComponent,
    FooterComponent,
    LoginComponent,
    CommonModule,
    RegisterComponent,
    BreadcrumbNavigationComponent,
    ContainerComponent
],
    
  templateUrl: './app.component.html',  
  styleUrls: ['./app.component.scss'],   
})
export class AppComponent {
  title = 'marketplace-client';
  showMain: boolean = true; 

  // Функция для переключения на логин
  navigateToLogin() {    
    this.showMain = false;
  }

  navigateToRegister(): void {
    this.showMain = false; // Переходим к компоненту Register
  }
}
