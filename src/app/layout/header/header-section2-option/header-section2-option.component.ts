import { Component } from '@angular/core';
import { ContainerComponent } from '../../../shared/container/container.component';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MenuBlogComponent } from "../../../shared/components/menu/menu-blog/menu-blog.component";

@Component({
  selector: 'app-header-section2-option',
  standalone: true,
  imports: [
    ContainerComponent,
    MatButtonModule,
    MatSelectModule,
    MenuBlogComponent
],
  templateUrl: './header-section2-option.component.html',
  styleUrl: './header-section2-option.component.scss'
})
export class HeaderSection1OptionComponent {

  selected = 'option2';
  selected1 = 'option4';
}
