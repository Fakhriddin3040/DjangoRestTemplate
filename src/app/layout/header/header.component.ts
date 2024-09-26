import { Component, EventEmitter, Output, ViewChild, AfterViewInit   } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { ContainerComponent } from '../../shared/container/container.component';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { Router } from '@angular/router';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap';  // Подключение NgbModal
import { LoginComponent } from '../../auth/login/login.component';  // Импорт компонента входа



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
    LoginComponent
  ],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  
})
export class HeaderComponent {
  
  imageUrl = 'assets/images/promo/promo1.png';
  imageUrl2 = 'assets/images/promo/promo2.png';
  selected = 'option2';

  @ViewChild('loginModal') loginModal: any;
  @Output() loginClick = new EventEmitter<void>();

   constructor(private modalService: NgbModal, private router: Router) {}  // Добавляем NgbModal

  
  navigateToLogin() {
    console.log('navigateToLogin method called');
    const loginComponent = document.getElementById('content');
    if (loginComponent) {
      this.modalService.open(loginComponent, { centered: true });
    }
  }
}
