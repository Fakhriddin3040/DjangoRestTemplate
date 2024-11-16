import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { AppMenuComponent } from '../../../shared/components/menu/app-menu/app-menu.component';
import { MenuHomeLayoutComponent } from '../../../shared/components/menu/menu-home-layout/menu-home-layout.component';
import { MenuCategoryComponent } from '../../../shared/components/menu/menu-category/menu-category.component';
import { MenuProductComponent } from '../../../shared/components/menu/menu-product/menu-product.component';
import { MenuBlogComponent } from '../../../shared/components/menu/menu-blog/menu-blog.component';
import { TranslateModule, TranslateService } from '@ngx-translate/core';


import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-header-section4-menu',
  standalone: true,
  imports: [
    ContainerComponent,
    AppMenuComponent,
    MenuHomeLayoutComponent,
    MenuCategoryComponent,
    MenuProductComponent,
    MenuBlogComponent,
    MatButtonModule,
    TranslateModule
  ],
  templateUrl: './header-section4-menu.component.html',
  styleUrl: './header-section4-menu.component.scss',
})
export class HeaderSection4MenuComponent {
  constructor(    
    private translate: TranslateService
  ) {
    this.translate.setDefaultLang('ru'); // Установите язык по умолчанию
  }

  switchLanguage(language: string) {
    this.translate.use(language); // Метод для смены языка
  }
}

