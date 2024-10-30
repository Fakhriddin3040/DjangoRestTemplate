import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
import { TranslateModule, TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-menu-product',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule, TranslateModule],
  templateUrl: './menu-product.component.html',
  styleUrl: './menu-product.component.scss'
})
export class MenuProductComponent {
  constructor(
   
    private translate: TranslateService
  ) {
    this.translate.setDefaultLang('ru'); // Установите язык по умолчанию
  }

  switchLanguage(language: string) {
    this.translate.use(language); // Метод для смены языка
  }
}
