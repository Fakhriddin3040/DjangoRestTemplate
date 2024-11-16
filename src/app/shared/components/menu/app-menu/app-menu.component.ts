import { Component, OnInit } from '@angular/core';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterModule } from '@angular/router';
import { BreadcrumbService } from '../../breadcrumb-navigation/breadcrumb.service';
import { MoyskladService } from '../../../../services/moysklad.service';
import { TranslateModule, TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-app-menu',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule, RouterModule, TranslateModule],
  templateUrl: './app-menu.component.html',
  styleUrl: './app-menu.component.scss',
})
export class AppMenuComponent implements OnInit {
  constructor(
    private breadcrumbService: BreadcrumbService,
    private dataFetchService: MoyskladService,
    private translate: TranslateService
  ) {
    this.translate.setDefaultLang('ru'); // Установите язык по умолчанию
  }

  switchLanguage(language: string) {
    this.translate.use(language); // Метод для смены языка
  }

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

        // Проверяем, есть ли данные
        if (data && data.length > 0) {
          this.sortedNames = data; // Сохраняем данные в sortedNames
          this.dataFetchService.updateData(data); // Сохраняем данные в сервисе
          console.log('AppMenuComponent - Данные успешно сохранены в сервисе:', data);
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
