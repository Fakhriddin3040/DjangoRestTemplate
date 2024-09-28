import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-menu-product',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule],
  templateUrl: './menu-product.component.html',
  styleUrl: './menu-product.component.scss'
})
export class MenuProductComponent {

}
