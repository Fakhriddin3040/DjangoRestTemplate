import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { InfoUserComponent } from './user/info-user/info-user.component';
import { authGuard } from './core/guards/auth.guard';
import { RegisterComponent } from './auth/register/register.component';
import { AppComponent } from './app.component';
import { MainComponent } from './layout/main/main.component';
import { ProductListComponent } from './features/products/components/product-list/product-list.component';

export const routes: Routes = [
    { path: '', component: MainComponent }, 
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'products', component: ProductListComponent }
];
