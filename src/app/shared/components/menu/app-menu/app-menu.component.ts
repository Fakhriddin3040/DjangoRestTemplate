import { Component } from '@angular/core';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterModule } from '@angular/router';
import { BreadcrumbService } from '../../breadcrumb-navigation/breadcrumb.service';
import { ProductService } from '../../../../features/products/services/product.service';

@Component({
  selector: 'app-app-menu',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule, RouterModule],
  templateUrl: './app-menu.component.html',
  styleUrl: './app-menu.component.scss',
})
export class AppMenuComponent {
  constructor(
    private breadcrumbService: BreadcrumbService,
    private dataService: ProductService
  ) {}

  onNavigateToConsumerElectric() {
    this.breadcrumbService.updateBreadcrumbs('Consumer Electric');
  }

 

  // Метод для получения данных при нажатии на кнопку
  fetchDataFromAnotherComponent() {
    this.dataService.fetchData().subscribe({
      next: (data) => {
        console.log('Данные из другого компонента:', data);
      },
      error: (error) => {
        console.error('Ошибка при загрузке данных:', error);
      }
    });
  }
}
