import { Component } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-menu-blog',
  standalone: true,
  imports: [MatButtonModule, MatMenuModule],
  templateUrl: './menu-blog.component.html',
  styleUrl: './menu-blog.component.scss'
})
export class MenuBlogComponent {

}
