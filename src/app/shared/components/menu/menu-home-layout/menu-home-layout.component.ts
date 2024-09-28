import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-menu-home-layout',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule],
  templateUrl: './menu-home-layout.component.html',
  styleUrl: './menu-home-layout.component.scss'
})
export class MenuHomeLayoutComponent {

}
