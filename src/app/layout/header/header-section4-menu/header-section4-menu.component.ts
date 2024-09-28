import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { AppMenuComponent } from "../../../shared/components/menu/app-menu/app-menu.component";
import { MenuHomeLayoutComponent } from "../../../shared/components/menu/menu-home-layout/menu-home-layout.component";
import { MenuCategoryComponent } from "../../../shared/components/menu/menu-category/menu-category.component";

@Component({
  selector: 'app-header-section4-menu',
  standalone: true,
  imports: [ContainerComponent, AppMenuComponent, MenuHomeLayoutComponent, MenuCategoryComponent],
  templateUrl: './header-section4-menu.component.html',
  styleUrl: './header-section4-menu.component.scss'
})
export class HeaderSection4MenuComponent {

}
