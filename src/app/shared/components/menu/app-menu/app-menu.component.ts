import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-app-menu',
  standalone: true,
  imports: [
    MatButtonModule,
    MatMenuModule,
    RouterModule
    ],
  templateUrl: './app-menu.component.html',
  styleUrl: './app-menu.component.scss'
})
export class AppMenuComponent {
  
}
