import { Component, ViewChild, TemplateRef, AfterViewInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements AfterViewInit {

  @ViewChild('content') content!: TemplateRef<any>;

  constructor(private modalService: NgbModal) {}

  ngAfterViewInit() {
    // Выводим контент в консоль, чтобы убедиться, что шаблон инициализирован
    if (this.content) {
      console.log('Template initialized:', this.content);
    } else {
      console.log('Template not found');
    }
  }

  navigateToLogin() {
    console.log('navigateToLogin method called');
    if (this.content) {
      console.log('Opening modal...');
      this.modalService.open(this.content, { centered: true });
    } else {
      console.log('Template not found');
    }
  }
}
