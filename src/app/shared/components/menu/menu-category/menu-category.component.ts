import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-menu-category',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule],
  templateUrl: './menu-category.component.html',
  styleUrl: './menu-category.component.scss'
})
export class MenuCategoryComponent {

}
