import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { InfoUserComponent } from './user/info-user/info-user.component';
import { authGuard } from './core/guards/auth.guard';
import { RegisterComponent } from './auth/register/register.component';
import { AppComponent } from './app.component';
import { MainComponent } from './layout/main/main.component';

export const routes: Routes = [
    { path: '', component: MainComponent }, // Главная страница 
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent } // Страница регистрации
];
