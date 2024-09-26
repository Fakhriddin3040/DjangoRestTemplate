import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { InfoUserComponent } from './user/info-user/info-user.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
];
