import { Component } from '@angular/core';

import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterModule } from '@angular/router';
import { BreadcrumbService } from '../../breadcrumb-navigation/breadcrumb.service';
import { MoyskladService } from '../../../../services/moysklad.service';

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
    private dataFetchService: MoyskladService   

  ) {}

  onNavigateToConsumerElectric() {
    this.breadcrumbService.updateBreadcrumbs('Consumer Electric');
  }

  sortedNames: string[] = [];

 // Метод для получения данных через сервис
 fetchData() {
  this.dataFetchService.fetchData().subscribe({
    next: (data) => {
      if (data.rows && Array.isArray(data.rows)) {
        // Извлекаем и сортируем имена
        const names = data.rows.map((item: any) => item.name);
        this.sortedNames = names.sort((a: string, b: string) => a.localeCompare(b));

        // Выводим результат в консоль
        console.log('Отсортированные имена:', this.sortedNames);
      } else {
        console.log('Поле rows отсутствует или не является массивом.');
      }
    },
    error: (error) => {
      console.error('Ошибка при выполнении запроса:', error);
    },
  });
}

}
