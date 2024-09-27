import { Component, EventEmitter, Output, ViewChild, AfterViewInit, OnInit } from '@angular/core';
import { InfoUserComponent } from '../../../user/info-user/info-user.component';
import { LoginComponent } from '../../../auth/login/login.component';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from '../../../core/services/auth.service';
import { CommonModule } from '@angular/common';
import { ContainerComponent } from "../../../shared/container/container.component";

@Component({
  selector: 'app-header-section3-utilities',
  standalone: true,
  imports: [
    CommonModule,
    InfoUserComponent,
    LoginComponent,
    ContainerComponent
],
  templateUrl: './header-section3-utilities.component.html',
  styleUrls: ['./header-section3-utilities.component.scss']
})
export class HeaderSection3UtilitiesComponent implements OnInit {
  selected = 'option2';

  @ViewChild('loginModal') loginModal: any;
  @Output() loginClick = new EventEmitter<void>();

   constructor(
    private modalService: NgbModal, 
    private router: Router,
    private authService: AuthService 
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
