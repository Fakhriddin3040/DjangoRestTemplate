import { Component, OnInit } from '@angular/core';

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
export class AppMenuComponent implements OnInit {
  constructor(
    private breadcrumbService: BreadcrumbService,
    private dataFetchService: MoyskladService
  ) {}

  onNavigateToConsumerElectric() {
    this.breadcrumbService.updateBreadcrumbs('Consumer Electric');
  }

  ngOnInit() {
    this.fetchData(); // Запрашиваем данные при инициализации
  }

  sortedNames: string[] = [];

  // Метод для получения данных через сервис
  fetchData() {
    this.dataFetchService.fetchData().subscribe({
      next: (data) => {
        console.log('AppMenuComponent - Полученные данные из API:', data);

        if (data && data.rows && data.rows.length > 0) {
          this.dataFetchService.updateData(data.rows); // Сохраняем только data.rows
          console.log('AppMenuComponent - Данные успешно сохранены в сервисе:', data.rows);
        } else {
          console.warn('AppMenuComponent - Пустой ответ от API или данные отсутствуют');
        } 
      },
      error: (error) => {
        console.error('AppMenuComponent - Ошибка при выполнении запроса:', error);
      },
    });
  }

}
