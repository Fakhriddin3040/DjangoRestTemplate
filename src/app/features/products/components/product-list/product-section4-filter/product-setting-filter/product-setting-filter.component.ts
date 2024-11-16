import { Component } from '@angular/core';
import { TranslateModule, TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-product-setting-filter',
  standalone: true,
  imports: [TranslateModule],
  templateUrl: './product-setting-filter.component.html',
  styleUrl: './product-setting-filter.component.scss'
})
export class ProductSettingFilterComponent {

  constructor(   
    private translate: TranslateService
  ) {
    this.translate.setDefaultLang('ru'); // Установите язык по умолчанию
  }

  switchLanguage(language: string) {
    this.translate.use(language); // Метод для смены языка
  }
}
